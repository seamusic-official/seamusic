from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from src.licenses.models import License


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


class SLicensesResponse(BaseModel):
    id: int
    title: str
    price: str
    description: str
    picture_url: str | None
    is_available: bool
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_db_model(cls, licenses: License) -> 'SLicensesResponse':
        return cls(
            id=licenses.id,
            title=licenses.title,
            price=licenses.price,
            description=licenses.description,
            picture_url=licenses.picture_url,
            is_available=licenses.is_available,
            created_at=licenses.created_at,
            updated_at=licenses.updated_at
        )


class SLicensesEditResponse(BaseModel):
    response: str = "License edited"


class SLicensesDeleteResponse(BaseModel):
    response: str = "License deleted"
