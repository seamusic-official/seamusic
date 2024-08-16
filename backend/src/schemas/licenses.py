from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel

from src.models.licenses import License as _License
from src.schemas.base import FromDBModelMixin, DetailMixin


class License(FromDBModelMixin):
    id: int
    title: str
    picture_url: Optional[str] = None
    description: Optional[str] = None
    file_path: str
    co_prod: Optional[str] = None
    prod_by: Optional[str] = None
    playlist_id: Optional[int] = None
    user_id: int
    beat_pack_id: Optional[int] = None
    price: str
    created_at: datetime
    updated_at: datetime

    _model_type = _License


class SLicenseResponse(License):
    pass


class SLicensesResponse(BaseModel):
    licenses: List[License]


class SMyLicensesResponse(SLicensesResponse):
    pass


class SCreateLicenseRequest(BaseModel):
    title: str
    description: str
    price: str


class SCreateLicenseResponse(License):
    pass


class SEditLicenseRequest(License):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[str] = None


class SEditLicensesResponse(BaseModel, DetailMixin):
    detail: str = "License edited"


class SLicensesDeleteResponse(BaseModel, DetailMixin):
    detail: str = "License deleted"
