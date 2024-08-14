from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.repositories.dtos.beatpacks import (
    BeatpackResponseDTO,
    BeatpacksResponseDTO,
    CreateBeatpackRequestDTO,
    UpdateBeatpackRequestDTO
)


@dataclass
class BaseBeatpacksRepository(ABC):
    @abstractmethod
    async def get_user_beatpacks(self, user_id: int) -> BeatpacksResponseDTO:
        ...

    @abstractmethod
    async def get_all_beatpacks(self) -> BeatpacksResponseDTO:
        ...

    @abstractmethod
    async def get_one_beatpack(self, beatpack_id: int) -> BeatpackResponseDTO:
        ...

    @abstractmethod
    async def add_beatpack(self, album: CreateBeatpackRequestDTO) -> BeatpackResponseDTO:
        ...

    @abstractmethod
    async def update_beatpack(self, album: UpdateBeatpackRequestDTO) -> BeatpackResponseDTO:
        ...

    @abstractmethod
    async def delete_beatpack(self, beatpack_id: int, user_id: int) -> None:
        ...
