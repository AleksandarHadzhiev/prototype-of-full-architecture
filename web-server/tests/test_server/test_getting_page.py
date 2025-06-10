import pytest

from fastapi.testclient import TestClient 
from src.app import create_app

app = create_app("test")
client = TestClient(app)

# First is the page we are looking for, 
# next, the status_code, finally what we expect
# to be in the content of the page
test_cases = [
    ("/index", 200, "css/index.css"),
    ("/not-found", 200, "css/not-found.css"),
    ("/page-does-not-exist", 404, "css/not-found.css"),
]


@pytest.mark.parametrize("page, status_code, css_style", test_cases)
def test_gets_index_page(page: str, status_code: int, css_style: str):
    response = client.get(page)
    assert response.status_code == status_code
    assert css_style in response.text