from dataclasses import dataclass

from sqlalchemy import select

from src.converters.repositories.database.sqlalchemy import request_dto_to_model, models_to_dto
from src.dtos.database.tags import AddTagRequestDTO, TagsResponseDTO, Tag as _Tag
from src.models.auth import User, ArtistProfile, ProducerProfile
from src.models.tags import Tag
from src.repositories.database.base import SQLAlchemyRepository
from src.repositories.database.tags.base import BaseTagsRepository


@dataclass
class TagsRepository(SQLAlchemyRepository, BaseTagsRepository):
    async def add_tag(self, tag: AddTagRequestDTO) -> None:
        tag = request_dto_to_model(model=Tag, request_dto=tag)
        self.session.add(tag)

    async def get_listener_tags(self, user_id: int) -> TagsResponseDTO:
        query = select(User).filter_by(id=user_id).column(column='tags')
        tags = list(await self.session.scalars(query))
        return TagsResponseDTO(tags=models_to_dto(models=tags, dto=_Tag))

    async def get_producer_tags(self, producer_id: int) -> TagsResponseDTO:
        query = select(ProducerProfile).filter_by(id=producer_id).column(column='tags')
        tags = list(await self.session.scalars(query))
        return TagsResponseDTO(tags=models_to_dto(models=tags, dto=_Tag))

    async def get_artist_tags(self, artist_id: int) -> TagsResponseDTO:
        query = select(ArtistProfile).filter_by(id=artist_id).column(column='tags')
        tags = list(await self.session.scalars(query))
        return TagsResponseDTO(tags=models_to_dto(models=tags, dto=_Tag))
