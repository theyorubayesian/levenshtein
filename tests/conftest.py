import pytest
from fastapi.testclient import TestClient

from levenshtein import app
from levenshtein.schema import Customer


@pytest.fixture()
def client():
    return TestClient(app)


@pytest.fixture()
def sample_name_true_positive():
    return {
        "first_name": "Jummy",
        "middle_name": "",
        "surname": "Plc."
    }


@pytest.fixture()
def sample_name_true_negative():
    return {
        "first_name": "Alphonso",
        "middle_name": "Oladapo",
        "surname": "Davies"
    }


@pytest.fixture()
def sample_name_true_negatives():
    return {
        "customers": [
            {
                "first_name": "Alphonso",
                "middle_name": "Oladapo",
                "surname": "Davies"
            },
            {
                "first_name": "Alphonso",
                "middle_name": "Oladapo",
                "surname": "Davies"
            },
        ]
    }


@pytest.fixture()
def sample_name_true_positives():
    return {
        "customers": [
            {
                "first_name": "Jummy",
                "middle_name": "",
                "surname": "Plc."
            },
            {
                "first_name": "Jummy",
                "middle_name": "",
                "surname": "Plc."
            },
        ]
    }


@pytest.fixture()
def sample_malformed_payload():
    return {
        "first_name": "",
        "surname": "Jummy"
    }

@pytest.fixture()
def sample_use_field_aliases():
    return {
        "first-name": "Olujimi",
        "middle-name": "Lingard",
        "surname": "Awoyokun"
    }

@pytest.fixture()
def customer_with_all_names(sample_name_true_negative):
    return Customer(**sample_name_true_negative)


@pytest.fixture()
def customer_without_middle_name(sample_name_true_positive):
    return Customer(**sample_name_true_positive)


@pytest.fixture()
def true_negative_name_list():
    return [
        "Alphonso Davies", "Davies Alphonso",
        "Alphonso Oladipo Davies", "Davies Oladapo Alphonso"
    ]

@pytest.fixture()
def true_positive_name_list():
    return [
        "UNIVERSITY OF IBADAN",
        "University Ibadan",
        "Ibadan University",
        "Ibadan of University"
    ]


@pytest.fixture()
def restricted_names():
    return [
        "Sterling Bank",
        "University of Ibadan (UI)",
        "Jumia Plc.",
        "Redeemed Christian Church of God"
    ]
