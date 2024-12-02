import pytest
from biscuit import get_app_instance


@pytest.fixture(scope="session")
def app_instance():
    app = get_app_instance()
    yield app
