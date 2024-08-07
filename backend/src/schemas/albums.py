import datetime
from typing import List

from pydantic import BaseModel

from src.models.albums import Album as _Album
from src.schemas.base import FromDBModelMixin, DetailMixin


class Album(BaseModel, FromDBModelMixin):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    is_available: bool
    title: str
    picture_url: str
    description: str
    co_prod: str
    type: str = "album"

    _model_type = _Album


class SMyAlbumsResponse(BaseModel):
    albums: List[Album]


class SAllAlbumsResponse(BaseModel):
    albums: List[Album]


class SAlbumResponse(Album):
    pass


class SAddAlbumResponse(Album):
    pass


class SUpdateAlbumPictureResponse(Album):
    pass


class SReleaseAlbumsRequest(BaseModel):
    title: str
    name: str
    picture_url: str
    description: str
    co_prod: str
    type: str = "album"


class SReleaseAlbumsResponse(Album):
    pass


class SUpdateAlbumRequest(BaseModel):
    title: str
    picture_url: str
    description: str
    co_prod: str
    prod_by: str
    type: str = "album"


class SUpdateAlbumResponse(Album):
    pass


class SDeleteAlbumResponse(BaseModel, DetailMixin):
    message: str = "Album was deleted."
