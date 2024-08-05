from datetime import datetime
from typing import Type, Optional

from pydantic import BaseModel, ConfigDict

from src.core.database import Base


class SBaseSchema(BaseModel):
    id: int
    is_available: bool
    created_at: datetime
    updated_at: datetime


class BaseResponse(BaseModel):
    _model_type: Type[Base]
    message: Optional[str] = None

    model_config = ConfigDict(extra='ignore')

    @classmethod
    def from_db_model(cls, model: Base) -> "cls":  # noqa: F821
        if not isinstance(model, cls._model_type):
            raise TypeError(f'`model` is not an instance of class {cls._model_type}')

        return cls.model_validate(**model.__dict__)
