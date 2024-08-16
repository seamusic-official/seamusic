from datetime import datetime

from dtos.database.base import BaseResponseDTO, BaseDTO, BaseRequestDTO


class License(BaseDTO):
    id: int
    title: str
    picture_url: str | None = None
    description: str | None = None
    file_path: str
    co_prod: str | None = None
    prod_by: str | None = None
    playlist_id: int | None = None
    user_id: int
    beat_pack_id: int | None = None
    price: str
    created_at: datetime
    updated_at: datetime


class LicenseResponseDTO(BaseResponseDTO):
    id: int
    title: str
    picture_url: str | None = None
    description: str | None = None
    file_path: str
    co_prod: str | None = None
    prod_by: str | None = None
    playlist_id: int | None = None
    user_id: int
    beat_pack_id: int | None = None
    price: str
    created_at: datetime
    updated_at: datetime


class LicensesResponseDTO(BaseResponseDTO):
    licenses: list[License]


class CreateLicenseRequestDTO(BaseRequestDTO):
    id: int
    title: str
    picture_url: str | None = None
    description: str | None = None
    file_path: str
    co_prod: str | None = None
    prod_by: str | None = None
    playlist_id: int | None = None
    user_id: int
    beat_pack_id: int | None = None
    price: str
    created_at: datetime
    updated_at: datetime


class UpdateLicenseRequestDTO(BaseRequestDTO):
    title: str | None = None
    description: str | None = None
    price: str | None = None
