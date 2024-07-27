import pytest
from fastapi import UploadFile, Response
from fastapi.testclient import TestClient
from httpx import Response

from src.auth.schemas import SUserResponse


email = 'test_email2@test.test'
password = 'test_password'


def test_register(client: TestClient) -> None:
    response: Response = client.post(
        url='/auth/register',
        json={
            'username': 'test_username2',
            'email': email,
            'birthday': '2024-06-30',
            'password': password,
            'tags': ['supertrap, newjazz, rage, hyperpop'],
            'role': ['listener']
        }
    )
    assert response.status_code == 201


@pytest.mark.parametrize(
    'password_,expected_status_code',
    [(password, 200), ('wrong_password_1', 401), ('wrong_password_2', 401)]
)
def test_login(client: TestClient, password_: str, expected_status_code: int) -> None:
    response: Response = client.post(
        url='/auth/login',
        json={
            'email': 'test_email@test.test',
            'password': password_
        }
    )
    assert response.status_code == expected_status_code


def test_get_me(client: TestClient) -> None:
    response: Response = client.get('/auth/users/me')
    assert response.status_code == 200


def test_get_users(client: TestClient) -> None:
    response: Response = client.get('/auth/users/')
    assert response.status_code == 200


def test_get_one(client: TestClient, user: SUserResponse) -> None:
    response: Response = client.get(f'/auth/users/{user.id}')
    assert response.status_code == 200


def test_update_user_picture(client: TestClient, user: SUserResponse) -> None:
    with open('some_file', 'rb') as file:
        response: Response = client.put(
            url=f'/auth/users/picture/{user.id}',
            json={'file': UploadFile(file=file)}
        )
    assert response.status_code == 200


def test_update_user(client: TestClient, user: SUserResponse) -> None:
    response: Response = client.put(
        url=f'/auth/users/{user.id}',
        json={
            'username': '',
            'email': '',
            'picture_url': '',
            'tags': ['supertrap, newjazz, rage'],
            'roles': ['artist', 'producer', 'listener']
        }
    )
    assert response.status_code == 200


def test_delete_user(client: TestClient, user: SUserResponse) -> None:
    response: Response = client.delete(f'/auth/users/{user.id}')
    assert response.status_code == 200


def test_get_me_as_artist(client: TestClient) -> None:
    response: Response = client.get('/auth/users/artists/me')
    assert response.status_code == 200


def test_get_artists(client: TestClient) -> None:
    response: Response = client.get('/auth/users/artists')
    assert response.status_code == 200


def test_get_one_artist(client: TestClient, user: SUserResponse) -> None:
    response: Response = client.get(f'/auth/users/artists/{user.id}')
    assert response.status_code == 200


def test_update_artists(client: TestClient, user: SUserResponse) -> None:
    response: Response = client.put(
        url=f'/auth/users/artists/{user.id}',
        json={'description': 'new_description'}
    )
    assert response.status_code


def test_deactivate_artists(client: TestClient, user: SUserResponse) -> None:
    response: Response = client.delete(f'/auth/users/artists/{user.id}')
    assert response.status_code == 200


def test_get_me_as_producer(client: TestClient) -> None:
    response: Response = client.get('/auth/users/producers/me')
    assert response.status_code == 200


def test_get_all_producers(client: TestClient) -> None:
    response: Response = client.get('/auth/users/producers')
    assert response.status_code == 200


def test_get_one_producer(client: TestClient, user: SUserResponse) -> None:
    response: Response = client.get(f'/auth/users/producers/{user.id}')
    assert response.status_code == 200


def test_update_one_producer(client: TestClient, user: SUserResponse) -> None:
    response: Response = client.put(
        url=f'/auth/users/producers/{user.id}',
        json={'description': 'new_description'}
    )
    assert response.status_code == 200


def test_deactivate_one_producer(client: TestClient, user: SUserResponse) -> None:
    response: Response = client.post(f'/auth/users/producers/{user.id}')
    assert response.status_code == 200


def test_refresh(client: TestClient) -> None:
    response: Response = client.post('/auth/refresh')
    assert response.status_code == 200


def test_spotify_callback(client: TestClient) -> None:
    response: Response = client.post('/auth/callbcak')
    assert response.status_code == 200
