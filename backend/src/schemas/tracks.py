from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict

from src.models.tracks import Track
from src.schemas.base import BaseResponse


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


class STrackResponse(BaseResponse):
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

    model_type = Track


class STrackUpdateResponse(BaseModel):
    response: str = "Track updated"


class STrackDeleteResponse(BaseModel):
    response: str = "Track deleted"
