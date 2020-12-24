import pytest
def pytest_addoption(parser):
    parser.addoption("--container_openc", action="store", default="default name")
    parser.addoption("--container_db", action="store", default="default name")

@pytest.fixture
def param_opencart(request):
    container = request.config.getoption('--container')
    return container

@pytest.fixture
def param_db(request):
    container_db = request.config.getoption('--container_db')
    return container_db
