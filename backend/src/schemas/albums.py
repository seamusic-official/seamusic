from typing import List

from pydantic import BaseModel

from src.models.albums import Album as _Album
from src.schemas.base import BaseSchema, BaseResponse, FromDBModelMixin


class Album(BaseSchema, FromDBModelMixin):
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


class SAlbumResponse(BaseResponse, Album, BaseSchema):
    pass


class SAddAlbumResponse(BaseResponse, Album, BaseSchema):
    pass


class SUpdateAlbumPictureResponse(BaseResponse, Album):
    pass


class SReleaseAlbumsRequest(BaseModel):
    title: str
    name: str
    picture_url: str
    description: str
    co_prod: str
    type: str = "album"


class SReleaseAlbumsResponse(BaseResponse, BaseSchema, Album):
    pass


class SUpdateAlbumRequest(BaseModel):
    title: str
    picture_url: str
    description: str
    co_prod: str
    prod_by: str
    type: str = "album"


class SUpdateAlbumResponse(BaseResponse, BaseSchema, Album):
    pass


class SDeleteAlbumResponse(BaseResponse):
    message = "Album was deleted."
