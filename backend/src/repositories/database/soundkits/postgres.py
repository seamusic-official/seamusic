from dataclasses import dataclass

from sqlalchemy import select, delete

from src.models.soundkits import Soundkit
from src.repositories.converters.sqlalchemy import request_dto_to_model, model_to_response_dto, models_to_dto
from src.repositories.database.base import SQLAlchemyRepository
from src.repositories.database.soundkits.base import BaseSoundkitsRepository
from src.repositories.dtos.soundkits import (
    Soundkit as _Soundkit,
    SoundkitsResponseDTO,
    SoundkitResponseDTO,
    CreateSoundkitRequestDTO,
    UpdateSoundkitRequestDTO
)


@dataclass
class SounkitsReporitory(SQLAlchemyRepository, BaseSoundkitsRepository):
    async def get_user_soundkits(self, user_id: int) -> SoundkitsResponseDTO:
        query = select(Soundkit).filter_by(user_id=user_id)
        soundkits = list(await self.session.scalars(query))
        return SoundkitsResponseDTO(soundkits=models_to_dto(models=soundkits, dto=_Soundkit))

    async def get_all_soundkits(self) -> SoundkitsResponseDTO:
        query = select(Soundkit)
        soundkits = list(await self.session.scalars(query))
        return SoundkitsResponseDTO(soundkits=models_to_dto(models=soundkits, dto=_Soundkit))

    async def get_soundkit_by_id(self, soundkit_id: int) -> SoundkitResponseDTO | None:
        soundkit = await self.session.get(Soundkit, soundkit_id)
        return model_to_response_dto(model=soundkit, response_dto=SoundkitResponseDTO)

    async def add_soundkit(self, soundkit: CreateSoundkitRequestDTO) -> None:
        soundkit = request_dto_to_model(model=Soundkit, request_dto=soundkit)
        self.session.add(soundkit)

    async def update_soundkit(self, soundkit: UpdateSoundkitRequestDTO) -> None:
        soundkit = request_dto_to_model(model=Soundkit, request_dto=soundkit)
        await self.session.merge(soundkit)

    async def delete_soundkit(self, soundkit_id: int, user_id: int) -> None:
        query = delete(Soundkit).filter_by(id=soundkit_id, user_id=user_id)
        await self.session.execute(query)
