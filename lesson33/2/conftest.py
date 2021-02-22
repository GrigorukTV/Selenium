import pytest
import requests
from unittest.mock import Mock

from docutils.parsers import null

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


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://api.openbrewerydb.org5",
        help="This is request url"
    )


@pytest.fixture(scope="session")
def api_client(request):
    base_url = request.config.getoption("--url")
    if env == 'mock':
        return mock_class()
    return testAPI(base_address=base_url)


def mock_class():
    m = Mock(spec=testAPI)
    m.get().status_code = 200
    m.get().json.return_value = [{
        "id": 430,
        "name": "Dog Brewhouse",
        "brewery_type": "planning",
        "street": "",
        "address_2": null,
        "address_3": null,
        "city": "San Diego",
        "state": "California",
        "county_province": null,
        "postal_code": "94612-2110",
        "country": "United States",
        "longitude": "-122.2698881",
        "latitude": "37.807739",
        "phone": "5103061914",
        "website_url": "http://www.divingdogbrew.com",
        "updated_at": "2018-08-23T23:27:26.494Z",
        "created_at": "2018-07-24T01:32:54.478Z"
    },
        {
            "id": 430,
            "name": "Dog Brewhouse",
            "brewery_type": "planning",
            "street": "",
            "address_2": null,
            "address_3": null,
            "city": "San Diego",
            "state": "California",
            "county_province": null,
            "postal_code": "94612-2110",
            "country": "United States",
            "longitude": "-122.2698881",
            "latitude": "37.807739",
            "phone": "5103061914",
            "website_url": "http://www.divingdogbrew.com",
            "updated_at": "2018-08-23T23:27:26.494Z",
            "created_at": "2018-07-24T01:32:54.478Z"
        }
    ]
    m.post().status_code = 405
    return m
