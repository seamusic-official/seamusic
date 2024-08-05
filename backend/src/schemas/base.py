from typing import Type

from pydantic import BaseModel, ConfigDict

from src.core.database import Base


class BaseResponse(BaseModel):
    model_config = ConfigDict(extra='ignore')
    model_type: Type[Base]

    def from_db_model(self, model: Base) -> "BaseResponse":
        if not isinstance(model, self.model_type):
            raise TypeError(f'`model` is not an instance of class {self.model_type}')

        return self.model_validate(**model.__dict__)
