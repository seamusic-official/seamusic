from datetime import date, datetime
from typing import Optional, List

from pydantic import BaseModel, EmailStr, Field

from src.models.auth import User as _User
from src.enums.auth import Role
from src.schemas.base import BaseResponse, FromDBModelMixin
from src.schemas.tags import Tag


class User(FromDBModelMixin):
    id: int
    username: str
    email: str
    password: str
    picture_url: str
    birthday: datetime

    _model_type = _User


class SUserRequest(BaseModel):
    username: str
    email: str
    password: str
    picture_url: str
    birthday: datetime
    roles: List[Role]
    tags: List[Tag]


class SAllUserResponse(BaseModel):
    users: List[User]


class SUserResponse(BaseResponse, User, BaseModel):
    pass


class SUserUpdateRequest(BaseModel):
    name: Optional[str]
    picture_url: Optional[str]
    description: Optional[str]
    co_prod: Optional[str]


class SUserDeleteResponse(BaseResponse):
    message: str = "User was deactivated."


class SRegisterUserRequest(BaseModel):
    username: str = Field(min_length=3, max_length=25)
    password: str = Field(min_length=5)
    email: EmailStr
    roles: List[Role]
    birthday: Optional[date]
    tags: Optional[List[str]]


class SRegisterUserResponse(BaseModel):
    response: str = "User created"


class SLoginUserRequest(BaseModel):
    email: EmailStr
    password: str


class SSpotifyCallbackResponse(BaseResponse):
    access_token: str
    refresh_token: str
    user: SUserResponse


class SRefreshTokenResponse(BaseModel):
    accessToken: str
    refreshToken: str


class SUserLoginResponse(BaseResponse):
    accessToken: str
    refreshToken: str
    user: SUserResponse


class Artist(BaseModel):
    user: User
    description: Optional[str] = "Description not found"


class SArtistDetail(BaseModel):
    user: User
    description: str


class SArtistResponse(BaseModel):
    artist_profiles: List[Artist]


class SArtistUpdate(BaseModel):
    description: Optional[str] = Field(max_length=255)


class SArtistDelete(BaseModel):
    response: str = "Artist deleted"


class Producer(BaseModel):
    user: User
    description: Optional[str] = "Description not found"


class SProducerDetail(BaseModel):
    user: User
    description: str


class SProducerResponse(BaseModel):
    artist_profiles: List[Artist]


class SProducerUpdateRequest(BaseModel):
    description: Optional[str] = Field(max_length=255)


class SProducerDeleteResponse(BaseResponse):
    message: str = "Producer deleted"
