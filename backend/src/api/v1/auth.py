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

from src.api.exceptions import NotFoundException, NoRightsException
from src.core.config import settings
from src.core.media import MediaRepository
from src.schemas.auth import (
    SRefreshTokenResponse,
    SSpotifyCallbackResponse,
    SArtistResponse,
    SProducerResponse,
    SRegisterUserResponse,
    SRegisterUserRequest,
    SLoginRequest,
    User,
    SMeResponse,
    SUsersResponse,
    SUserResponse,
    SUpdateUserPictureResponse,
    SUpdateUserRequest,
    SUpdateUserResponse,
    SDeleteUserResponse,
    SMeAsArtistResponse,
    SArtistsResponse,
    SUpdateArtistRequest,
    SUpdateArtistResponse,
    SDeleteArtistResponse,
    SProducersResponse,
    Producer,
    SMeAsProducerResponse,
    SUpdateProducerRequest,
    SUpdateProducerResponse,
    SDeleteProducerResponse,
    SLoginResponse,
)
from src.services.auth import UsersDAO, ArtistDAO, ProducerDAO, RoleDAO, UserToRoleDAO
from src.services.tags import ListenerTagsDAO, TagsDAO
from src.utils.auth import (
    authenticate_user,
    create_access_token,
    create_refresh_token,
    get_hashed_password,
    get_current_user,
)
from src.utils.files import unique_filename

auth = APIRouter(prefix="/auth", tags=["Auth & Users"])


"""
Users routes
"""


@auth.get(
    path="/users/me",
    response_model=SMeResponse,
    summary="Get details of currently logged in user",
    status_code=status.HTTP_200_OK,
    responses={status.HTTP_200_OK: {"model": SMeResponse}},
)
async def get_me(user: User = Depends(get_current_user)) -> SMeResponse:
    return SMeResponse(**user.model_dump())


@auth.get(
    path="/users",
    response_model=SUsersResponse,
    summary="Get all users",
    status_code=status.HTTP_200_OK,
    responses={status.HTTP_200_OK: {"model": SUsersResponse}},
)
async def get_users() -> SUsersResponse:
    response = await UsersDAO.find_all()
    return SUsersResponse(users=[User.from_db_model(model=user) for user in response])


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

    return SUserResponse.from_db_model(model=user)


@auth.put(
    path="/users/picture/{user_id}",
    summary="Update image info by id",
    response_model=SUpdateUserPictureResponse,
    responses={status.HTTP_200_OK: {"model": SUpdateUserPictureResponse}},
)
async def update_user_picture(
    user_id: int, file: UploadFile = File(...), user: User = Depends(get_current_user)
) -> SUpdateUserPictureResponse:

    if user.id != user_id:
        raise NoRightsException()

    filename = await unique_filename(file) if file else None
    picture_url = await MediaRepository.upload_file("PICTURES", filename, file)

    update_data = {"picture_url": picture_url}
    await UsersDAO.edit_one(user_id, update_data)
    return SUpdateUserPictureResponse()


@auth.put(
    path="/users/{user_id}",
    summary="Update user info by id",
    response_model=SUpdateUserResponse,
    responses={status.HTTP_200_OK: {"model": SUpdateUserResponse}},
)
async def update_user(
    user_id: int, data: SUpdateUserRequest, user: User = Depends(get_current_user)
) -> SUpdateUserResponse:

    if not user:
        raise NotFoundException()

    if user.id != user_id:
        raise NoRightsException()

    update_data = {}

    if data.username:
        update_data["username"] = data.username
    if data.picture_url:
        update_data["picture_url"] = data.picture_url
    if data.name:
        update_data["name"] = data.picture_url
    if data.description:
        update_data["description"] = data.description

    await UsersDAO.edit_one(user_id, update_data)
    return SUpdateUserResponse(**update_data)


@auth.delete(
    path="/users/{user_id}",
    summary="Delete user by id",
    response_model=SDeleteUserResponse,
    responses={status.HTTP_200_OK: {"model": SDeleteUserResponse}},
)
async def delete_users(
    user_id: int, user: User = Depends(get_current_user)
) -> SDeleteUserResponse:
    if not user:
        raise NotFoundException()

    if user.id != user_id:
        raise NoRightsException()

    await UsersDAO.delete(user_id)
    return SDeleteUserResponse()


