from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from src.beats.models import Beat


class SBeatBase(BaseModel):
    id: int
    title: str
    description: Optional[str]
    picture_url: Optional[str]
    file_url: str
    co_prod: Optional[str]
    prod_by: Optional[str]
    view_count: Optional[int] = None

    playlist_id: Optional[int] = None
    user_id: int
    beat_pack_id: Optional[int] = None


class SBeatUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    picture_url: Optional[str]
    co_prod: Optional[str]
    prod_by: Optional[str]


class SBeatRelease(BaseModel):
    title: Optional[str]
    description: Optional[str]
    co_prod: Optional[str]
    prod_by: Optional[str]


class SBeatCreate(SBeatBase):
    pass


class SBeat(SBeatBase):
    id: int
    is_available: bool
    created_at: datetime

    class Config:
        orm_mode = True


class SBeatResponse(BaseModel):
    id: int
    title: str
    description: str
    picture_url: str
    type: str
    file_url: str
    user_id: int
    is_available: bool
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_db_model(cls, beat: Beat) -> "SBeatResponse":
        return cls(
            id=beat.id,
            title=beat.title,
            description=beat.description,
            picture_url=beat.picture_url,
            type=beat.type,
            file_url=beat.file_url,
            user_id=beat.user_id,
            is_available=beat.is_available,
            created_at=beat.created_at,
            updated_at=beat.updated_at,
        )


class SBeatDeleteResponse(BaseModel):
    response: str = "Beat deleted"
