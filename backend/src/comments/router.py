from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from sqlalchemy.orm import joinedload
from src.beatpacks.models import Beatpack
from src.soundkits.models import Soundkit

from src.auth.schemas import SUser
from src.auth.dependencies import get_current_user
from .models import BaseComment
from .schemas import CommentCreate, CommentResponse, CommentUpdate, SCommentDeleteResponse, CommentUpdateResponse
from src.database import get_async_session
from src.beats.models import Beat


comments = APIRouter(prefix="/comments", tags=["Comments"])


@comments.post(
    "/create-comment-for-beat/{beat_id}/",
    summary='create comment for beat'
)
async def create_comment_for_beat(
    beat_id: int,
    current_user: SUser = Depends(get_current_user),
):
    return