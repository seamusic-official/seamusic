from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.repositories.dtos.beats import (
    BeatResponseDTO,
    CreateBeatRequestDTO,
    UpdateBeatRequestDTO
    )


@dataclass
class BaseBeatsRepository(ABC):
    @abstractmethod
    async def get_user_beats(self, user_id: int) -> list[BeatResponseDTO]:
        ...

    @abstractmethod
    async def all_beats(self) -> list[BeatResponseDTO]:
        ...

    @abstractmethod
    async def get_one_beat(self, beat_id: int) -> BeatResponseDTO:
        ...

    @abstractmethod
    async def create_beat(self, beat: CreateBeatRequestDTO) -> BeatResponseDTO:
        ...

    @abstractmethod
    async def update_beat(self, beat: UpdateBeatRequestDTO) -> BeatResponseDTO:
        ...

    @abstractmethod
    async def delete_beat(self, beat_id: int, user_id: int) -> None:
        ...
