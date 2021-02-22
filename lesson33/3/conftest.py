import pytest
import requests
from unittest.mock import Mock

env = 'mock'


class testAPI:

    def __init__(self, base_address):
        self.base_address = base_address

    def post(self, path="/", params=None, data=None, headers=None):
        url = self.base_address + path
        print("POST request to {}".format(url))
        return requests.post(url=url, params=params, data=data, headers=headers)

    def get(self, path="/", params=None):
        url = self.base_address + path
        print("GET request to {}".format(url))
        return requests.get(url=url, params=params)

    def put(self, path="/", params=None, data=None, headers=None):
        url = self.base_address + path
        print("PUT request to {}".format(url))
        return requests.put(url=url, params=params, data=data)

    def delete(self, path="/", params=None):
        url = self.base_address + path
        print("DELETE request to {}".format(url))
        return requests.delete(url=url, params=params)


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://jsonplaceholder.typicode.com",
        help="This is request url"
    )


@pytest.fixture(scope="session")
def api_client(request):
    base_url = request.config.getoption("--url")
    if env == 'mock':
        return mock_class()
    return testAPI(base_address=base_url)


def mock_class(false=None):
    m = Mock(spec=testAPI)
    m.get().status_code = 200
    m.get().json.return_value = [{
        "userId": 1,
        "id": 5,
        "title": "laboriosam mollitia et enim quasi adipisci quia provident illum",
        "completed": false
    }
    ]
    m.post().json.return_value = [{
        'postId': 5,
        'name': 'vero',
        'email': 'tests@mail.ru',
        'body': 'harum'
    },
        {
            'postId': 77,
            'name': 'vero',
            'email': 'tests@mail.ru',
            'body': 'harum'
        }]
    m.put().json.return_value = {
        'postId': 77,
        'name': 'vero',
        'email': 'tests@mail.ru',
        'body': 'harum'
    }
    m.delete().json.return_value = {
    }
    return m
