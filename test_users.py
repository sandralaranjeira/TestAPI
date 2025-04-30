import requests

def test_get_users(base_url):
    response = requests.get(f"{base_url}/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_user_by_id(base_url):
    user_id = 1
    response = requests.get(f"{base_url}/users/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == user_id
    assert "name" in data
