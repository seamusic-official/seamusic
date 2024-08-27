from dataclasses import dataclass
from io import BytesIO

from src.dtos.database.soundkits import (
    SoundkitsResponseDTO,
    SoundkitResponseDTO,
    CreateSoundkitRequestDTO,
    CreateSoundkitResponseDTO,
    UpdateSoundkitResponseDTO,
    UpdateSoundkitRequestDTO
)
from src.exceptions.services import NotFoundException, NoRightsException
from src.repositories import DatabaseRepositories, BaseMediaRepository
from src.repositories.database.soundkits.base import BaseSoundkitsRepository
from src.repositories.database.soundkits.postgres import init_postgres_repository
from src.repositories.media.s3 import init_s3_repository
from src.services.base import BaseService


@dataclass
class SoundkitsDatabaseRepositories(DatabaseRepositories):
    soundkits: BaseSoundkitsRepository


@dataclass
class SoundkitsRepositories:
    database: SoundkitsDatabaseRepositories
    media: BaseMediaRepository


@dataclass
class SoundkitsService(BaseService):
    repositories: SoundkitsRepositories

    async def get_user_soundkits(self, user_id: int,) -> SoundkitsResponseDTO:
        return await self.repositories.database.soundkits.get_user_soundkits(user_id=user_id)

    async def get_all_soundkits(self) -> SoundkitsResponseDTO:
        return await self.repositories.database.soundkits.get_all_soundkits()

    async def get_soundkit_by_id(self, soundkit_id: int) -> SoundkitResponseDTO:
        soundkit = await self.repositories.database.soundkits.get_soundkit_by_id(soundkit_id=soundkit_id)

        if not soundkit:
            raise NotFoundException()

        return soundkit

    async def add_soundkit(
        self,
        user_id: int,
        prod_by: str,
        file_stream: BytesIO,
        file_info: str,
    ) -> CreateSoundkitResponseDTO:

        file_url = await self.repositories.media.upload_file("AUDIOFILES", file_info, file_stream)

        data = CreateSoundkitRequestDTO(
            title="Title",
            description="Description",
            file_path=file_url,
            prod_by=prod_by,
            user_id=user_id,
        )

        soundkit_id = await self.repositories.database.soundkits.add_soundkit(soundkit=data)
        return CreateSoundkitResponseDTO(id=soundkit_id)

    async def update_soundkit_picture(
        self,
        soundkit_id: int,
        user_id: int,
        file_info: str,
        file_stream: BytesIO,
    ) -> UpdateSoundkitResponseDTO:

        soundkit = await self.repositories.database.soundkits.get_soundkit_by_id(soundkit_id=soundkit_id)

        if soundkit.user_id != user_id:
            raise NoRightsException()

        file_url = await self.repositories.media.upload_file("PICTURES", file_info, file_stream)

        data = UpdateSoundkitRequestDTO(picture_url=file_url)
        soundkit_id = await self.repositories.database.soundkits.update_soundkit(soundkit=data)
        return UpdateSoundkitResponseDTO(id=soundkit_id)

    async def release_soundkit(
        self,
        soundkit_id: int,
        user_id: int,
        data: UpdateSoundkitRequestDTO,
    ) -> UpdateSoundkitResponseDTO:

        soundkit = await self.repositories.database.soundkits.get_soundkit_by_id(soundkit_id=soundkit_id)

        if soundkit.user_id != user_id:
            raise NoRightsException()

        soundkit_id = self.repositories.database.soundkits.update_soundkit(soundkit=data)

        return UpdateSoundkitResponseDTO(id=soundkit_id)

    async def update_soundkit(
        self,
        soundkit_id: int,
        user_id: int,
        data: UpdateSoundkitRequestDTO,
    ) -> UpdateSoundkitResponseDTO:

        soundkit = await self.repositories.database.soundkits.get_soundkit_by_id(soundkit_id=soundkit_id)

        if soundkit.user_id != user_id:
            raise NoRightsException()

        soundkit_id = self.repositories.database.soundkits.update_soundkit(soundkit=data)

        return UpdateSoundkitResponseDTO(id=soundkit_id)

    async def delete_soundkits(
        self,
        soundkit_id: int,
        user_id: int,
    ) -> None:

        soundkit = await self.repositories.database.soundkits.get_soundkit_by_id(soundkit_id=soundkit_id)

        if soundkit.user_id != user_id:
            raise NoRightsException()

        await self.repositories.database.soundkits.delete_soundkit(soundkit_id=soundkit_id, user_id=user_id)


def get_soundkits_repositories() -> SoundkitsRepositories:
    return SoundkitsRepositories(
        database=SoundkitsDatabaseRepositories(soundkits=init_postgres_repository()),
        media=init_s3_repository()
    )


def get_soundkits_service() -> SoundkitsService:
    return SoundkitsService(repositories=get_soundkits_repositories())
