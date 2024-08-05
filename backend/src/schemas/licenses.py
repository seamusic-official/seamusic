from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from src.models.licenses import License
from src.schemas.base import BaseResponse


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
    price: str


class SLicense(SLicenseBase):
    id: int
    created_at: datetime
    updated_at: datetime


class SLicensesResponse(BaseResponse):
    id: int
    title: str
    price: str
    description: str
    picture_url: str | None
    is_available: bool
    created_at: datetime
    updated_at: datetime

    _model_type = License


class SLicensesEditResponse(BaseModel):
    response: str = "License edited"


class SLicensesDeleteResponse(BaseModel):
    response: str = "License deleted"
