from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from src.soundkits.models import Soundkit


class SSoundkitBase(BaseModel):
    title: str
    picture: Optional[str]
    description: Optional[str]
    file_path: str
    co_prod: Optional[str]
    prod_by: Optional[str]
    playlist_id: Optional[int]
    user_id: int
    beat_pack_id: Optional[int]


class SSoundkitUpdate(BaseModel):
    title: Optional[str]
    picture: Optional[str]
    description: Optional[str]
    co_prod: Optional[str]
    prod_by: Optional[str]


class SSoundkitCreate(SSoundkitBase):
    pass


class SSoundkit(SSoundkitBase):
    id: int
    is_available: bool
    created_at: datetime

    class Config:
        orm_mode = True


class SSoundkitResponse(BaseModel):
    id: int
    name: str
    description: str
    picture_url: str
    file_url: str
    user_id: int
    is_available: bool
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_db_model(cls, soundkit: Soundkit) -> "SSoundkitResponse":
        return cls(
            id=soundkit.id,
            name=soundkit.name,
            description=soundkit.description,
            picture_url=soundkit.picture_url,
            file_url=soundkit.file_url,
            user_id=soundkit.user_id,
            is_available=soundkit.is_available,
            created_at=soundkit.created_at,
            updated_at=soundkit.updated_at,
        )


class SSoundkitDeleteResponse(BaseModel):
    response: str = "Soundkit deleted"
