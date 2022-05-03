from typing import List

import azure.functions as func
import yaml
from azure.functions import AsgiMiddleware
from fastapi import FastAPI

from levenshtein.schema import (
    Customer,
    CustomerList,
    Vote
)
from levenshtein.verify import get_possible_names
from levenshtein.verify import validate_name

with open("settings.yml") as f:
    try:
        settings = yaml.safe_load(f)
    except yaml.YAMLError as err:
        print(err)
        raise err

MATCH_CONFIDENCE: float = float(settings["MATCH-CONFIDENCE"])
RESTRICTED_NAMES: List[str] = settings["RESTRICTED-NAMES"]

app = FastAPI()


@app.post("/validate-name/", response_model=Vote)
async def single_validation(customer: Customer):
    names = get_possible_names(customer)
    result = validate_name(names, RESTRICTED_NAMES, MATCH_CONFIDENCE)
    return result


@app.post("/validate-names/", response_model=List[Vote])
async def batch_validation(customers: CustomerList):
    results = []
    for customer in customers.customers:
        names = get_possible_names(customer)
        result = validate_name(names, RESTRICTED_NAMES, MATCH_CONFIDENCE)
        results.append(result)
    return results


def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return AsgiMiddleware(app).handle(req, context)
