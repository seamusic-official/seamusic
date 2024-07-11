from fastapi import UploadFile, File, APIRouter, Depends, HTTPException, Response
from typing import List
import requests

from src.exceptions import CustomException, NotFoundException, NoRightsException
from src.notifications.utils import send_message
from src.auth.dependencies import get_current_user
from src.services import MediaRepository
from src.auth.services import UsersDAO, ArtistDAO, ProducerDAO
from src.auth.utils import authenticate_user, create_access_token, create_refresh_token, get_hashed_password, verify_password
from src.auth.schemas import SUser, SArtist, SProducer, SRegisterUser, SLoginUser, SUserBase, SUserUpdate, SUserResponse
from src.config import settings
from src.beats.utils import unique_filename


auth = APIRouter(
    prefix = "/auth",
    tags = ["Auth & Users"]
)

redirect_uri = "http://localhost:5173"


@auth.get('/users/me', summary='Get details of currently logged in user')
async def get_me(user: SUser = Depends(get_current_user)) -> SUser:
    return user 

@auth.get('/users', summary='Get all users')
async def get_users() -> List[SUser]:
    response = await UsersDAO.find_all()
    return response

@auth.get("/users/{id}", summary="Get a user by ID")
async def get_one(id: int) -> SUser:
    user = await UsersDAO.find_one_by_id(id)
    if not user:
        raise NotFoundException()
    
    user_dict = {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "picture_url": user.picture_url,
        "birthday": user.birthday,
        "role": user.role,
        "updated_at": user.updated_at,
        "created_at": user.created_at
    }

    return SUser(**user_dict)

@auth.put('/users/picture/{id}', summary='Update image info by id')
async def update_user_picture(id: int, file: UploadFile = File(...), user: SUser = Depends(get_current_user)):
    if user.id != id:
        raise NoRightsException()
    
    filename = await unique_filename(file) if file else None
    picture_url = await MediaRepository.upload_file("PICTURES", filename, file)
    
    update_data = {
        "picture_url": picture_url
    }
    await UsersDAO.edit_one(id, update_data)
    return CustomException(200, f"User {user.username} picture_url has been updated")

@auth.put('/users/{id}', summary='Update user info by id')
async def update_user(id: int, data: SUserUpdate, user: SUser = Depends(get_current_user)):
    if not user:
        raise NotFoundException()

    if user.id != id:
        raise NoRightsException()
    
    update_data = {}

    if data.username:
        update_data["username"] = data.username
    if data.email:
        update_data["email"] = data.email
    if data.picture_url:
        update_data["picture_url"] = data.picture_url

    await UsersDAO.edit_one(id, update_data)
    return update_data

@auth.delete('/users/{id}', summary='Delete user by id')
async def delete_users(id: int, user: SUser = Depends(get_current_user)):
    if not user:
        raise NotFoundException()
    
    if user.id != id:
        raise NoRightsException()
    
    await UsersDAO.delete(id)
    return CustomException(200, f"User with id {id} has been deleted")

@auth.get('/users/artists', summary='Get all artists')
async def get_artists() -> List[SArtist]:
    response = await ArtistDAO.find_all()
    return response

@auth.get('/users/artists/{id}', summary='Get one artists by id')
async def get_one_artist() -> List[SArtist]:
    response = await UsersDAO.find_one_by_id()
    return response

@auth.put('/users/artists/{id}', summary='Update artist by id')
async def update_artists():
    response = await UsersDAO.edit_one()
    return response

@auth.get('/users/producers', summary='Get all producers')
async def get_producers():
    response = await ProducerDAO.find_all()
    return response

@auth.get('/users/producers/{id}', summary='Get one producer by id')
async def get_producer():
    response = await ProducerDAO.find_one_by_id()
    return response

@auth.put('/users/producers/{id}', summary='Update producer by id')
async def update_producer():
    response = await ProducerDAO.edit_one()
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
    
    print(f"{user_id} FSDEWJKKJLREJKL:")
    
    if user.role == "Artist":
        artist_profile_data = {
            "description": "Hi, I'm an artist"
        }
        artist_profile_id = await ArtistDAO.add_one(artist_profile_data)

        await UsersDAO.edit_one(user_id, {"artist_profile_id": artist_profile_id})

    if user.role == "Producer":
        producer_profile_data = {
            "description": "Hi, I'm a producer"
        }
        producer_profile_id = await ProducerDAO.add_one(producer_profile_data)

        await UsersDAO.edit_one(user_id, {"producer_profile_id": producer_profile_id})

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
