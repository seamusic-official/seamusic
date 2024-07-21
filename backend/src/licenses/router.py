from typing import List

from src.licenses.services import LicensesRepository
from src.auth.schemas import SUser
from src.auth.dependencies import get_current_user
from src.licenses.schemas import SLicenseBase, SLicensesResponse, SLicensesEditResponse, SLicensesDeleteResponse

from fastapi import APIRouter, Depends, status


licenses = APIRouter(
    prefix = "/licenses",
    tags = ["Licenses"]
)

@licenses.post(
    "/my",
    summary="Packs by current user",
    response_model=List[SLicensesResponse],
    responses={
        status.HTTP_200_OK: {'model': List[SLicensesResponse]}
    }
)
async def get_user_licenses(user: SUser = Depends(get_current_user)) -> List[SLicensesResponse]:
    response = await LicensesRepository.find_all(owner=user)

    return [SLicensesResponse.from_db_model(licenses=license) for license in response]

@licenses.get(
    "/all",
    summary="Get all licenses",
    response_model=List[SLicensesResponse],
    responses={
        status.HTTP_200_OK: {'model': List[SLicensesResponse]}
    }
)
async def all_licenses() -> List[SLicensesResponse]:
    response =  await LicensesRepository.find_all()

    return [SLicensesResponse.from_db_model(licenses=_license) for _license in response]

@licenses.get(
    "/{id}",
    summary="Get license by id",
    response_model=SLicensesResponse,
    responses={
        status.HTTP_200_OK: {'model': SLicensesResponse}
    }
)
async def get_one(id: int) -> SLicensesResponse:
    response = await LicensesRepository.find_one_by_id(int(id))

    return SLicensesResponse.from_db_model(licenses=response)

@licenses.post(
    "/beatbacks/add",
    summary="Add a file for new beat",
    response_model=SLicensesResponse,
    responses={
        status.HTTP_200_OK: {'model': SLicensesResponse}
    }
)
async def add_licenses(data: SLicenseBase, user: SUser = Depends(get_current_user)):
    data = {
        "title": data.title,
        "description": data.description,
        "price": data.price
    }
    
    response = await LicensesRepository.add_one(data)

    return SLicensesResponse.from_db_model(licenses=response)

@licenses.put(
    "/update/{id}",
    summary="Edit license by id",
    response_model=SLicensesEditResponse,
    responses={
        status.HTTP_200_OK: {'model': SLicensesEditResponse}
    }
)
async def update_licenses(id: int, licenses_data: SLicenseBase) -> SLicensesEditResponse:
    data = {
        "title": licenses_data.title,
        "description": licenses_data.description,
    }
    
    await LicensesRepository.edit_one(id, data)

    return SLicensesEditResponse

@licenses.delete(
    "/delete/{id}",
    summary="Create new licenses",
    response_model=SLicensesDeleteResponse,
    responses={
        status.HTTP_200_OK: {'model': SLicensesDeleteResponse}
    }
)
async def delete_licenses(id: int) -> SLicensesDeleteResponse:
    await LicensesRepository.delete(id=id)

    return SLicensesDeleteResponse
