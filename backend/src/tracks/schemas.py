from pydantic import BaseModel, Field
from src.auth.schemas import SUser
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class STrackBase(BaseModel):
    title: str
    picture: Optional[str]
    description: Optional[str]
    file_path: str
    co_prod: Optional[str]
    prod_by: Optional[str]
    playlist_id: Optional[int]
    user_id: int
    Track_pack_id: Optional[int]

class STrackCreate(STrackBase):
    pass

class STrack(STrackBase):
    id: int
    is_available: bool
    created_at: datetime

    class Config:
        orm_mode = True
