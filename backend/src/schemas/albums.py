from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict

from src.models.albums import Album
from src.schemas.base import BaseResponse


class SAlbumBase(BaseModel):
    title: str
    picture: Optional[str]
    description: Optional[str]
    file_path: str
    co_prod: Optional[str]
    prod_by: Optional[str]
    playlist_id: Optional[int]
    user_id: int
    Track_pack_id: Optional[int]


class SAlbumEdit(BaseModel):
    name: str
    description: Optional[str]
    prod_by: Optional[str]


class SAlbumCreate(SAlbumBase):
    pass


class SAlbum(SAlbumBase):
    id: int
    is_available: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class SAlbumResponse(BaseResponse):
    title: str
    picture: Optional[str]
    description: Optional[str]
    co_prod: Optional[str]
    prod_by: Optional[str]
    user_id: int

    model_type = Album


class SAlbumDeleteResponse(BaseModel):
    response: str = "Album deleted."
