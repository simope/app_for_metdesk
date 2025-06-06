from app.main import my_app
from fastapi.testclient import TestClient
import pytest


@pytest.fixture
def client():
    return TestClient(my_app)
