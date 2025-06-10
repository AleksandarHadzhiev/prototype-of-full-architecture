from fastapi.testclient import TestClient 
from src.app import create_app

app = create_app("test")
client = TestClient(app)

def test_gets_index_page():
    response = client.get("/index")
    assert response.status_code == 200
    assert "css/index.css" in response.text