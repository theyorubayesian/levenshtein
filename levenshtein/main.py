from typing import (
    Dict,
    List,
    Union
)

import yaml
from thefuzz import process
from fastapi import FastAPI

from levenshtein.schema import Customer
from levenshtein.schema import CustomerList
from levenshtein.schema import Vote

with open("settings.yml") as f:
    try:
        settings = yaml.safe_load(f)
    except yaml.YAMLError as err:
        print(err)
        raise err

app = FastAPI()

MATCH_CONFIDENCE: float = float(settings["MATCH_CONFIDENCE"])
RESTRICTED_NAMES: List[str] = settings["RESTRICTED_NAMES"]


def get_possible_names(customer: Customer) -> List[str]:
    """
    Get list of name combinations to test

    @param customer: 

    @return: Permutation of customer first, middle and last names.
    """
    names = [
        customer.first_name + " " + customer.surname,
        customer.surname + " " + customer.first_name,
    ]
    if customer.middle_name:
        names.extend([
            customer.first_name + " " + customer.middle_name + " " + customer.surname,
            customer.surname + " " + customer.middle_name + " " + customer.first_name
        ])
    return names


def validate_name(
    names: List[str], 
    restricted_names: List[str] = RESTRICTED_NAMES,
    match_confidence: float = MATCH_CONFIDENCE
) -> Dict[str, Union[bool, int, str]]:
    """


    @param names:
    @param restricted_names:
    @param match_confidence:

    @return:
    """
    for name in names:
        candidate = process.extractOne(
            name, restricted_names, score_cutoff=match_confidence)
        if candidate:
            return {
                "vote": False,
                "candidate": candidate[0],
                "match_score": candidate[1]
            }
    return {"vote": True}


@app.post("/validate-name/", response_model=Vote)
def single_validation(customer: Customer):
    names = get_possible_names(customer)
    result = validate_name(names, RESTRICTED_NAMES, MATCH_CONFIDENCE)
    return result


@app.post("/validate-names/", response_model=List[Vote])
def batch_validation(customers: CustomerList):
    results = []
    for customer in customers:
        names = get_possible_names(customer)
        result = validate_name(names, RESTRICTED_NAMES, MATCH_CONFIDENCE)
        results.append(result)
    return results


