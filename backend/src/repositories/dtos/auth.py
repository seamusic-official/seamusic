from datetime import datetime

from pydantic import EmailStr, Field

from src.enums.auth import Role
from src.repositories.dtos.base import BaseRequestDTO, BaseResponseDTO, BaseDTO


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
    password: str
    picture_url: str


class UpdateUserRequestDTO(BaseRequestDTO):
    name: str | None = None
    username: str | None = None
    picture_url: str | None = None
    description: str | None = None


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
