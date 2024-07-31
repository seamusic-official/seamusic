from typing import List

import requests
from fastapi import (
    UploadFile,
    File,
    APIRouter,
    Depends,
    HTTPException,
    Response,
    status,
)

from src.auth.dependencies import get_current_user
from src.auth.schemas import (
    SUser,
    SArtist,
    SProducer,
    SRegisterUser,
    SLoginUser,
    SUserUpdate,
    SArtistUpdate,
    SRefreshTokenResponse,
    SUserUpdateResponse,
    SUserResponse,
    SUserEditImageResponse,
    SUserDeleteResponse,
    SArtistDeleteResponse,
    SProducerDeleteResponse,
    SAuthUserRegisterResponse,
    SUserLoginResponse,
    SSpotifyCallbackResponse,
)
from src.auth.services import UsersDAO, ArtistDAO, ProducerDAO, RoleDAO, UserToRoleDAO
from src.auth.utils import (
    authenticate_user,
    create_access_token,
    create_refresh_token,
    get_hashed_password,
)
from src.beats.utils import unique_filename
from src.config import settings
from src.exceptions import NotFoundException, NoRightsException
from src.services import MediaRepository
from src.tags.services import ListenerTagsDAO, TagsDAO


auth = APIRouter(prefix="/auth", tags=["Auth & Users"])


"""
Users routes
"""


@auth.get(
    path="/users/me",
    response_model=SUserResponse,
    summary="Get details of currently logged in user",
    status_code=status.HTTP_200_OK,
    responses={status.HTTP_200_OK: {"model": SUserResponse}},
)
async def get_me(user: SUser = Depends(get_current_user)) -> SUserResponse:
    return SUserResponse(
        id=user.id,
        username=user.username,
        email=user.email,
        picture_url=user.picture_url,
        birthday=user.birthday,
    )


@auth.get(
    path="/users",
    response_model=List[SUserResponse],
    summary="Get all users",
    status_code=status.HTTP_200_OK,
    responses={status.HTTP_200_OK: {"model": List[SUserResponse]}},
)
async def get_users() -> List[SUserResponse]:
    response = await UsersDAO.find_all()

    return [SUserResponse.from_db_model(user=user) for user in response]


@auth.get(
    path="/users/{user_id}",
    response_model=SUserResponse,
    summary="Get a user by ID",
    status_code=status.HTTP_200_OK,
    responses={status.HTTP_200_OK: {"model": SUserResponse}},
)
async def get_one(user_id: int) -> SUserResponse:
    user = await UsersDAO.find_one_by_id(user_id)

    if not user:
        raise NotFoundException()

    return SUserResponse.from_db_model(user=user)


@auth.put(
    path="/users/picture/{user_id}",
    summary="Update image info by id",
    response_model=SUserEditImageResponse,
    responses={status.HTTP_200_OK: {"model": SUserEditImageResponse}},
)
async def update_user_picture(
    user_id: int, file: UploadFile = File(...), user: SUser = Depends(get_current_user)
) -> SUserEditImageResponse:
    if user.id != user_id:
        raise NoRightsException()

    filename = await unique_filename(file) if file else None
    picture_url = await MediaRepository.upload_file("PICTURES", filename, file)

    update_data = {"picture_url": picture_url}
    await UsersDAO.edit_one(user_id, update_data)
    return SUserEditImageResponse


@auth.put(
    path="/users/{user_id}",
    summary="Update user info by id",
    response_model=SUserUpdateResponse,
    responses={status.HTTP_200_OK: {"model": SUserUpdateResponse}},
)
async def update_user(
    user_id: int, data: SUserUpdate, user: SUser = Depends(get_current_user)
) -> SUserUpdateResponse:
    if not user:
        raise NotFoundException()

    if user.id != user_id:
        raise NoRightsException()

    update_data = {}

    if data.username:
        update_data["username"] = data.username
    if data.email:
        update_data["email"] = data.email
    if data.picture_url:
        update_data["picture_url"] = data.picture_url

    await UsersDAO.edit_one(user_id, update_data)

    return SUserUpdateResponse(
        username=data.username, email=data.email, picture_url=data.picture_url
    )


@auth.delete(
    path="/users/{user_id}",
    summary="Delete user by id",
    response_model=SUserDeleteResponse,
    responses={status.HTTP_200_OK: {"model": SUserDeleteResponse}},
)
async def delete_users(
    user_id: int, user: SUser = Depends(get_current_user)
) -> SUserDeleteResponse:
    if not user:
        raise NotFoundException()

    if user.id != user_id:
        raise NoRightsException()

    await UsersDAO.delete(user_id)
    return SUserDeleteResponse


"""
Artists routes
"""


@auth.get(
    path="/users/artists/me",
    response_model=SArtist,
    summary="Get my artist profile",
    status_code=status.HTTP_200_OK,
    responses={status.HTTP_200_OK: {"model": SArtist}},
)
async def get_me_as_artist(user: SUser = Depends(get_current_user)) -> SArtist:
    artist_profile = await ArtistDAO.find_one_or_none(user=user)
    return artist_profile


