from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from sqlalchemy import Column
from sqlalchemy import Table
from sqlalchemy import ForeignKey
from sqlalchemy import Integer, DateTime

import datetime
from src.database import Base
import os
from typing import List
from src.auth import User
from src.soundkits.models import Soundkit
from src.beats.models import Beat

class Comment(Base):

    __tablename__ = 'comment'

    id = Mapped[int] = mapped_column(index = True, primary_key = True)
    comment : Mapped[str] = mapped_column(nullable = False)
    date_pub : Mapped[DateTime] = mapped_column(default = datetime.utc.now())
    
    author_id : Mapped[int] = mapped_column(ForeignKey('users.id'))
    author : Mapped['User'] = relationship(back_populates='comment_author')

    beat_id : Mapped[int] = mapped_column(ForeignKey("beats.id"))    
    beat : Mapped['Beat']  = relationship(back_populates = 'comment') 
