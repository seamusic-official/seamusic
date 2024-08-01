from datetime import date, datetime
from enum import Enum
from typing import Optional, List

from pydantic import BaseModel, EmailStr, Field

from src.models.auth import User
from src.schemas.tags import STag


class Role(str, Enum):
    superuser = "superuser"
    moder = "moder"
    artist = "artist"
    producer = "producer"
    listener = "listener"


"""
User (Listener) schemas
"""


class SUserBase(BaseModel):
    username: str = Field(min_length=5, max_length=25)
    email: EmailStr
    picture_url: Optional[str]
    birthday: Optional[date]
    roles: Optional[List[Role]] = None


class SUser(SUserBase):
    id: int
    created_at: datetime
    updated_at: datetime


class SUserEditImageResponse(BaseModel):
    response: str = "User image edited"


class SUserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    picture_url: str
    birthday: Optional[date]

    @classmethod
    def from_db_model(cls, user: User) -> "SUserResponse":
        return cls(
            id=user.id,
            username=user.username,
            email=user.email,
            picture_url=user.picture_url,
            birthday=user.birthday,
        )


class SUserUpdate(BaseModel):
    username: Optional[str] = Field(min_length=5, max_length=25)
    email: Optional[EmailStr]
    picture_url: Optional[str]
    tags: Optional[List[STag]]
    roles: Optional[List[Role]]


class SUserUpdateResponse(BaseModel):
    username: str
    email: EmailStr
    picture_url: str


class SUserDeleteResponse(BaseModel):
    response: str = "User deleted"


"""
Artist schemas
"""


class SArtistBase(BaseModel):
    user: SUser
    description: Optional[str]
    tags: Optional[List[STag]]


class SArtist(SArtistBase):
    id: int
    created_at: datetime
    updated_at: datetime


class SArtistUpdate(BaseModel):
    description: Optional[str] = Field(max_length=255)


class SArtistDeleteResponse(BaseModel):
    response: str = "Artist deleted"


"""
Producer schemas
"""


class SProducerBase(BaseModel):
    user: SUser
    description: Optional[str]
    tags: Optional[List[STag]]


class SProducer(SProducerBase):
    id: int
    created_at: datetime
    updated_at: datetime


class SProducerDeleteResponse(BaseModel):
    response: str = "Producer deleted"


class SProducerUpdate(BaseModel):
    description: Optional[str] = Field(max_length=255)


"""
Auth schemas
"""


class SRegisterUser(BaseModel):
    username: str = Field(min_length=3, max_length=25)
    password: str = Field(min_length=5)
    email: EmailStr
    roles: List[Role]
    birthday: Optional[date]
    tags: Optional[List[str]]


class SAuthUserRegisterResponse(BaseModel):
    response: str = "User created"


class SLoginUser(BaseModel):
    email: EmailStr
    password: str


class SUserLoginResponse(BaseModel):
    accessToken: str
    refreshToken: str
    user: SUserResponse

    @classmethod
    def from_db_model(
        cls, user: User, access_token: str, refresh_token: str
    ) -> "SUserLoginResponse":
        return cls(
            accessToken=access_token,
            refreshToken=refresh_token,
            user=SUserResponse.from_db_model(user=user),
        )


class SSpotifyCallbackResponse(BaseModel):
    access_token: str
    refresh_token: str
    user: SUserResponse

    @classmethod
    def from_db_model(cls, user: User, refresh_token: str, access_token: str):
        return cls(
            access_token=access_token,
            refresh_token=refresh_token,
            user=SUserResponse.from_db_model(user=user),
        )


class SRefreshTokenResponse(BaseModel):
    accessToken: str
    refreshToken: str
