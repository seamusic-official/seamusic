from src.repositories.dtos.base import BaseDTO, BaseResponseDTO, BaseRequestDTO


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
