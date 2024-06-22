from src.soundkits.services import SoundkitRepository
from src.soundkits.schemas import SSoundkit
from src.soundkits.utils import unique_filename
from src.services import MediaRepository
from src.auth.schemas import SUser
from src.config import settings
from src.auth.dependencies import get_current_user

from fastapi import UploadFile, File, APIRouter, Depends
from typing import List

soundkits = APIRouter(
    prefix = "/soundkits",
    tags = ["Sound-kits"]
)

@soundkits.get("/all", summary="All soundkits")
async def get_all_soundkits() -> List[SSoundkit]:
    return await SoundkitRepository.find_all()