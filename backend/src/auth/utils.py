import os
import uuid
from datetime import datetime, timedelta, UTC

from fastapi import HTTPException, UploadFile
from jose import jwt
from passlib.context import CryptContext
from pydantic import EmailStr

from src.auth.services import UsersDAO
from src.config import settings


password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = (60 * 24 * 7) * 2  # 14 days
ALGORITHM = "HS256"
JWT_SECRET_KEY = settings.auth.JWT_SECRET_KEY   # should be kept secret
JWT_REFRESH_SECRET_KEY = settings.auth.JWT_REFRESH_SECRET_KEY   # should be kept secret


async def unique_filename(file: UploadFile) -> str:
    try:
        file_name, file_extension = os.path.splitext(file.filename)
        unique_filename_ = f"user_picture-{file_name.replace(' ', '-')}_{uuid.uuid4()}{file_extension}"
        return unique_filename_

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to process the audio file: {str(e)}")


def get_hashed_password(password: str) -> str:
    return password_context.hash(password)


def verify_password(password: str, real_hashed_pass: str) -> bool:
    return password_context.verify(password, real_hashed_pass)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expires_delta = datetime.now(UTC) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expires_delta})

    encoded_jwt = jwt.encode(
        to_encode,
        JWT_SECRET_KEY,
        ALGORITHM
        )
    return encoded_jwt


def create_refresh_token(data: dict) -> str:
    to_encode = data.copy()
    expires_delta = datetime.now(UTC) + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expires_delta})

    encoded_jwt = jwt.encode(
        to_encode,
        JWT_REFRESH_SECRET_KEY,
        ALGORITHM
        )
    return encoded_jwt


async def authenticate_user(email: EmailStr, password: str):
    user = await UsersDAO.find_one_or_none(email=email)

    if user:
        if not verify_password(password, user.password):
            print(verify_password(password, user.password))
            return None
        return user
    return None
