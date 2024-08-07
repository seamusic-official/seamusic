from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel

from src.models.beats import Beat as _Beat
from src.schemas.base import FromDBModelMixin, DetailMixin


class Beat(BaseModel, FromDBModelMixin):
    id: int
    title: str
    description: Optional[str] = None
    picture_url: Optional[str] = None
    file_url: str
    co_prod: Optional[str] = None
    prod_by: Optional[str] = None
    user_id: int
    is_available: bool
    created_at: datetime
    updated_at: datetime

    _model_type = _Beat


class SBeatResponse(Beat):
    pass


class SBeatsResponse(BaseModel):
    beats: List[Beat]


class SMyBeatsResponse(SBeatsResponse):
    pass


class SCreateBeatResponse(Beat):
    pass


class SUpdateBeatPictureResponse(Beat):
    pass


class SBeatReleaseRequest(BaseModel, FromDBModelMixin):
    title: Optional[str]
    description: Optional[str]
    co_prod: Optional[str]
    prod_by: Optional[str]

    _model_type = _Beat


class SBeatReleaseResponse(Beat):
    pass


class SBeatUpdateRequest(BaseModel):
    title: Optional[str]
    description: Optional[str]
    picture_url: Optional[str]
    co_prod: Optional[str]
    prod_by: Optional[str]


class SBeatUpdateResponse(Beat):
    pass


class SDeleteBeatResponse(BaseModel, DetailMixin):
    response: str = "Beat deleted"
