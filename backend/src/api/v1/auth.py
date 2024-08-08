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
from src.services import auth as services
from src.exceptions.api import NotFoundException, NoRightsException
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
from src.repositories.auth import UsersDAO, ArtistDAO, ProducerDAO, RoleDAO, UserToRoleDAO
from src.repositories.tags import ListenerTagsDAO, TagsDAO
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
    users = await services.get_all_users()
    return SUsersResponse(users=[User.from_db_model(model=user) for user in users])


@auth.get(
    path="/users/{user_id}",
    response_model=SUserResponse,
    summary="Get a user by ID",
    status_code=status.HTTP_200_OK,
    responses={status.HTTP_200_OK: {"model": SUserResponse}},
)
async def get_one(user_id: int) -> SUserResponse:
    user = await services.get_user_by_id(user_id=user_id)

    return SUserResponse.from_db_model(model=user)


@auth.put(
    path="/users/picture/{user_id}",
    summary="Update image info by id",
    response_model=SUpdateUserPictureResponse,
    responses={status.HTTP_200_OK: {"model": SUpdateUserPictureResponse}},
)
async def update_user_picture(
        file: UploadFile = File(...),
        user: User = Depends(get_current_user)
) -> SUpdateUserPictureResponse:
    await services.update_current_user_picture(user_id=user.id, file=file)

    return SUpdateUserPictureResponse()


@auth.put(
    path="/users/{user_id}",
    summary="Update user info by id",
    response_model=SUpdateUserResponse,
    responses={status.HTTP_200_OK: {"model": SUpdateUserResponse}},
)
async def update_user(
    data: SUpdateUserRequest,
    user: User = Depends(get_current_user)
) -> SUpdateUserResponse:
    update_data = await services.update_current_user(user_id=user.id, data=data)
    return SUpdateUserResponse(**update_data)


@auth.delete(
    path="/users/{user_id}",
    summary="Delete user by id",
    response_model=SDeleteUserResponse,
    responses={status.HTTP_200_OK: {"model": SDeleteUserResponse}},
)
async def delete_users(
    user: User = Depends(get_current_user)
) -> SDeleteUserResponse:
    await services.delete_current_user(user_id=user.id)

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
    artist = await services.get_artist_by_id(artist_id=user.id)

    return SMeAsArtistResponse.from_db_model(artist)


@auth.get(
    path="/users/artists",
    response_model=SArtistsResponse,
    summary="Get all artists",
    status_code=status.HTTP_200_OK,
    responses={status.HTTP_200_OK: {"model": SArtistsResponse}},
)
async def get_artists() -> SArtistsResponse:
    artists = await services.get_all_artists()
    return SArtistsResponse(artists=artists)


@auth.get(
    path="/users/artists/{artist_id}",
    response_model=SArtistResponse,
    summary="Get one artists by id",
    status_code=status.HTTP_200_OK,
    responses={status.HTTP_200_OK: {"model": SArtistResponse}},
)
async def get_one_artist(artist_id: int) -> SArtistResponse:
    artist = await services.get_artist_by_id(artist_id=artist_id)
    return SArtistResponse.from_db_model(artist)


@auth.put(
    path="/users/artists/{artist_id}",
    response_model=SUpdateArtistResponse,
    summary="Update artist by id",
    status_code=status.HTTP_200_OK,
    responses={status.HTTP_200_OK: {"model": SUpdateArtistResponse}},
)
async def update_artist(
    data: SUpdateArtistRequest,
    user: User = Depends(get_current_user)
) -> SUpdateArtistResponse:
    await services.update_current_artist(artist_id=user.id, description=data.description)

    return SUpdateArtistResponse()


@auth.delete(
    path="/users/artists/{artist_id}",
    summary="Deactivate artist profile by id",
    response_model=SDeleteArtistResponse,
    responses={status.HTTP_200_OK: {"model": SDeleteArtistResponse}},
)
async def deactivate_artists(user: User = Depends(get_current_user)):
    await services.deactivate_artist(artist_id=user.id)

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
    producer_profile = await services.get_producer_by_id(producer_id=user.id)

    return SMeAsProducerResponse.from_db_model(producer_profile)


@auth.get(
    path="/users/producers",
    summary="Get all producers",
    status_code=status.HTTP_200_OK,
    response_model=SProducersResponse,
    responses={status.HTTP_200_OK: {"model": SProducersResponse}},
)
async def get_all_producers() -> SProducersResponse:
    response = await services.get_all_producers()
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
    response = await services.get_producer_by_id(producer_id=producer_id)

    return SProducerResponse.from_db_model(response)


@auth.put(
    path="/users/producers/{producer_id}",
    response_model=SUpdateProducerResponse,
    summary="Update producer by id",
    status_code=status.HTTP_200_OK,
    responses={status.HTTP_200_OK: {"model": SUpdateProducerResponse}},
)
async def update_one_producer(
    data: SUpdateProducerRequest,
    user: User = Depends(get_current_user),
) -> SUpdateProducerResponse:
    await services.update_one_producer(producer_id=user.id, description=data.description)

    return SUpdateProducerResponse()


@auth.post(
    path="/users/producers/{producer_id}",
    summary="Deactivate artist profile by id",
    response_model=SDeleteProducerResponse,
    responses={status.HTTP_200_OK: {"model": SDeleteProducerResponse}},
)
async def deactivate_one_producer(
    user: User = Depends(get_current_user)
) -> SDeleteProducerResponse:
    await services.deactivate_one_producer(producer_id=user.id)

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
    await services.create_new_user(
        username=user.username,
        password=user.password,
        email=user.email,
        roles=user.roles,
        birthday=user.birthday,
        tags=user.tags
    )

    return SRegisterUserResponse()


@auth.post(
    path="/login",
    summary="Signin",
    response_model=SLoginResponse,
    responses={status.HTTP_200_OK: {"model": SLoginResponse}},
)
async def login(user: SLoginRequest, response: Response) -> SLoginResponse:
    return await services.login(
        email=user.email,
        password=user.password,
        response=response
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
    return await services.refresh_token(user_id=user.id)


@auth.post(path="/callback", response_model=SSpotifyCallbackResponse)
async def spotify_callback(code, response: Response) -> SSpotifyCallbackResponse:
    await services.spotify_callback(
        code=code,
        response=response
    )