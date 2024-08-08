from typing import List, Optional

from pydantic import BaseModel

from src.models.beatpacks import Beatpack as _Beatpack
from src.schemas.auth import User
from src.schemas.base import FromDBModelMixin, DetailMixin
from src.schemas.beats import Beat


class Beatpack(FromDBModelMixin):
    title: str
    description: str
    users: List[User]
    beats: List[Beat]

    _model_type = _Beatpack


class SBeatpackResponse(Beatpack):
    pass


class SBeatpacksResponse(BaseModel):
    beatpacks: List[Beatpack]


class SMyBeatpacksResponse(SBeatpacksResponse):
    pass


class SCreateBeatpackRequest(BaseModel):
    title: str
    description: str
    beats: List[Beat]


class SCreateBeatpackResponse(Beatpack):
    pass


class SEditBeatpackRequest(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


class SEditBeatpackResponse(BaseModel, DetailMixin):
    detail: str = "Beatpack edited"


class SDeleteBeatpackResponse(BaseModel, DetailMixin):
    detail: str = "Beat pack deleted"
