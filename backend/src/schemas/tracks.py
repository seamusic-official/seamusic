from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict

from src.models.tracks import Track


class STrackBase(BaseModel):
    title: str
    picture: Optional[str]
    description: Optional[str]
    file_path: str
    co_prod: Optional[str]
    prod_by: Optional[str]
    playlist_id: Optional[int]
    user_id: int
    Track_pack_id: Optional[int]


class STrackCreate(STrackBase):
    pass


class STrack(STrackBase):
    id: int
    is_available: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class STrackResponse(BaseModel):
    id: int
    name: str
    prod_by: str
    description: str
    co_prod: str
    type: str
    user_id: int
    is_available: bool
    file_url: str
    picture_url: str
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_db_model(cls, track: Track) -> "STrackResponse":
        return cls(
            id=track.id,
            name=track.name,
            prod_by=track.prod_by,
            description=track.description,
            co_prod=track.co_prod,
            type=track.type,
            user_id=track.user_id,
            is_available=track.is_available,
            file_url=track.file_url,
            picture_url=track.picture_url,
            created_at=track.created_at,
            updated_at=track.updated_at,
        )


class STrackUpdateResponse(BaseModel):
    response: str = "Track updated"


class STrackDeleteResponse(BaseModel):
    response: str = "Track deleted"
