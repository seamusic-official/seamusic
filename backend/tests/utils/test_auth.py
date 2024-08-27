from datetime import datetime, timedelta, UTC

from fastapi import Depends, Request
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import EmailStr
import pytest
from unittest.mock import AsyncMock, patch

from src.core.config import settings
from src.exceptions.api import UnauthorizedException
from src.schemas.auth import User
from src.dtos.database.auth import User as _User
from src.services.auth import UsersService

from src.utils.auth import (get_current_user, get_hashed_password, get_refresh_token, 
                            authenticate_user, create_access_token, create_refresh_token, 
                            verify_password)

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 14  # 14 days
ALGORITHM = "HS256"
JWT_SECRET_KEY = settings.auth.JWT_SECRET_KEY
JWT_REFRESH_SECRET_KEY = settings.auth.JWT_REFRESH_SECRET_KEY


test_email = "test@example.com"
test_password = "password123"
hashed_password = get_hashed_password(test_password)

@pytest.fixture
@pytest.mark.utils
def mock_user_service():
    return AsyncMock(spec=UsersService)

@pytest.mark.asyncio
@pytest.mark.utils
async def test_authenticate_user(mock_user_service):
    mock_user_service.get_user_by_email = AsyncMock(return_value={
        'id': 1,
        'username': 'testuser',
        'email': test_email,
        'password': hashed_password,
        'picture_url': 'http://example.com/pic.jpg',
        'birthday': '2000-01-01'
    })

    user = await authenticate_user(test_email, test_password, service=mock_user_service)
    
    assert user is not None
    assert user.email == test_email
    assert user.password == hashed_password


@pytest.mark.asyncio
@pytest.mark.utils
async def test_authenticate_user_fail(mock_user_service):
    mock_user_service.get_user_by_email = AsyncMock(return_value=None)

    user = await authenticate_user(test_email, test_password, service=mock_user_service)
    
    assert user is None


@pytest.mark.asyncio
@pytest.mark.utils
async def test_get_current_user(mock_user_service):
    token_data = {"sub": 1, "exp": (datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)).timestamp()}
    token = create_refresh_token(token_data)

    mock_user_service.get_user_by_id = AsyncMock(return_value={
        'id': 1,
        'username': 'testuser',
        'email': test_email,
        'password': hashed_password,
        'picture_url': 'http://example.com/pic.jpg',
        'birthday': '2000-01-01'
    })

    user = await get_current_user(token=token, service=mock_user_service)

    assert user is not None
    assert user.id == 1
    assert user.email == test_email


@pytest.mark.asyncio
@pytest.mark.utils
async def test_get_current_user_unauthorized(mock_user_service):
    token = "invalid.token"

    with pytest.raises(UnauthorizedException):
        await get_current_user(token=token, service=mock_user_service)


@pytest.mark.parametrize("password,expected", [
    ("password123", True),
    ("wrongpassword", False),
])
@pytest.mark.utils
def test_verify_password(password, expected):
    if expected:
        assert verify_password(password, hashed_password) is True
    else:
        assert verify_password(password, hashed_password) is False