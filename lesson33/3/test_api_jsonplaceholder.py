import pytest
from unittest.mock import Mock


# проверка на существование добавленных данных
def test_api_post_one(api_client):
    res = api_client.post(
        path="/comments",
        data={'postId': 77, 'name': 'vero', 'email': 'tests@mail.ru', 'body': 'harum'}
    )
    assert res.json()['name'] == 'vero'


# проверка на обновление данных
def test_api_put_two(api_client):
    res = api_client.put(
        path="/comments/67",
        data={'email': 'tests@mail.ru'}
    )
    print(res.json())
    assert res.json()['email'] == 'tests@mail.ru'


# проверка на удаление данных
def test_api_delete_three(api_client):
    res = api_client.delete(
        path="/comments/67"
    )
    assert (res.json()) == {}


# проверка на существование id (работает только с одним id)
@pytest.mark.parametrize('id', [5])
def test_api_put_four(api_client, id):
    res = api_client.get(
        path="/todos/" + str(id)
    )
    error = False
    for item in res.json():
        if item['id'] != id:
            error = True
            break
    assert error == False
