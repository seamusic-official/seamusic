from pydantic import BaseModel
from typing import Optional
from datetime import datetime

from src.albums.models import Album


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

    class Config:
        orm_mode = True


class SAlbumResponse(BaseModel):
    title: str
    picture: Optional[str]
    description: Optional[str]
    co_prod: Optional[str]
    prod_by: Optional[str]
    user_id: int

    @classmethod
    def from_db_model(cls, album: Album) -> 'SAlbumResponse':
        return cls(
            title=album.name,
            picture=album.picture_url,
            description=album.description,
            co_prod=album.co_prod,
            prod_by=album.prod_by,
            user_id=album.user_id,
        )


class SAlbumDeleteResponse(BaseModel):
    response: str = 'Album deleted.'