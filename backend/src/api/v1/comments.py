from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from src.core.database import get_async_session
from src.models.beats import Beat
from src.models.comments import BaseComment
from src.schemas.comments import (
    CommentCreate,
    CommentResponse,
    CommentUpdate,
    SCommentDeleteResponse,
    CommentUpdateResponse,
)
from src.utils.auth import get_current_user


comments = APIRouter(prefix="/comments", tags=["Comments"])
