from fastapi import UploadFile, File, APIRouter, Depends, HTTPException, Response
from src.config import settings
from src.beats.utils import unique_filename
from src.exceptions import CustomException, NotFoundException, NoRightsException
from src.notifications.utils import send_message
from src.auth.dependencies import get_current_user
from src.services import MediaRepository
from src.auth.services import UsersDAO, ArtistDAO, ProducerDAO, RoleDAO, UserToRoleDAO
from src.tags.services import ListenerTagsDAO, TagsDAO
from src.auth.utils import authenticate_user, create_access_token, create_refresh_token, get_hashed_password, verify_password
from src.auth.schemas import (SUser, SArtist, SProducer, SRegisterUser, SLoginUser,
                              SUserBase, SUserUpdate, SArtistUpdate, SProducerUpdate
                              )
from typing import List
import requests


auth = APIRouter(
    prefix = "/auth",
    tags = ["Auth & Users"]
)


"""
Users routes
"""
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


"""
Artists routes
"""
@auth.get('/users/artists/me', summary='Get my artist profile')
async def get_me_as_artist(user: SUser = Depends(get_current_user)) -> SArtist:
    artist_profile = await ArtistDAO.find_one_or_none(user=user)
    return artist_profile

@auth.get('/users/artists', summary='Get all artists')
async def get_artists() -> List[SArtist]:
    response = await ArtistDAO.find_all()
    return response

@auth.get('/users/artists/{id}', summary='Get one artists by id')
async def get_one_artist(id: int) -> SArtist:
    user = await ArtistDAO.find_one_by_id(id)
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

@auth.put('/users/artists/{id}', summary='Update artist by id')
async def update_artists(artist_id: int, data: SArtistUpdate, user: SUser = Depends(get_current_user)):
    if not user:
        raise NotFoundException()
    
    if user.id != artist_id:
        raise NoRightsException()
    
    update_data = {}

    if data.username:
        update_data["description"] = data.username

    await UsersDAO.edit_one(id, update_data)
    return SUser(**update_data)

@auth.delete('/users/artists/{id}', summary='Deactivate artist profile by id')
async def deactivate_artists(id: int, user: SUser = Depends(get_current_user)):
    if not user:
        raise NotFoundException()
    
    if user.id != id:
        raise NoRightsException()
    
    await ArtistDAO.delete(id)
    return CustomException(200, f"User with id {id} has been deleted")


"""
Producers routes
"""
@auth.get('/users/producers/me', summary='Get my producer profile')
async def get_me_as_producer(user: SUser = Depends(get_current_user)) -> SProducer:
    producer_profile = await ProducerDAO.find_one_or_none(user=user)
    return producer_profile

@auth.get('/users/producers', summary='Get all producers')
async def get_all_producers() -> List[SProducer]:
    response = await ProducerDAO.find_all()
    return response

@auth.get('/users/producers/{id}', summary='Get one producer by id')
async def get_one_producer() -> SProducer:
    response = await ProducerDAO.find_one_by_id()
    return response

@auth.put('/users/producers/{id}', summary='Update producer by id')
async def update_one_producer(artist_id: int, data: SArtistUpdate, user: SUser = Depends(get_current_user)):
    if not user:
        raise NotFoundException()
    
    if user.id != artist_id:
        raise NoRightsException()
    
    update_data = {}

    if data.username:
        update_data["description"] = data.username

    await UsersDAO.edit_one(id, update_data)
    return SUser(**update_data)

@auth.post('/users/producers/{id}', summary='Deactivate artist profile by id')
async def deactivate_one_producer(id: int, user: SUser = Depends(get_current_user)):
    if not user:
        raise NotFoundException()
    
    if user.id != id:
        raise NoRightsException()

    await ArtistDAO.edit_one(id, {"is_available": False})
    return CustomException(200, f"User with id {id} has been deleted")


"""
Auth routes
"""
@auth.post('/register', summary="Create new user")
async def register(user: SRegisterUser):
    existing_user = await UsersDAO.find_one_or_none(email=user.email)
    if existing_user:
        raise HTTPException(status_code=403)
    
    role_superuser = await RoleDAO.find_one_by_id(id=1)
    
    if not role_superuser: 
        role_superuser = await RoleDAO.add_one({"name": "superuser"})
        role_moder = await RoleDAO.add_one({"name": "moder"})
        role_producer = await RoleDAO.add_one({"name": "producer"})
        role_artist = await RoleDAO.add_one({"name": "artist"})
        role_listener = await RoleDAO.add_one({"name": "listener"})
    
    user_roles = []
    
    for role_name in user.roles:
        role = await RoleDAO.find_one_or_none(name=role_name)
        if role:
            user_roles.append(role)
        else:
            raise HTTPException(status_code=400, detail="Role not found")

    user_tags = []
    
    for tag_name in user.tags:
        tag = await TagsDAO.find_one_or_none(name=tag_name)

        if tag:
            user_tags.append(tag)
        else:
            raise HTTPException(status_code=400, detail="Role not found")

    hashed_password = get_hashed_password(user.password)

    user = await UsersDAO.add_one({
        "username": user.username,
        "email": user.email,
        "password": hashed_password,
        "birthday": user.birthday
    })
    
    for tag in user_roles:
        await ListenerTagsDAO.add_one({
            "user_id": user.id,
            "tag_id": tag.id
        })
    
    for role in user_roles:
        await UserToRoleDAO.add_one({
            "user_id": user.id,
            "role_id": role.id
        })
    
    artist_profile_id = await ArtistDAO.add_one({"description": "Hi, I'm an artist"})
    await UsersDAO.edit_one(user.id, {"artist_profile_id": artist_profile_id})
    await ProducerDAO.edit_one(artist_profile_id, {"is_available": False})

    producer_profile_id = await ProducerDAO.add_one({"description": "Hi, I'm a producer"})
    await UsersDAO.edit_one(user.id, {"producer_profile_id": producer_profile_id})
    await ArtistDAO.edit_one(user.id, {"is_available": False})

    return user.id

     
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
        'redirect_uri': "http://localhost:5173/profile",
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
