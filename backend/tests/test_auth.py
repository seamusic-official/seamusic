import pytest
from sqlalchemy import insert, select
from conftest import client, async_session_maker

def test_register():
    response = client.post("/auth/register", json={
        "username": "test_username",
        "email": "test_email@test.test",
        "birthday": "2024-06-30",
        "password": "test_password",
        "tags": ["supertrap, newjazz, rage, hyperpop"],
        "role": ["listener"]
    })

    assert response.status_code == 201