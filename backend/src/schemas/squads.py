from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, Field, ConfigDict


class SBeatBase(BaseModel):
    title: str
    picture: Optional[str]
    description: Optional[str]
    file_path: str
    co_prod: Optional[str]
    prod_by: Optional[str]
    playlist_id: Optional[int]
    user_id: int
    beat_pack_id: Optional[int]


class SBeatCreate(SBeatBase):
    pass


class SBeat(SBeatBase):
    id: int
    is_available: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class SBeatPackBase(BaseModel):
    title: str
    description: str
    owner_id: int
    beats: List[SBeat] = Field(...)


class SBeatPackCreate(SBeatPackBase):
    pass


class SBeatPack(SBeatPackBase):
    id: int
    liked: bool
    is_available: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
