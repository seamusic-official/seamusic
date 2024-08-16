from dataclasses import dataclass

from sqlalchemy import select, delete

from src.converters.repositories.database.sqlalchemy import model_to_response_dto, models_to_dto, request_dto_to_model
from src.dtos.database.auth import (
    User as _User,
    UserResponseDTO,
    UsersResponseDTO,
    UpdateUserRequestDTO,
    ArtistResponseDTO,
    ArtistsResponseDTO,
    UpdateArtistRequestDTO,
    ProducerResponseDTO,
    ProducersResponseDTO,
    UpdateProducerRequestDTO,
    CreateUserRequestDTO, Artist, Producer,
)
from src.models.auth import User, ArtistProfile, ProducerProfile
from src.repositories.database.auth.base import BaseUsersRepository, BaseArtistsRepository, BaseProducersRepository
from src.repositories.database.base import SQLAlchemyRepository


@dataclass
class UsersRepository(BaseUsersRepository, SQLAlchemyRepository):
    async def get_user_by_id(self, user_id: int) -> UserResponseDTO | None:
        user = await self.session.get(User, user_id)
        return model_to_response_dto(model=user, response_dto=UserResponseDTO)

    async def get_users(self) -> UsersResponseDTO:
        query = select(User)
        users = list(await self.session.scalars(query))
        return UsersResponseDTO(users=models_to_dto(models=users, dto=_User))

    async def create_user(self, user: CreateUserRequestDTO) -> None:
        user = request_dto_to_model(request_dto=user, model=User)
        self.session.add(user)

    async def update_user(self, user: UpdateUserRequestDTO) -> None:
        user = request_dto_to_model(request_dto=user, model=User)
        await self.session.merge(user)

    async def delete_user(self, user_id: int) -> None:
        query = delete(User).filter_by(id=user_id)
        await self.session.execute(query)


@dataclass
class ArtistsRepository(BaseArtistsRepository, SQLAlchemyRepository):
    async def get_artist_by_id(self, artist_id: int) -> ArtistResponseDTO | None:
        artist_id = await self.session.get(ArtistProfile, artist_id)
        return model_to_response_dto(model=artist_id, response_dto=ArtistResponseDTO)

    async def get_artists(self) -> ArtistsResponseDTO:
        query = select(ArtistProfile)
        artists = list(await self.session.scalars(query))
        return ArtistsResponseDTO(users=models_to_dto(models=artists, dto=Artist))

    async def update_artist(self, artist: UpdateArtistRequestDTO):
        artist = request_dto_to_model(request_dto=artist, model=ArtistProfile)
        await self.session.merge(artist)


@dataclass
class ProducersRepository(BaseProducersRepository, SQLAlchemyRepository):
    async def get_producer_by_id(self, producer_id: int) -> ProducerResponseDTO | None:
        producer_id = await self.session.get(ProducerProfile, producer_id)
        return model_to_response_dto(model=producer_id, response_dto=ProducerResponseDTO)

    async def get_producers(self) -> ProducersResponseDTO:
        query = select(ProducerProfile)
        producers = list(await self.session.scalars(query))
        return ProducersResponseDTO(users=models_to_dto(models=producers, dto=Producer))

    async def update_producer(self, producer: UpdateProducerRequestDTO) -> None:
        producer = request_dto_to_model(request_dto=producer, model=ProducerProfile)
        await self.session.merge(producer)