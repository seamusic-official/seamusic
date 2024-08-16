from src.dtos.database.base import BaseRequestDTO, BaseResponseDTO, BaseDTO


class Tag(BaseDTO):
    name: str


class TagResponseDTO(BaseResponseDTO):
    name: str


class TagsResponseDTO(BaseResponseDTO):
    tags: list[Tag]


class AddTagRequestDTO(BaseRequestDTO):
    name: str


class UpdateTagRequestDTO(BaseRequestDTO):
    name: str
