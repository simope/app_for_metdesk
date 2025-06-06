from .expectations import messages, codes


def test_knock(client):
    response = client.get("/knock")
    assert response.status_code == codes["knock"]
    assert response.json() == messages["knock"]
