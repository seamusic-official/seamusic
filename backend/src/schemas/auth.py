from datetime import date, datetime
from typing import Optional, List

from pydantic import BaseModel, EmailStr, Field

from src.enums.auth import Role
from src.schemas.base import BaseResponse, SBaseSchema
from src.schemas.tags import Tag


class User(SBaseSchema):
    username: str
    email: str
    password: str
    picture_url: str
    birthday: datetime


class SUserRequest(BaseModel):
    username: str
    email: str
    password: str
    picture_url: str
    birthday: datetime
    roles: List[Role]
    tags: List[Tag]


class SUserResponse(SBaseSchema):
    users: List[User]


class SUserDetail(SBaseSchema):
    username: str
    email: str
    password: str
    picture_url: str
    birthday: datetime


class SUserUpdate(SBaseSchema):
    name: Optional[str]
    picture_url: Optional[str]
    description: Optional[str]
    co_prod: Optional[str]


class SUserDeleteResponse(BaseResponse):
    message = "User was deactivated."


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


class Artist(SBaseSchema):
    user: User
    description: Optional[str] = "Description not found"


class SArtistDetail(SBaseSchema):
    user: User
    description: str


class SArtistResponse(SBaseSchema):
    artist_profiles: List[Artist]


class SArtistUpdate(BaseModel):
    description: Optional[str] = Field(max_length=255)


class SArtistDelete(BaseModel):
    response: str = "Artist deleted"


class Producer(SBaseSchema):
    user: User
    description: Optional[str] = "Description not found"


class SProducerDetail(SBaseSchema):
    user: User
    description: str


class SProducerResponse(SBaseSchema):
    artist_profiles: List[Artist]


class SProducerUpdateRequest(BaseModel):
    description: Optional[str] = Field(max_length=255)


class SProducerDeleteResponse(BaseResponse):
    message = "Producer deleted"