"""
Artists routes
"""


@auth.get(
    path="/users/artists/me",
    summary="Get my artist profile",
    status_code=status.HTTP_200_OK,
    response_model=SMeAsArtistResponse,
    responses={status.HTTP_200_OK: {"model": SMeAsArtistResponse}},
)
async def get_me_as_artist(
    user: User = Depends(get_current_user),
) -> SMeAsArtistResponse:
    response = await ArtistDAO.find_one_or_none(user=user)
    return SMeAsArtistResponse.from_db_model(**response)


@auth.get(
    path="/users/artists",
    response_model=SArtistsResponse,
    summary="Get all artists",
    status_code=status.HTTP_200_OK,
    responses={status.HTTP_200_OK: {"model": SArtistsResponse}},
)
async def get_artists() -> SArtistsResponse:
    response = await ArtistDAO.find_all()
    return SArtistsResponse(artists=response)


@auth.get(
    path="/users/artists/{artist_id}",
    response_model=SArtistResponse,
    summary="Get one artists by id",
    status_code=status.HTTP_200_OK,
    responses={status.HTTP_200_OK: {"model": SArtistResponse}},
)
async def get_one_artist(artist_id: int) -> SArtistResponse:
    artist = await ArtistDAO.find_one_by_id(artist_id)
    if not artist:
        raise NotFoundException()
    return SArtistResponse.from_db_model(artist)


@auth.put(
    path="/users/artists/{artist_id}",
    response_model=SUpdateArtistResponse,
    summary="Update artist by id",
    status_code=status.HTTP_200_OK,
    responses={status.HTTP_200_OK: {"model": SUpdateArtistResponse}},
)
async def update_artist(
    artist_id: int, data: SUpdateArtistRequest, user: User = Depends(get_current_user)
) -> SUpdateArtistResponse:
    if not user:
        raise NotFoundException()

    if user.id != artist_id:
        raise NoRightsException()

    update_data = {}

    if data.username:
        update_data["description"] = data.username

    await UsersDAO.edit_one(artist_id, update_data)
    return SUpdateArtistResponse(**update_data)


@auth.delete(
    path="/users/artists/{artist_id}",
    summary="Deactivate artist profile by id",
    response_model=SDeleteArtistResponse,
    responses={status.HTTP_200_OK: {"model": SDeleteArtistResponse}},
)
async def deactivate_artists(artist_id: int, user: User = Depends(get_current_user)):
    if not user:
        raise NotFoundException()

    if user.id != artist_id:
        raise NoRightsException()

    await ArtistDAO.delete(artist_id)
    return SDeleteArtistResponse()


"""
Producers routes
"""


@auth.get(
    path="/users/producers/me",
    summary="Get my producer profile",
    status_code=status.HTTP_200_OK,
    response_model=SMeAsProducerResponse,
    responses={status.HTTP_200_OK: {"model": SMeAsProducerResponse}},
)
async def get_me_as_producer(
    user: User = Depends(get_current_user),
) -> SMeAsProducerResponse:
    producer_profile = await ProducerDAO.find_one_or_none(user=user)
    # lazy load error
    return SMeAsProducerResponse.from_db_model(producer_profile)


@auth.get(
    path="/users/producers",
    summary="Get all producers",
    status_code=status.HTTP_200_OK,
    response_model=SProducersResponse,
    responses={status.HTTP_200_OK: {"model": SProducersResponse}},
)
async def get_all_producers() -> SProducersResponse:
    response = await ProducerDAO.find_all()
    # lazy load error

    producers = list(map(lambda producer: Producer.from_db_model(producer), response))
    return SProducersResponse(producers=producers)


@auth.get(
    path="/users/producers/{producer_id}",
    response_model=SProducerResponse,
    summary="Get one producer by id",
    status_code=status.HTTP_200_OK,
    responses={status.HTTP_200_OK: {"model": SProducerResponse}},
)
async def get_one_producer(producer_id: int) -> SProducerResponse:
    response = await ProducerDAO.find_one_by_id(id_=producer_id)
    # lazy load error
    return SProducerResponse.from_db_model(response)


