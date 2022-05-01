from typing import (
    Dict,
    List,
    Union
)

from thefuzz import process

from levenshtein.schema import Customer


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
    restricted_names: List[str],
    match_confidence: float,
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
