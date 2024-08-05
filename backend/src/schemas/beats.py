from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict

from src.models.beats import Beat
from src.schemas.base import BaseResponse


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

    model_config = ConfigDict(from_attributes=True)


class SBeatResponse(BaseResponse):
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

    _model_type = Beat


class SBeatDeleteResponse(BaseModel):
    response: str = "Beat deleted"
