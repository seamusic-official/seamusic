from src.beats.services import BeatsRepository, BeatPacksRepository
from src.beats.schemas import SBeatBase, SBeat, SBeatCreate, SBeatPackBase, SBeatPack, SBeatPackCreate
from src.auth.schemas import SUser
from src.beats.utils import save_audio, save_image
from src.config import settings
from src.auth.dependencies import get_current_user
from fastapi import UploadFile, File, APIRouter, Depends, Form
from fastapi.responses import FileResponse
from .schemas import CommentResponse
from .models import Comment
from src.database import Base

beats = APIRouter(
    prefix = "/comments",
    tags = ["Comments"]
)



@beats.post('/', response_models = CommentResponse)
async def create_comment(

    db: Base,
    content_id: int,
    current_user: SUser = Depends(get_current_user),
    comment: str = Form(...),

):

    comment = db.query(Comment).filter()
    