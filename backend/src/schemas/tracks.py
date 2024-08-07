from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel

from src.models.tracks import Track
from src.schemas.base import DetailMixin


class STrack(BaseModel):
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

    _model_type = Track


class SMyTracksResponse(BaseModel):
    tracks: List[STrack]


class SAllTracksResponse(BaseModel):
    tracks: List[STrack]


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

    _model_type = Track


class SAddTracksResponse(BaseModel):
    title: str
    file_url: str
    prod_by: str
    user_id: int
    type: str

    _model_type = Track


class SUpdateTrackPictureResponse(STrackResponse):
    pass


class SReleaseTrackRequest(BaseModel):
    title: str
    picture: Optional[str]
    description: Optional[str]
    file_path: str
    co_prod: Optional[str]
    prod_by: Optional[str]
    playlist_id: Optional[int]
    user_id: int
    Track_pack_id: Optional[int]


class SReleaseTrackResponse(STrackResponse):
    pass


class SUpdateTrackRequest(BaseModel):
    title: str
    picture: Optional[str]
    description: Optional[str]
    file_path: str
    co_prod: Optional[str]
    prod_by: Optional[str]
    playlist_id: Optional[int]
    user_id: int
    Track_pack_id: Optional[int]


class SUpdateTrackResponse(BaseModel, DetailMixin):
    detail: str = "Track updated"


class SDeleteTrackResponse(BaseModel, DetailMixin):
    detail: str = "Track deleted"
