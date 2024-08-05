from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel

from src.models.tracks import Track
from src.schemas.base import BaseResponse


class STrack(BaseResponse):
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


class SMyTracksResponse(BaseResponse):
    tracks: List[STrack]


class SAllTracksResponse(BaseResponse):
    tracks: List[STrack]


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

    _model_type = Track


class SAddTracksResponse(BaseResponse):
    title: str
    file_url: str
    prod_by: str
    user_id: int
    type: str

    _model_type = Track


class SUpdateTrackPictureResponse(BaseResponse, STrackResponse):
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


class SReleaseTrackResponse(BaseResponse, STrackResponse):
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


class SUpdateTrackResponse(BaseResponse):
    message = "Track updated"


class SDeleteTrackResponse(BaseResponse):
    message = "Track deleted"
