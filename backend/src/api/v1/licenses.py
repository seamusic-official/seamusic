from typing import List

from fastapi import APIRouter, Depends, status

from src.schemas.auth import SUser
from src.schemas.licenses import (
    SLicenseBase,
    SLicensesResponse,
    SLicensesEditResponse,
    SLicensesDeleteResponse,
)
from src.services.licenses import LicensesRepository
from src.utils.auth import get_current_user


licenses = APIRouter(prefix="/licenses", tags=["Licenses"])


@licenses.post(
    path="/my",
    summary="Packs by current user",
    response_model=List[SLicensesResponse],
    responses={status.HTTP_200_OK: {"model": List[SLicensesResponse]}},
)
async def get_user_licenses(
    user: SUser = Depends(get_current_user),
) -> List[SLicensesResponse]:
    response = await LicensesRepository.find_all(owner=user)
    return [SLicensesResponse.from_db_model(model=license_) for license_ in response]


@licenses.get(
    path="/all",
    summary="Get all licenses",
    response_model=List[SLicensesResponse],
    responses={status.HTTP_200_OK: {"model": List[SLicensesResponse]}},
)
async def all_licenses() -> List[SLicensesResponse]:
    response = await LicensesRepository.find_all()
    return [SLicensesResponse.from_db_model(model=_license) for _license in response]


@licenses.get(
    path="/{license_id}",
    summary="Get license by id",
    response_model=SLicensesResponse,
    responses={status.HTTP_200_OK: {"model": SLicensesResponse}},
)
async def get_one(license_id: int) -> SLicensesResponse:
    response = await LicensesRepository.find_one_by_id(int(license_id))
    return SLicensesResponse.from_db_model(model=response)


@licenses.post(
    path="/beatbacks/add",
    summary="Add a file for new beat",
    response_model=SLicensesResponse,
    responses={status.HTTP_200_OK: {"model": SLicensesResponse}},
)
async def add_licenses(data: SLicenseBase, user: SUser = Depends(get_current_user)):
    data = {"title": data.title, "description": data.description, "price": data.price}

    response = await LicensesRepository.add_one(data)
    return SLicensesResponse.from_db_model(model=response)


@licenses.put(
    path="/update/{license_id}",
    summary="Edit license by id",
    response_model=SLicensesEditResponse,
    responses={status.HTTP_200_OK: {"model": SLicensesEditResponse}},
)
async def update_licenses(
    license_id: int, licenses_data: SLicenseBase
) -> SLicensesEditResponse:
    data = {
        "title": licenses_data.title,
        "description": licenses_data.description,
    }

    await LicensesRepository.edit_one(license_id, data)
    return SLicensesEditResponse


@licenses.delete(
    path="/delete/{license_id}",
    summary="Create new licenses",
    response_model=SLicensesDeleteResponse,
    responses={status.HTTP_200_OK: {"model": SLicensesDeleteResponse}},
)
async def delete_licenses(license_id: int) -> SLicensesDeleteResponse:
    await LicensesRepository.delete(id_=license_id)

    return SLicensesDeleteResponse
