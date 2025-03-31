import requests

BASE_URL = "http://localhost:8000"

def test_add():
    response = requests.get(f"{BASE_URL}/add/-1/1")
    assert response.status_code == 200
    assert response.json() == {"result": 0}

def test_subtract():
    response = requests.get(f"{BASE_URL}/subtract/5/3")
    assert response.status_code == 200
    assert response.json() == {"result": 2}

def test_multiply():
    response = requests.get(f"{BASE_URL}/multiply/4/2")
    assert response.status_code == 200
    assert response.json() == {"result": 8}
