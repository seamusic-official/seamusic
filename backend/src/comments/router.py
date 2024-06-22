from src.beats.services import BeatsRepository, BeatPacksRepository
from src.beats.schemas import SBeatBase, SBeat, SBeatCreate, SBeatPackBase, SBeatPack, SBeatPackCreate
from src.auth.schemas import SUser
from src.beats.utils import save_audio, save_image
from src.config import settings
from src.auth.dependencies import get_current_user
from fastapi import UploadFile, File, APIRouter, Depends, Form, Session, Depends, HTTPException
from fastapi.responses import FileResponse
from .schemas import CommentResponse
from .models import Comment
from src.database import get_db
from src.beats.models  import Beat
from datetime import datetime

beats = APIRouter(
    prefix = "/comments",
    tags = ["Comments"]
)



@beats.post('/', response_models = CommentResponse)
async def create_comment(

    beat_id: int,
    db: Session = Depends(get_db),
    current_user: SUser = Depends(get_current_user),
    comment: str = Form(...),

):

    beat_obj = db.query(Beat).filter(Beat.id == beat_id).first()

    if beat_obj:

        new_comment_obj = Comment(
            comment = comment,
            date_pub = datetime.utcnow(),
            beat_id = beat_obj,
            author_id = current_user.id,

        )


        return new_comment_obj
    
    raise HTTPException(detail = 'Beat Not Found', status_code = 404)


    

@router.get('/get-beat-comments/{id}/', response_model = CommentResponse)
async def get_comments(

    beat_id: int,
    db: Session = Depends(get_db),
    current_user: SUser = Depends(get_current_user),

):
    

    beat_objects = db.query(Beat).filter(Beat.id == beat_id).first()

    if not beat_objects:
        raise HTTPException(detail = 'Beat Not found', status_code = 404)
    

    comments  = db.query(Comment).filter(Comment.beat_id == beat_id).all()


    if comments:

        response = CommentResponse(
            id = comments.id,
            author = str(comments.author.username),
            author_id = comments.author_id,
            comment = comments.comment,
            date_pub = comments.date_pub

        )

        return response
    
    raise HTTPException(detail = f'Comment not found', status_code = 404)



@router.delete('delete-comments/{id}/')
async def delete_comment(

    comment_id: int,
    db: Session = Depends(get_db),
    current_user: SUser = Depends(get_current_user),
    
):
    
    comment = db.query(Comment.id).filter(Comment.id == comment_id).first()

    if not comment:
        raise HTTPException(detail = f'Comment with id {comment_id} Not found', status_code = 404)
    

    if comment.author_id == current_user.id:

        db.delete(comment)
        db.commit()

        return f'Comment Deleted Succsesfully'
