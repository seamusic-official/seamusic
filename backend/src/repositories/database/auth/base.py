from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.dtos.database.auth import (
    UserResponseDTO,
    UsersResponseDTO,
    UpdateUserRequestDTO,
    ArtistResponseDTO,
    ArtistsResponseDTO,
    UpdateArtistRequestDTO,
    ProducerResponseDTO,
    ProducersResponseDTO,
    UpdateProducerRequestDTO,
    CreateUserRequestDTO,
)


@dataclass
class BaseUsersRepository(ABC):
    @abstractmethod
    async def get_user_by_id(self, user_id: int) -> UserResponseDTO | None:
        ...

    @abstractmethod
    async def get_users(self) -> UsersResponseDTO:
        ...

    @abstractmethod
    async def create_user(self, user: CreateUserRequestDTO) -> None:
        ...

    @abstractmethod
    async def update_user(self, user: UpdateUserRequestDTO) -> None:
        ...

    @abstractmethod
    async def delete_user(self, user_id: int) -> None:
        ...


@dataclass
class BaseArtistsRepository(ABC):
    @abstractmethod
    async def get_artist_by_id(self, artist_id: int) -> ArtistResponseDTO | None:
        ...

    @abstractmethod
    async def get_artists(self) -> ArtistsResponseDTO:
        ...

    @abstractmethod
    async def update_artist(self, artist: UpdateArtistRequestDTO):
        ...


@dataclass
class BaseProducersRepository(ABC):
    @abstractmethod
    async def get_producer_by_id(self, producer_id: int) -> ProducerResponseDTO | None:
        ...

    @abstractmethod
    async def get_producers(self) -> ProducersResponseDTO:
        ...

    @abstractmethod
    async def update_producer(self, producer: UpdateProducerRequestDTO) -> None:
        ...