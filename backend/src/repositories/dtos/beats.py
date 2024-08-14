from src.repositories.dtos.base import BaseDTO, BaseResponseDTO, BaseRequestDTO


class Beat(BaseDTO):
    title: str
    description: str
    picture_url: str
    file_url: str
    co_prod: str
    type: str
    user_id: int


class BeatResponseDTO(BaseResponseDTO):
    title: str
    description: str
    picture_url: str
    file_url: str
    co_prod: str
    type: str
    user_id: int


class CreateBeatRequestDTO(BaseRequestDTO):
    title: str
    description: str
    picture_url: str
    file_url: str
    co_prod: str
    type: str
    user_id: int


class UpdateBeatRequestDTO(BaseRequestDTO):
    title: str | None = None
    description: str | None = None
    picture_url: str | None = None
    file_url: str | None = None
    co_prod: str | None = None
    type: str | None = None
    user_id: int | None = None