@auth.get(
    path="/users/artists",
    response_model=List[SArtist],
    summary="Get all artists",
    status_code=status.HTTP_200_OK,
    responses={status.HTTP_200_OK: {"model": List[SArtist]}},
)
async def get_artists() -> List[SArtist]:
    response = await ArtistDAO.find_all()
    return response


@auth.get(
    path="/users/artists/{artist_id}",
    response_model=SArtist,
    summary="Get one artists by id",
    status_code=status.HTTP_200_OK,
    responses={status.HTTP_200_OK: {"model": SArtist}},
)
async def get_one_artist(artist_id: int) -> SArtist:
    user = await ArtistDAO.find_one_by_id(artist_id)
    if not user:
        raise NotFoundException()

    # user_dict = {
    #     "id": user.id,
    #     "username": user.username,
    #     "email": user.email,
    #     "picture_url": user.picture_url,
    #     "birthday": user.birthday,
    #     "role": user.role,
    #     "updated_at": user.updated_at,
    #     "created_at": user.created_at,
    # }

    return SUserResponse(user=user)


@auth.put(
    path="/users/artists/{artist_id}",
    response_model=SUser,
    summary="Update artist by id",
    status_code=status.HTTP_200_OK,
    responses={status.HTTP_200_OK: {"model": SUser}},
)
async def update_artists(
    artist_id: int, data: SArtistUpdate, user: SUser = Depends(get_current_user)
) -> SUser:
    if not user:
        raise NotFoundException()

    if user.id != artist_id:
        raise NoRightsException()

    update_data = {}

    if data.username:
        update_data["description"] = data.username

    await UsersDAO.edit_one(artist_id, update_data)
    return SUser(**update_data)


@auth.delete(
    path="/users/artists/{artist_id}",
    summary="Deactivate artist profile by id",
    response_model=SArtistDeleteResponse,
    responses={status.HTTP_200_OK: {"model": SArtistDeleteResponse}},
)
async def deactivate_artists(artist_id: int, user: SUser = Depends(get_current_user)):
    if not user:
        raise NotFoundException()

    if user.id != artist_id:
        raise NoRightsException()

    await ArtistDAO.delete(artist_id)
    return SArtistDeleteResponse


"""
Producers routes
"""


@auth.get(
    path="/users/producers/me",
    response_model=SProducer,
    summary="Get my producer profile",
    status_code=status.HTTP_200_OK,
    responses={status.HTTP_200_OK: {"model": SProducer}},
)
async def get_me_as_producer(user: SUser = Depends(get_current_user)):
    producer_profile = await ProducerDAO.find_one_or_none(user=user)
    # lazy load error
    return producer_profile


@auth.get(
    path="/users/producers",
    response_model=List[SProducer],
    summary="Get all producers",
    status_code=status.HTTP_200_OK,
    responses={status.HTTP_200_OK: {"model": List[SProducer]}},
)
async def get_all_producers() -> List[SProducer]:
    response = await ProducerDAO.find_all()
    # lazy load error
    return response


@auth.get(
    path="/users/producers/{producer_id}",
    response_model=SProducer,
    summary="Get one producer by id",
    status_code=status.HTTP_200_OK,
    responses={status.HTTP_200_OK: {"model": SProducer}},
)
async def get_one_producer(producer_id: int) -> SProducer:
    response = await ProducerDAO.find_one_by_id(id_=producer_id)
    # lazy load error
    return response


@auth.put(
    path="/users/producers/{producer_id}",
    response_model=SUser,
    summary="Update producer by id",
    status_code=status.HTTP_200_OK,
    responses={status.HTTP_200_OK: {"model": SUser}},
)
async def update_one_producer(
    producer_id: int, data: SArtistUpdate, user: SUser = Depends(get_current_user)
) -> SUser:
    if not user:
        raise NotFoundException()

    if user.id != producer_id:
        raise NoRightsException()

    update_data = {}

    if data.description:
        update_data["description"] = data.description

    await UsersDAO.edit_one(producer_id, update_data)
    # lazy load error
    return SUser(**update_data)


@auth.post(
    path="/users/producers/{producer_id}",
    summary="Deactivate artist profile by id",
    response_model=SProducerDeleteResponse,
    responses={status.HTTP_200_OK: {"model": SProducerDeleteResponse}},
)
async def deactivate_one_producer(
    producer_id: int, user: SUser = Depends(get_current_user)
) -> SProducerDeleteResponse:
    if not user:
        raise NotFoundException()

    if user.id != producer_id:
        raise NoRightsException()

    await ArtistDAO.edit_one(producer_id, {"is_available": False})
    return SProducerDeleteResponse


"""
Auth routes
"""


