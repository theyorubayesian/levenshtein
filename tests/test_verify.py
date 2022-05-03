import json

from levenshtein.verify import get_possible_names
from levenshtein.verify import validate_name


def test_customer_all_names(customer_with_all_names):
    names = get_possible_names(customer_with_all_names)
    expected_names = [
        "alphonso davies", "davies alphonso",
        "alphonso oladapo davies", "davies oladapo alphonso"
    ]
    assert sorted(names) == sorted(expected_names), "Returned name list does not match expectations"


def test_customer_no_middle_name(customer_without_middle_name):
    names = get_possible_names(customer_without_middle_name)
    expected_names = ["jummy plc.", "plc. jummy"]
    assert sorted(names) == sorted(expected_names), "Returned name list does not match expectations"


def test_validate_name_pass(true_negative_name_list, restricted_names):
    validation = validate_name(true_negative_name_list, restricted_names, 70)
    assert json.dumps(validation, sort_keys=True) == \
        json.dumps({"vote": True}, sort_keys=True), \
            "`Wrong validation result`. Expected `{'vote': True}`"


def test_validate_name_fail(true_positive_name_list, restricted_names):
    validation = validate_name(true_positive_name_list, restricted_names, 70)
    assert validation["vote"] == False, "Incorrect vote for customer. Expected False."
    assert "candidate" in validation, "`candidate` not returned"
    assert "match_score" in validation, "`match_score` not returned"
