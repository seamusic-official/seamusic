from pydantic import BaseModel, ConfigDict

from src.core.database import Base


class FromDBModelMixin(BaseModel):
    _model_type: type[Base]
    model_config = ConfigDict(extra="ignore")

    @classmethod
    def from_db_model(cls, model: Base) -> "cls":  # noqa: F821
        if not isinstance(model, cls._model_type):
            raise TypeError(f"`model` is not an instance of class {cls._model_type}")

        return cls.model_validate(**model.__dict__)


class DetailMixin:
    detail: str | None = None
