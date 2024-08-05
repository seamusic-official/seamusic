from typing import Type

from pydantic import BaseModel, ConfigDict

from src.core.database import Base


class BaseResponse(BaseModel):
    model_config = ConfigDict(extra='ignore')
    model_type: Type[Base]

    @classmethod
    def from_db_model(cls, model: Base) -> "BaseResponse":
        if not isinstance(model, cls.model_type):
            raise TypeError(f'`model` is not an instance of class {cls.model_type}')

        return cls.model_validate(**model.__dict__)
