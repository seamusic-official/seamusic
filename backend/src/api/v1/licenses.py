from fastapi import APIRouter, Depends, status

from src.models.auth import User
from src.schemas.licenses import (
    SLicensesResponse,
    SEditLicensesResponse,
    SLicensesDeleteResponse,
    SMyLicensesResponse, SLicenseResponse, SCreateLicenseRequest, SCreateLicenseResponse, SEditLicenseRequest,
)
from src.services.licenses import LicensesRepository
from src.utils.auth import get_current_user


licenses = APIRouter(prefix="/licenses", tags=["Licenses"])


@licenses.post(
    path="/my",
    summary="Packs by current user",
    response_model=SMyLicensesResponse,
    responses={status.HTTP_200_OK: {"model": SMyLicensesResponse}},
)
async def get_user_licenses(user: User = Depends(get_current_user)) -> SMyLicensesResponse:
    response = await LicensesRepository.find_all(owner=user)
    return SMyLicensesResponse(licenses=[SLicensesResponse.from_db_model(model=license_) for license_ in response])


@licenses.get(
    path="/all",
    summary="Get all licenses",
    response_model=SLicensesResponse,
    responses={status.HTTP_200_OK: {"model": SLicensesResponse}},
)
async def all_licenses() -> SLicensesResponse:
    response = await LicensesRepository.find_all()
    return SLicensesResponse(licenses=[SLicensesResponse.from_db_model(model=_license) for _license in response])


@licenses.get(
    path="/{license_id}",
    summary="Get license by id",
    response_model=SLicenseResponse,
    responses={status.HTTP_200_OK: {"model": SLicenseResponse}},
)
async def get_one(license_id: int) -> SLicenseResponse:
    response = await LicensesRepository.find_one_by_id(int(license_id))
    return SLicenseResponse.from_db_model(model=response)


@licenses.post(
    path="/beatbacks/add",
    summary="Add a file for new beat",
    response_model=SCreateLicenseResponse,
    responses={status.HTTP_200_OK: {"model": SCreateLicenseResponse}},
)
async def add_license(
    data: SCreateLicenseRequest,
    user: User = Depends(get_current_user)
) -> SCreateLicenseResponse:

    response = await LicensesRepository.add_one(data.mo)
    return SCreateLicenseResponse.from_db_model(model=response)


@licenses.put(
    path="/update/{license_id}",
    summary="Edit license by id",
    response_model=SEditLicensesResponse,
    responses={status.HTTP_200_OK: {"model": SEditLicensesResponse}},
)
async def update_license(
    license_id: int,
    licenses_data: SEditLicenseRequest
) -> SEditLicensesResponse:
    data = {
        "title": licenses_data.title,
        "description": licenses_data.description,
    }

    await LicensesRepository.edit_one(license_id, data)
    return SEditLicensesResponse()


@licenses.delete(
    path="/delete/{license_id}",
    summary="Create new licenses",
    response_model=SLicensesDeleteResponse,
    responses={status.HTTP_200_OK: {"model": SLicensesDeleteResponse}},
)
async def delete_licenses(license_id: int) -> SLicensesDeleteResponse:
    await LicensesRepository.delete(id_=license_id)

    return SLicensesDeleteResponse()
