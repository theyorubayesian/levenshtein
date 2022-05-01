import pytest
from fastapi.testclient import TestClient

from levenshtein import app


@pytest.fixture()
def client():
    return TestClient(app)


@pytest.fixture()
def sample_name_true_positives():
    return {
        "first_name": "Jummy",
        "middle_name": "",
        "surname": "Plc."
    }


@pytest.fixture()
def sample_name_true_negatives():
    return {
        "first_name": "Jummy",
        "middle_name": "",
        "surname": "Plc."
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
