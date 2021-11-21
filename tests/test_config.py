import pytest
from api.app import app


@pytest.fixture(scope="module")
def test_api():
    with app.test_client() as client:
        yield client