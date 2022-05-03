import logging

from fastapi.testclient import TestClient


def test_validate_name_tp(client: TestClient, sample_name_true_positive: dict):
    response = client.post("/validate-name/", json=sample_name_true_positive)
    assert response.status_code == 200
    assert response.json()["vote"] == False


def test_validate_name_tn(client: TestClient, sample_name_true_negative: dict):
    response = client.post("/validate-name/", json=sample_name_true_negative)
    logging.info(response)
    assert response.status_code == 200
    assert response.json()["vote"] == True


def test_validate_name_aliases(client: TestClient, sample_use_field_aliases: dict):
    response = client.post("/validate-name/", json=sample_use_field_aliases)
    assert response.status_code == 200


def test_validate_names_tp(client: TestClient, sample_name_true_positives: dict):
    response = client.post("/validate-names/", json=sample_name_true_positives)
    assert response.status_code == 200
    assert all([result["vote"]==False for result in response.json()])


def test_validate_names_tn(client: TestClient, sample_name_true_negatives: dict):
    response = client.post("/validate-names/", json=sample_name_true_negatives)
    assert response.status_code == 200
    assert all([result["vote"]==True for result in response.json()])
