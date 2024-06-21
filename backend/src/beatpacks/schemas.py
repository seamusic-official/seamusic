from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from src.beats.schemas import SBeat

class SBeatpackBase(BaseModel):
    title: str
    description: str
    owner_id: int
    beats: List[SBeat] = Field(...)
    
class SBeatPackCreate(SBeatpackBase):
    pass

class SBeatPack(SBeatpackBase):
    id: int
    liked: bool
    is_available: bool
    created_at: datetime

    class Config:
        orm_mode = True