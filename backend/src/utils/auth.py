from datetime import datetime, timedelta, UTC

from fastapi import Depends, Request, HTTPException
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import EmailStr

from src.schemas.auth import User
from src.core.config import settings
from src.services.auth import UsersDAO


password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = (60 * 24 * 7) * 2  # 14 days
ALGORITHM = "HS256"
JWT_SECRET_KEY = settings.auth.JWT_SECRET_KEY  # should be kept secret
JWT_REFRESH_SECRET_KEY = settings.auth.JWT_REFRESH_SECRET_KEY  # should be kept secret


def get_hashed_password(password: str) -> str:
    return password_context.hash(password)


def verify_password(password: str, real_hashed_pass: str) -> bool:
    return password_context.verify(password, real_hashed_pass)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expires_delta = datetime.now(UTC) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expires_delta})

    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
    return encoded_jwt


def create_refresh_token(data: dict) -> str:
    to_encode = data.copy()
    expires_delta = datetime.now(UTC) + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expires_delta})

    encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, ALGORITHM)
    return encoded_jwt


async def authenticate_user(email: EmailStr, password: str):
    user = await UsersDAO.find_one_or_none(email=email)

    if user:
        if not verify_password(password, user.password):
            print(verify_password(password, user.password))
            return None
        return user
    return None


async def get_refresh_token(request: Request):
    token = request.cookies.get("refreshToken")
    if not token:
        raise HTTPException(status_code=401)
    return token


async def get_current_user(token: str = Depends(get_refresh_token)) -> User:
    try:
        payload = jwt.decode(token, JWT_REFRESH_SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=401)

    expire: str = payload.get("exp")

    if (not expire) or (int(expire) < datetime.now(UTC).timestamp()):
        raise HTTPException(status_code=401)
    user_id: str = payload.get("sub")
    if not user_id:
        raise HTTPException(status_code=401)
    user = await UsersDAO.find_one_by_id(int(user_id))
    if not user:
        raise HTTPException(status_code=401)

    return user
