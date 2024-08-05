from datetime import datetime
from typing import List

from pydantic import BaseModel, ConfigDict

from src.models.beatpacks import Beatpack
from src.schemas.base import BaseResponse


class BeatCreate(BaseModel):
    id: int


class BeatpackCreate(BaseModel):
    title: str
    description: str
    beats: List[BeatCreate]


class BeatResponse(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)


class SBeatpackEditResponse(BaseModel):
    response: str = "Beat pack edited"


class SBeatpackDeleteResponse(BaseModel):
    response: str = "Beat pack deleted"


class SBeatpackResponse(BaseResponse):
    id: int
    description: str
    is_available: bool
    title: str
    created_at: datetime
    updated_at: datetime

    model_type = Beatpack
