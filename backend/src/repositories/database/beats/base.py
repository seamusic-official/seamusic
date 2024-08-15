from abc import ABC, abstractmethod
from dataclasses import dataclass

from repositories.dtos.beats import BeatsResponseDTO
from src.repositories.dtos.beats import (
    BeatResponseDTO,
    CreateBeatRequestDTO,
    UpdateBeatRequestDTO
)


@dataclass
class BaseBeatsRepository(ABC):
    @abstractmethod
    async def get_user_beats(self, user_id: int) -> BeatsResponseDTO:
        ...

    @abstractmethod
    async def all_beats(self) -> BeatsResponseDTO:
        ...

    @abstractmethod
    async def get_one_beat(self, beat_id: int) -> BeatResponseDTO | None:
        ...

    @abstractmethod
    async def create_beat(self, beat: CreateBeatRequestDTO) -> None:
        ...

    @abstractmethod
    async def update_beat(self, beat: UpdateBeatRequestDTO) -> None:
        ...

    @abstractmethod
    async def delete_beat(self, beat_id: int, user_id: int) -> None:
        ...
