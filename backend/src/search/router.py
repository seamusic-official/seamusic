from src.search.services import searchRepository, BeatPacksRepository
from src.search.schemas import SBeatBase, SBeat, SBeatCreate, SBeatPackBase, SBeatPack, SBeatPackCreate
from src.auth.schemas import SUser
from src.search.utils import save_audio, save_image
from src.config import settings
from src.auth.dependencies import get_current_user
from fastapi import UploadFile, File, APIRouter, Depends
from fastapi.responses import FileResponse

search = APIRouter(
    prefix = "/search",
    tags = ["Search"]
)
