from datetime import datetime
from typing import List

from pydantic import BaseModel

from src.beatpacks.models import Beatpack


class BeatCreate(BaseModel):
    id: int


class BeatpackCreate(BaseModel):
    title: str
    description: str
    beats: List[BeatCreate]


class BeatResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class SBeatpackEditResponse(BaseModel):
    response: str = "Beat pack edited"


class SBeatpackDeleteResponse(BaseModel):
    response: str = "Beat pack deleted"


class SBeatpackResponse(BaseModel):
    id: int
    description: str
    is_available: bool
    title: str
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_db_model(cls, beatpack: Beatpack) -> "SBeatpackResponse":
        return cls(
            id=beatpack.id,
            description=beatpack.description,
            is_available=beatpack.is_available,
            title=beatpack.title,
            created_at=beatpack.created_at,
            updated_at=beatpack.updated_at,
        )
