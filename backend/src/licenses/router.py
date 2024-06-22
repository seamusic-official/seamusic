from src.licenses.services import LicensesRepository
from src.auth.schemas import SUser
from src.auth.dependencies import get_current_user
from src.licenses.schemas import SLicenseBase

from fastapi import UploadFile, File, APIRouter, Depends
from fastapi.responses import FileResponse


licenses = APIRouter(
    prefix = "/licenses",
    tags = ["Licenses"]
)

@licenses.post("/my", summary="Packs by current user")
async def get_user_licenses(user: SUser = Depends(get_current_user)):
    response = await LicensesRepository.find_all(owner=user)
    return response

@licenses.get("/all", summary="Create new licenses")
async def all_licenses():
    return await LicensesRepository.find_all()

@licenses.get("/{id}", summary="Create new licenses")
async def get_one(id: int):
    return await LicensesRepository.find_one_by_id(id)

@licenses.post("/beatbacks/add", summary="Add a file for new beat")
async def add_licenses(data: SLicenseBase, user: SUser = Depends(get_current_user)):
    data = {
        "title": data.title,
        "description": data.description,
        "licenses": data.licenses
    }
    
    response = await LicensesRepository.add_one(data)
    return response

@licenses.put("/update/{id}", summary="Create new licenses")
async def update_licenses(id: int, licenses_data: SLicenseBase):
    data = {
        "title": licenses_data.title,
        "description": licenses_data.description,
    }
    
    await LicensesRepository.edit_one(id, data)
    return data

@licenses.delete("/delete/{id}", summary="Create new licenses")
async def delete_licenses(id: int):
    return await LicensesRepository.delete(id=id)
