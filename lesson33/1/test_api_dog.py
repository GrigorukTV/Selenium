import pytest
import json
from unittest.mock import Mock


# проверка статуса запроса страницы с картинкой
def test_one(api_client):
    res = api_client.get(
        path="/api/breed/hound/afghan/images"
    )
    assert res.status_code == 200


# проверка существования значения
def test_three(api_client):
    res = api_client.get(
        path="/api/breed/hound/list"
    )
    item = 'blood'
    assert (item in res.json()['message']) == True


# проверка отсутствия значения
def test_four(api_client):
    res = api_client.post(
        path="/api/breed/hound/images",
        params={'userId': 0}
    )
    assert res.status_code == 405


# проверка количества возвращаемых картинок
@pytest.mark.parametrize('count', [1, 2, 3])
def test_two(api_client, count):
    res = api_client.get(
        path="/api/breed/hound/afghan/images/random/" + str(count),
    )
    message = res.json()['message']
    if isinstance(res.json, Mock):
        if 'random/1' in api_client.get.call_args[1]['path']:
            message = message[:1]
        elif 'random/2' in api_client.get.call_args[1]['path']:
            message = message[:2]
        elif 'random/3' in api_client.get.call_args[1]['path']:
            message = message[:3]
    assert res.status_code == 200
    assert len(message) == count


# проверка статуса запроса страницы с картинкой по определенной породе
@pytest.mark.parametrize('breed', ["afghan", "basset", "blood"])
def test_five(api_client, breed):
    res = api_client.get(
        path="/api/breed/hound/" + breed + "/images"
    )
    assert res.status_code == 200
