from datetime import datetime, date

from pydantic import EmailStr, Field

from src.dtos.database.base import BaseRequestDTO, BaseResponseDTO, BaseDTO
from src.enums.auth import Role, AccessLevel


class User(BaseDTO):
    id: int
    username: str
    email: EmailStr
    password: str
    picture_url: str
    roles: list[Role]
    birthday: datetime


class UserResponseDTO(BaseResponseDTO):
    id: int
    username: str
    email: EmailStr
    password: str
    picture_url: str
    roles: list[Role]
    birthday: datetime


class UsersResponseDTO(BaseResponseDTO):
    users: list[User]


class CreateUserRequestDTO(BaseRequestDTO):
    username: str
    email: EmailStr
    password: str | None
    picture_url: str | None = None
    roles: list[Role]
    birthday: date
    tags: list[str]
    access_level: AccessLevel


class UpdateUserRequestDTO(BaseRequestDTO):
    username: str | None = None
    picture_url: str | None = None
    description: str | None = None
    artist_profile_id: int | None = None
    producer_profile_id: int | None = None


class Artist(BaseDTO):
    user: User
    description: str | None = None


class ArtistResponseDTO(BaseResponseDTO):
    user: User
    description: str | None = None


class ArtistsResponseDTO(BaseResponseDTO):
    artists: list[Artist]


class CreateArtistRequestDTO(BaseRequestDTO):
    user: User
    description: str | None = Field(max_length=255)


class UpdateArtistRequestDTO(BaseRequestDTO):
    description: str | None = Field(max_length=255)
    is_available: bool | None = None


class Producer(BaseDTO):
    user: User
    description: str | None = None


class ProducerResponseDTO(BaseResponseDTO):
    user: User
    description: str | None = None


class ProducersResponseDTO(BaseResponseDTO):
    producers: list[Producer]


class CreateProducerRequestDTO(BaseRequestDTO):
    user: User
    description: str | None = Field(max_length=255)


class UpdateProducerRequestDTO(BaseRequestDTO):
    description: str | None = Field(max_length=255)
    is_available: bool | None = None
