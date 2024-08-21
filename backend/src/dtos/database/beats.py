from datetime import datetime

from src.dtos.database.base import BaseDTO, BaseResponseDTO, BaseRequestDTO
from src.enums.type import Type


class Beat(BaseDTO):
    title: str
    description: str
    picture_url: str
    file_url: str
    co_prod: str
    type: str
    user_id: int


class BeatResponseDTO(BaseResponseDTO):
    id: int
    title: str
    description: str
    picture_url: str
    file_url: str
    prod_by: str
    co_prod: str
    type: str
    user_id: int
    created_at: datetime
    updated_at: datetime
    is_available: bool = True


class BeatsResponseDTO(BaseResponseDTO):
    beats: list[Beat]


class CreateBeatRequestDTO(BaseRequestDTO):
    title: str
    description: str
    file_url: str
    co_prod: str | None = None
    type: Type = Type.beat
    user_id: int
    created_at: datetime
    updated_at: datetime
    is_available: bool = True


class UpdateBeatRequestDTO(BaseRequestDTO):
    title: str | None = None
    description: str | None = None
    picture_url: str | None = None
    file_url: str | None = None
    prod_by: str | None = None
    co_prod: str | None = None
    type: str | None = None
    user_id: int | None = None
