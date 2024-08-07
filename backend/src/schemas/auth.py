from datetime import date, datetime
from typing import Optional, List

from pydantic import BaseModel, EmailStr, Field

from src.enums.auth import Role
from src.models.auth import User as _User
from src.schemas.base import FromDBModelMixin, DetailMixin
from src.schemas.tags import Tag


class User(BaseModel, FromDBModelMixin):
    id: int
    username: str
    email: str
    password: str
    picture_url: str
    birthday: datetime

    _model_type = _User


class SUserResponse(User, FromDBModelMixin):
    pass


class SMeResponse(SUserResponse):
    pass


class SUsersResponse(BaseModel):
    users: List[User]


class SUpdateUserPictureResponse(BaseModel, DetailMixin):
    detail = 'User picture updated.'


class SUpdateUserRequest(BaseModel):
    name: Optional[str]
    username: Optional[str]
    picture_url: Optional[str]
    description: Optional[str]


class SUpdateUserResponse(BaseModel):
    name: str
    username: str
    picture_url: str
    description: str


class SDeleteUserResponse(BaseModel, DetailMixin):
    detail = 'User deleted.'


class Artist(BaseModel, FromDBModelMixin):
    user: User
    description: Optional[str] = "Description not found"


class SArtistResponse(Artist):
    pass


class SMeAsArtistResponse(SMeResponse):
    pass


class SArtistsResponse(BaseModel):
    artists: List[Artist]


class SUpdateArtistRequest(BaseModel):
    description: Optional[str] = Field(max_length=255)


class SUpdateArtistResponse(BaseModel):
    description: str = Field(max_length=255)


class SDeleteArtistResponse(BaseModel, DetailMixin):
    detail = 'Artist deleted.'


class Producer(BaseModel, FromDBModelMixin):
    user: User
    description: Optional[str] = "Description not found"


class SProducerResponse(Producer):
    pass


class SMeAsProducerResponse(SProducerResponse):
    pass


class SProducersResponse(BaseModel):
    producers: List[Producer]


class SUpdateProducerRequest(BaseModel):
    description: Optional[str] = Field(max_length=255)


class SUpdateProducerResponse(BaseModel):
    description: str


class SDeleteProducerResponse(BaseModel, DetailMixin):
    detail = 'Producer deleted.'


class SRegisterUserRequest(BaseModel):
    username: str = Field(min_length=3, max_length=25)
    password: str = Field(min_length=5)
    email: EmailStr
    roles: List[Role]
    birthday: Optional[date]
    tags: Optional[List[str]]


class SRegisterUserResponse(BaseModel, DetailMixin):
    detail = 'User created.'


class SLoginRequest(BaseModel):
    email: EmailStr
    password: str


class SLoginResponse(BaseModel):
    accessToken: str
    refreshToken: str
    user: User


class SRefreshTokenResponse(BaseModel):
    accessToken: str
    refreshToken: str


class SSpotifyCallbackResponse(BaseModel):
    access_token: str
    refresh_token: str
    user: User
