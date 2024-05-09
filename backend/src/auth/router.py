from fastapi import Depends, Request, APIRouter
from src.auth.dependencies import get_current_user
from fastapi import APIRouter, HTTPException, Response, Depends
from src.auth.services import UsersDAO
from src.auth.utils import authenticate_user, create_access_token, create_refresh_token, get_hashed_password, verify_password
from src.auth.schemas import SUser, SArtist, SListener, SProducer, SRegisterUser, SLoginUser
from src.config import settings
import requests

auth = APIRouter(
    prefix = "/auth",
    tags = ["Auth & Users"]
)

redirect_uri = "http://localhost:5173"

@auth.post('/register', summary="Create new user")
async def register(user: SRegisterUser):
    existing_user = await UsersDAO.find_one_or_none(email=user.email)
    if existing_user:
        raise HTTPException(status_code=403)
    
    hashed_password = get_hashed_password(user.password)

    user = {
        "username": user.username,
        "email": user.email,
        "password": hashed_password,
        "role": user.role,
        "birthday": user.birthday
    }
    await UsersDAO.add_one(user)
    return user

@auth.post('/login', summary="Signin")
async def login(user: SLoginUser, response: Response):
    auth_user = await authenticate_user(email=user.email, password=user.password)
    print(auth_user)
    if not auth_user:
        raise HTTPException(status_code=401)

    access_token = create_access_token({"sub":  str(auth_user.id)})
    refresh_token = create_refresh_token({"sub":  str(auth_user.id)})

    response.set_cookie(key="refreshToken", value=refresh_token, httponly=True, samesite="Strict")
    
    return {
        "accessToken": access_token,
        "refreshToken": refresh_token,
        "user": auth_user,
    }


@auth.post('/refresh')
async def refresh(user: SUser = Depends(get_current_user)) -> dict:
    if not user:
        HTTPException(status_code=401, detail="refresh token is not valid")

    access_token = create_access_token({"sub":  str(user.id)})
    refresh_token = create_refresh_token({"sub":  str(user.id)})

    return {
        'accessToken': access_token,
        'refreshToken': refresh_token
    }


@auth.get('/users/me', summary='Get details of currently logged in user')
async def get_me(user: SUser = Depends(get_current_user)):
    return user 

@auth.get('/users/artists', summary='Get details of currently logged in user')
async def get_artists():
    response = await UsersDAO.find_all_artists()
    return response

@auth.post("/callback")
async def spotify_callback(code, response: Response):
    payload = {
        'code': code,
        'client_id': settings.spotify.CLIENT_ID,
        'client_secret': settings.spotify.CLIENT_SECRET,
        "grant_type": "authorization_code",
        'redirect_uri': redirect_uri,
    }

    auth_response = requests.post('https://accounts.spotify.com/api/token', headers={'Content-Type': 'application/x-www-form-urlencoded'}, data=payload)
    auth_response_data = auth_response.json()

    access_token = auth_response_data.get('access_token')
    refresh_token = auth_response_data.get('refresh_token')

    if access_token:
        user_response = requests.get('https://api.spotify.com/v1/me', headers={'Authorization': f'Bearer {access_token}'})
        user_data = user_response.json() 

        user = await UsersDAO.find_one_or_none(email=user_data.get('email'))
        if not user:
            new_user = {
                "username": user_data.get('username'),
                "email": user_data.get('email'),
                "password": None
            }
            print(new_user)
            await UsersDAO.add_one(new_user)
            user = new_user
            access_token = create_access_token({"sub":  str(user.id)})
            refresh_token = create_refresh_token({"sub":  str(user.id)})
            response.set_cookie("refresh_token", refresh_token, httponly=True)
            return {
                "id": user.id,
                "access_token": access_token,
                "refresh_token": refresh_token
            }
        else:
            access_token = create_access_token({"sub":  str(user.id)})
            refresh_token = create_refresh_token({"sub":  str(user.id)})

            response.set_cookie("refresh_token", refresh_token, httponly=True)

            return {
                "id": user.id,
                "access_token": access_token,
                "refresh_token": refresh_token
            }
    else:
        return {'error': 'Failed to obtain access token'}
