import json


def test_create_art(client):
    data = {
        "title": "Andy Warhol",
        "description": "Picture 1",
        "date_posted": "2021-12-06"
    }
    response = client.post("/art/create-art", json.dumps(data))
    assert response.status_code == 200