@auth.put(
    path="/users/producers/{producer_id}",
    response_model=SUpdateProducerResponse,
    summary="Update producer by id",
    status_code=status.HTTP_200_OK,
    responses={status.HTTP_200_OK: {"model": SUpdateProducerResponse}},
)
async def update_one_producer(
    producer_id: int,
    data: SUpdateProducerRequest,
    user: User = Depends(get_current_user),
) -> SUpdateProducerResponse:

    if not user:
        raise NotFoundException()

    if user.id != producer_id:
        raise NoRightsException()

    update_data = {}

    if data.description:
        update_data["description"] = data.description

    await UsersDAO.edit_one(producer_id, update_data)
    # lazy load error
    return SUpdateProducerResponse(**update_data)


@auth.post(
    path="/users/producers/{producer_id}",
    summary="Deactivate artist profile by id",
    response_model=SDeleteProducerResponse,
    responses={status.HTTP_200_OK: {"model": SDeleteProducerResponse}},
)
async def deactivate_one_producer(
    producer_id: int, user: User = Depends(get_current_user)
) -> SDeleteProducerResponse:
    if not user:
        raise NotFoundException()

    if user.id != producer_id:
        raise NoRightsException()

    await ArtistDAO.edit_one(producer_id, {"is_available": False})
    return SDeleteProducerResponse()


"""
Auth routes
"""


@auth.post(
    path="/register",
    summary="Create new user",
    response_model=SRegisterUserResponse,
    responses={status.HTTP_201_CREATED: {"model": SRegisterUserResponse}},
)
async def register(user: SRegisterUserRequest) -> SRegisterUserResponse:
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

    return SRegisterUserResponse()


@auth.post(
    path="/login",
    summary="Signin",
    response_model=SLoginResponse,
    responses={status.HTTP_200_OK: {"model": SLoginResponse}},
)
async def login(user: SLoginRequest, response: Response) -> SLoginResponse:
    auth_user = await authenticate_user(email=user.email, password=user.password)

    if not auth_user:
        raise HTTPException(status_code=401)

    access_token = create_access_token({"sub": str(auth_user.id)})
    refresh_token_ = create_refresh_token({"sub": str(auth_user.id)})

    response.set_cookie(
        key="refreshToken", value=refresh_token_, httponly=True, samesite="strict"
    )

    return SLoginResponse(
        user=auth_user, accessToken=access_token, refreshToken=refresh_token_
    )


@auth.post(
    path="/refresh",
    response_model=SRefreshTokenResponse,
    summary="Refresh auth token",
    status_code=status.HTTP_200_OK,
    responses={status.HTTP_200_OK: {"model": SRefreshTokenResponse}},
)
async def refresh_token(
    user: User = Depends(get_current_user),
) -> SRefreshTokenResponse:
    if not user:
        HTTPException(status_code=401, detail="refresh token is not valid")

    access_token = create_access_token({"sub": str(user.id)})
    refresh_token_ = create_refresh_token({"sub": str(user.id)})

    return SRefreshTokenResponse(accessToken=access_token, refreshToken=refresh_token_)


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
        url="https://accounts.spotify.com/api/token",
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
                "id": user_data["id"],
                "username": user_data.get("username"),
                "email": user_data.get("email"),
                "password": None,
            }

            await UsersDAO.add_one(new_user)
            user = new_user
            access_token = create_access_token({"sub": str(user["id"])})
            refresh_token_ = create_refresh_token({"sub": str(user["id"])})
            response.set_cookie("refresh_token", refresh_token_, httponly=True)

            return SSpotifyCallbackResponse.from_db_model(
                user=user, access_token=access_token, refresh_token=refresh_token_
            )

        else:
            access_token = create_access_token({"sub": str(user.id)})
            refresh_token_ = create_refresh_token({"sub": str(user.id)})

            response.set_cookie("refresh_token", refresh_token_, httponly=True)

            return SSpotifyCallbackResponse.from_db_model(
                user=user, access_token=access_token, refresh_token=refresh_token_
            )

    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Failed to obtain access token",
        )