@auth.post(
    path="/register",
    summary="Create new user",
    response_model=SAuthUserRegisterResponse,
    responses={status.HTTP_201_CREATED: {"model": SAuthUserRegisterResponse}},
)
async def register(user: SRegisterUser) -> SAuthUserRegisterResponse:
    existing_user = await UsersDAO.find_one_or_none(email=user.email)
    if existing_user:
        raise HTTPException(status_code=403)

    role_superuser = await RoleDAO.find_one_by_id(id_=1)

    if not role_superuser:
        pass
        # role_superuser = await RoleDAO.add_one({"name": "superuser"})
        # role_moder = await RoleDAO.add_one({"name": "moder"})
        # role_producer = await RoleDAO.add_one({"name": "producer"})
        # role_artist = await RoleDAO.add_one({"name": "artist"})
        # role_listener = await RoleDAO.add_one({"name": "listener"})

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

    user = await UsersDAO.add_one(
        {
            "username": user.username,
            "email": user.email,
            "password": hashed_password,
            "birthday": user.birthday,
        }
    )

    for tag in user_roles:
        await ListenerTagsDAO.add_one({"user_id": user.id, "tag_id": tag.id})

    for role in user_roles:
        await UserToRoleDAO.add_one({"user_id": user.id, "role_id": role.id})

    artist_profile_id = await ArtistDAO.add_one({"description": "Hi, I'm an artist"})
    await UsersDAO.edit_one(user.id, {"artist_profile_id": artist_profile_id})
    await ProducerDAO.edit_one(artist_profile_id, {"is_available": False})

    producer_profile_id = await ProducerDAO.add_one(
        {"description": "Hi, I'm a producer"}
    )
    await UsersDAO.edit_one(user.id, {"producer_profile_id": producer_profile_id})
    await ArtistDAO.edit_one(user.id, {"is_available": False})

    return SAuthUserRegisterResponse


@auth.post(
    path="/login",
    summary="Signin",
    response_model=SUserLoginResponse,
    responses={status.HTTP_200_OK: {"model": SUserLoginResponse}},
)
async def login(user: SLoginUser, response: Response) -> SUserLoginResponse:
    auth_user = await authenticate_user(email=user.email, password=user.password)
    print(auth_user)
    if not auth_user:
        raise HTTPException(status_code=401)

    access_token = create_access_token({"sub": str(auth_user.id)})
    refresh_token = create_refresh_token({"sub": str(auth_user.id)})

    response.set_cookie(
        key="refreshToken", value=refresh_token, httponly=True, samesite="Strict"
    )

    return SUserLoginResponse.from_db_model(
        user=auth_user, access_token=access_token, refresh_token=refresh_token
    )


@auth.post(
    path="/refresh",
    response_model=SRefreshTokenResponse,
    summary="Refresh auth token",
    status_code=status.HTTP_200_OK,
    responses={status.HTTP_200_OK: {"model": SRefreshTokenResponse}},
)
async def refresh(user: SUser = Depends(get_current_user)) -> SRefreshTokenResponse:
    if not user:
        HTTPException(status_code=401, detail="refresh token is not valid")

    access_token = create_access_token({"sub": str(user.id)})
    refresh_token = create_refresh_token({"sub": str(user.id)})

    return SRefreshTokenResponse(accessToken=access_token, refreshToken=refresh_token)

    return SRefreshTokenResponse(
        accessToken=access_token,
        refreshToken=refresh_token
    )

@auth.post(path="/callback", response_model=SSpotifyCallbackResponse)
async def spotify_callback(code, response: Response) -> SSpotifyCallbackResponse:
    payload = {
        "code": code,
        "client_id": settings.spotify.CLIENT_ID,
        "client_secret": settings.spotify.CLIENT_SECRET,
        "grant_type": "authorization_code",
        "redirect_uri": "http://localhost:5173/profile",
    }

    auth_response = requests.post(
        "https://accounts.spotify.com/api/token",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data=payload,
    )
    auth_response_data = auth_response.json()

    access_token = auth_response_data.get("access_token")
    # refresh_token = auth_response_data.get("refresh_token")

    if access_token:
        user_response = requests.get(
            "https://api.spotify.com/v1/me",
            headers={"Authorization": f"Bearer {access_token}"},
        )
        user_data = user_response.json()

        user = await UsersDAO.find_one_or_none(email=user_data.get("email"))
        if not user:
            new_user = {
                "username": user_data.get("username"),
                "email": user_data.get("email"),
                "password": None,
            }

            await UsersDAO.add_one(new_user)
            user = new_user
            access_token = create_access_token({"sub": str(user.id)})
            refresh_token = create_refresh_token({"sub": str(user.id)})
            response.set_cookie("refresh_token", refresh_token, httponly=True)

            return SSpotifyCallbackResponse.from_db_model(
                user=user, access_token=access_token, refresh_token=refresh_token
            )

        else:
            access_token = create_access_token({"sub": str(user.id)})
            refresh_token = create_refresh_token({"sub": str(user.id)})

            response.set_cookie("refresh_token", refresh_token, httponly=True)

            return SSpotifyCallbackResponse.from_db_model(
                user=user, access_token=access_token, refresh_token=refresh_token
            )

    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Failed to obtain access token",
        )
