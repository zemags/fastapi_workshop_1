import json


def test_create_owner(client):
    data = {"ownername": "testname", "email": "test@email.com", "password": "testpassword"}
    response = client.post("/owners/", json.dumps(data))
    assert response.status_code == 200
    assert response.json()["email"] == "test@email.com"
    assert response.json()["is_active"] == True
