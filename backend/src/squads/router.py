from fastapi import UploadFile, File, APIRouter, Depends

squads = APIRouter(
    prefix = "/squads",
    tags = ["Squads"]
)

