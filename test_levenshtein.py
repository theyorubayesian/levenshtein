def test_validate_name_tp(client, sample_name_true_positives):
    response = client.post("/validate-name/", json=sample_name_true_positives)
    assert response.status_code == 200
    assert response.json() == {"Income": ">50K"}


def test_validate_name_tn(client, sample_name_true_negatives):
    response = client.post("/validate-name/", json=sample_name_true_negatives)
    assert response.status_code == 200
    assert response.json() == {"Income": ">50K"} 


def test_validate_name_tp(client, sample_name_aliases):
    response = client.post("/validate-name/", json=sample_name_aliases)
    assert response.status_code == 200
    assert response.json() == {"Income": ">50K"}


def test_validate_names_tp(client, sample_name_true_positives):
    response = client.post("/validate-names/", json=sample_name_true_positives)
    assert response.status_code == 200
    assert response.json() == {"Income": ">50K"}


def test_validate_names_tn(client, sample_name_true_negatives):
    response = client.post("/validate-names/", json=sample_name_true_negatives)
    assert response.status_code == 200
    assert response.json() == {"Income": ">50K"}
