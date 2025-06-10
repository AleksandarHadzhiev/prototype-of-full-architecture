import pytest

from fastapi.testclient import TestClient 

from src.main import create_app

app = create_app("test")
client = TestClient(app)

# First is the page we are looking for, 
# next, the status_code, finally what we expect
# to be in the content of the page
test_cases = [
    ("/aleks", 200, {"message": "Hello, aleks! Welcome to the app :)"}),
]


@pytest.mark.parametrize("user, status_code, response_body", test_cases)
def test_greet_user(user: str, status_code: int, response_body: dict):
    response = client.get(user)
    assert response.status_code == status_code
    assert response.json() == response_body