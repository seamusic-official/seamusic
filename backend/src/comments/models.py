from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Integer, String, DateTime

from src.auth.models import User
from src.beats.models import Beat
from src.beatpacks.models import Beatpack
import datetime
from src.database import Base
import os
from typing import List




class BaseComment(Base):
    __tablename__ = 'base_comment'

    """

    тут есть всё я сократил код место того что бы написать
    несколько классов можно написить одну 
    поля : Comment: сообшение, comment_author: создатель коментарие, comment_author_id: id создателя коментарие
    beat_id: Id бита, beat_pack_id: id бит пека 
    и так дал


    """

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    comment: Mapped[str] = mapped_column(String, nullable=False)
    comment_creator_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))
    comment_author: Mapped['User'] = relationship('User')
    beat_id: Mapped[int] = mapped_column(Integer, ForeignKey('beats.id'))
    beat_pack_id: Mapped[int] = mapped_column(Integer, ForeignKey('beatpacks.id'))
    soundkit_id: Mapped[int] = mapped_column(Integer, ForeignKey('soundkits.id'))
