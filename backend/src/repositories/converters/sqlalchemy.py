from src.core.database import Base
from src.repositories.dtos.base import BaseRequestDTO, BaseResponseDTO, BaseDTO


def model_to_response_dto(response_dto: type[BaseResponseDTO], model: Base | None = None) -> BaseResponseDTO | None:
    return response_dto(**model.__dict__) if model else None


def models_to_dto(models: list[Base], dto: type[BaseDTO]) -> list[BaseDTO]:
    return list(map(lambda model: dto(**model.__dict__), models))


def request_dto_to_model(request_dto: BaseRequestDTO, model: type[Base]):
    return model(**request_dto.model_dump())
