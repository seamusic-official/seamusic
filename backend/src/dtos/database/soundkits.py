from datetime import datetime

from dtos.database.base import BaseDTO, BaseResponseDTO, BaseRequestDTO


class Soundkit(BaseDTO):
    title: str
    picture_url: str | None
    description: str | None
    file_path: str
    co_prod: str | None
    prod_by: str | None
    playlist_id: int | None
    user_id: int
    beat_pack_id: int | None


class SoundkitResponseDTO(BaseResponseDTO):
    id: int
    name: str
    description: str
    picture_url: str
    file_url: str
    user_id: int
    is_available: bool
    created_at: datetime
    updated_at: datetime


class SoundkitsResponseDTO(BaseResponseDTO):
    soundkits: list[Soundkit]


class CreateSoundkitRequestDTO(BaseRequestDTO):
    title: str
    picture_url: str | None
    description: str | None
    file_path: str
    co_prod: str | None
    prod_by: str | None
    playlist_id: int | None
    user_id: int
    beat_pack_id: int | None


class UpdateSoundkitRequestDTO(BaseRequestDTO):
    title: str
    picture_url: str | None
    description: str | None
    file_path: str
    co_prod: str | None
    prod_by: str | None
    playlist_id: int | None
    user_id: int
    beat_pack_id: int | None
