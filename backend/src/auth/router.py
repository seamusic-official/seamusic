from fastapi import Depends, Request, APIRouter
from src.notifications.utils import send_message
from src.auth.dependencies import get_current_user
from fastapi import APIRouter, HTTPException, Response, Depends
from src.auth.services import UsersDAO, ArtistDAO, ProducerDAO
from src.auth.utils import authenticate_user, create_access_token, create_refresh_token, get_hashed_password, verify_password
from src.auth.schemas import SUser, SArtist, SProducer, SRegisterUser, SLoginUser
from src.config import settings
import requests

auth = APIRouter(
    prefix = "/auth",
    tags = ["Auth & Users"]
)

redirect_uri = "http://localhost:5173"


@auth.get('/users/me', summary='Get details of currently logged in user')
async def get_me(user: SUser = Depends(get_current_user)):
    return user 

@auth.get('/users', summary='Get all users')
async def get_users():
    response = await UsersDAO.find_all()
    return response

@auth.get('/users/{id}', summary='Get one user by id')
async def get_users(id):
    response = await UsersDAO.find_one_by_id(id)
    return response

@auth.put('/users/{id}', summary='Update user info by id')
async def update_users(id):
    response = await UsersDAO.edit_one(id)
    return response

@auth.delete('/users/{id}', summary='Delete user by id')
async def delete_users(id):
    response = await UsersDAO.delete(id)
    return response

@auth.get('/users/artists', summary='Get all artists')
async def get_artists():
    response = await UsersDAO.find_all_artists()
    return response

@auth.get('/users/artists/{id}', summary='Get one artists by id')
async def get_artist():
    response = await UsersDAO.find_one_by_id()
    return response

@auth.put('/users/artists/{id}', summary='Update artist by id')
async def update_artist():
    response = await UsersDAO.edit_one()
    return response

@auth.get('/users/producers', summary='Get all producers')
async def get_producers():
    response = await UsersDAO.find_all_producers()
    return response

@auth.get('/users/producers/{id}', summary='Get one producer by id')
async def get_producer():
    response = await UsersDAO.find_one_by_id()
    return response

@auth.put('/users/producers/{id}', summary='Update producer by id')
async def update_producer():
    response = await UsersDAO.edit_one()
    return response


@auth.post('/register', summary="Create new user")
async def register(user: SRegisterUser):
    existing_user = await UsersDAO.find_one_or_none(email=user.email)
    if existing_user:
        raise HTTPException(status_code=403)

    hashed_password = get_hashed_password(user.password)

    user_data = {
        "username": user.username,
        "email": user.email,
        "password": hashed_password,
        "role": user.role,
        "birthday": user.birthday
    }

    user_id = await UsersDAO.add_one(user_data)
    
    # print(f"{user_id} FSDEWJKKJLREJKL:")
    
    # if user.role == "Artist":
    #     artist_profile_data = {
    #         "description": "Hi, I'm an artist"
    #     }
    #     artist_profile_id = await ArtistDAO.add_one(artist_profile_data)
    #     print(f"{artist_profile_id} TFGDHJKSADFRWEUIFWEUIMNUIMNEWUIOFEFWEFWWEFUSDFI")
    #     artist_profile = await ArtistDAO.find_one_by_id(artist_profile_id)

    #     await UsersDAO.edit_one(user_id, {"artist_profile": artist_profile})
        
    # if user.role == "Producer":
    #     producer_profile_data = {
    #         "description": "Hi, im a producer",
    #     }
    #     producer_profile_id = await ProducerDAO.add_one(producer_profile_data)
    #     producer_profile = await ProducerDAO.find_one_by_id(producer_profile_id)

    #     await UsersDAO.edit_one(user_id, {"producer_profile": producer_profile})
    send_message(f"Your account was created, {user.username}", user.email)
    return user_id


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
