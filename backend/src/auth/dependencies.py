from datetime import datetime, UTC

from fastapi import Depends, HTTPException, Request
from jose import jwt, JWTError

from src.auth.schemas import SUser
from src.auth.services import UsersDAO
from src.auth.utils import ALGORITHM, JWT_REFRESH_SECRET_KEY


async def get_refresh_token(request: Request):
    token = request.cookies.get("refreshToken")
    if not token:
        raise HTTPException(status_code=401)
    return token


async def get_current_user(token: str = Depends(get_refresh_token)) -> SUser:
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
