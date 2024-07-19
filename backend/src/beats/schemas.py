from pydantic import BaseModel, Field
from src.auth.schemas import SUser
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


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

    class Config:
        orm_mode = True
