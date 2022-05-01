from fastapi.testclient import TestClient


def test_validate_name_tp(client: TestClient, sample_name_true_positives: dict):
    response = client.post("/validate-name/", json=sample_name_true_positives)
    assert response.status_code == 200
    assert response.json() == {"Income": ">50K"}


def test_validate_name_tn(client: TestClient, sample_name_true_negatives: dict):
    response = client.post("/validate-name/", json=sample_name_true_negatives)
    assert response.status_code == 200
    assert response.json() == {"Income": ">50K"} 


def test_validate_name_tp(client: TestClient, sample_name_aliases: dict):
    response = client.post("/validate-name/", json=sample_name_aliases)
    assert response.status_code == 200
    assert response.json() == {"Income": ">50K"}


def test_validate_names_tp(client: TestClient, sample_name_true_positives: dict):
    response = client.post("/validate-names/", json=sample_name_true_positives)
    assert response.status_code == 200
    assert response.json() == {"Income": ">50K"}


def test_validate_names_tn(client: TestClient, sample_name_true_negatives: dict):
    response = client.post("/validate-names/", json=sample_name_true_negatives)
    assert response.status_code == 200
    assert response.json() == {"Income": ">50K"}
