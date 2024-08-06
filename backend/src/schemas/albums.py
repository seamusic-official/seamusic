from typing import List, Optional

from pydantic import BaseModel

from src.schemas.base import SBaseSchema


class Album(SBaseSchema):
    name: str
    picture_url: str
    description: str
    co_prod: str
    type: str = "album"


class SAlbumRequest(BaseModel):
    name: str
    picture_url: str
    description: str
    co_prod: str
    type: str = "album"


class SAlbumResponse(SBaseSchema):
    albums: List[Album]


class SAlbumDetail(SBaseSchema):
    name: str
    picture_url: str
    description: str
    co_prod: str
    type: str


class SAlbumCreate(BaseModel):
    name: str
    picture_url: str
    description: str
    co_prod: str
    type: str = "album"


class SAlbumUpdate(SBaseSchema):
    name: Optional[str]
    picture_url: Optional[str]
    description: Optional[str]
    co_prod: Optional[str]


class SAlbumDelete(BaseModel):
    response: str = "Album was deleted."
