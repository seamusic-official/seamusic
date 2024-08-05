from pydantic import BaseModel
from src.schemas.base import SBaseSchema


class Tag(SBaseSchema):
    name: str


class STagRequest(BaseModel):
    name: str


class STagResponse(BaseModel):
    name: str
