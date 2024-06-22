from pydantic import BaseModel, Field
from src.auth.schemas import SUser
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class SLicenseBase(BaseModel):
    title: str
    picture: Optional[str]
    description: Optional[str]
    file_path: str
    co_prod: Optional[str]
    prod_by: Optional[str]
    playlist_id: Optional[int]
    user_id: int
    beat_pack_id: Optional[int]

class SLicense(SLicenseBase):
    id: int
    created_at: datetime
    updated_at: datetime
