from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict

from src.models.soundkits import Soundkit
from src.schemas.base import BaseResponse


class SSoundkitBase(BaseModel):
    title: str
    picture: Optional[str]
    description: Optional[str]
    file_path: str
    co_prod: Optional[str]
    prod_by: Optional[str]
    playlist_id: Optional[int]
    user_id: int
    beat_pack_id: Optional[int]


class SSoundkitUpdate(BaseModel):
    title: Optional[str]
    picture: Optional[str]
    description: Optional[str]
    co_prod: Optional[str]
    prod_by: Optional[str]


class SSoundkitCreate(SSoundkitBase):
    pass


class SSoundkit(SSoundkitBase):
    id: int
    is_available: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class SSoundkitResponse(BaseResponse):
    id: int
    name: str
    description: str
    picture_url: str
    file_url: str
    user_id: int
    is_available: bool
    created_at: datetime
    updated_at: datetime

    model_type = Soundkit


class SSoundkitDeleteResponse(BaseModel):
    response: str = "Soundkit deleted"
