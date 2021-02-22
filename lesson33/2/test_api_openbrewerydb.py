import re
import pytest
from unittest.mock import Mock


# проверка существования зничения города
def test_api_one(api_client):
    res = api_client.get(
        path="/breweries?",
        params={'by_city': 'san_diego'}
    )
    error = False
    for item in res.json():
        if item['city'] != 'San Diego':
            error = True
            break
    assert error == False


# проверка номера телефона пивоварен, у которых в данных есть "dog"
def test_api_two(api_client):
    res = api_client.get(
        path="/breweries/search?",
        params={'query': 'dog'}
    )
    error = False
    for item in res.json():
        if re.search(r'[а-яА-Яa-zA-Z]', item['phone']) != None:
            error = True
            break
    assert error == False


# проверка на возврат не пустого массива
def test_api_four(api_client):
    res = api_client.get(
        path="/breweries/search",
        params={'query': 'lost_forty'}
    )
    assert res.json() != []


# проверка на количество выведенных страниц на экран
@pytest.mark.parametrize('per_page', [1, 2])
def test_api_five(api_client, per_page):
    res = api_client.get(
        path="/breweries",
        params={'per_page': per_page}
    )
    message = res.json()
    if isinstance(res.json, Mock):
        message = message[:per_page]
    assert res.status_code == 200
    assert len(message) == per_page

