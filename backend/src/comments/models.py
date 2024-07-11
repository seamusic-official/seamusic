from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

from src.auth.models import User
from src.beats.models import Beat
from src.beatpacks.models import Beatpack
import datetime
from src.database import Base
import os
from typing import List

class UserComment(Base):
    __tablename__ = "user_comments"

    description = Mapped[str] = mapped_column()
    
    to_whom_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    to_whom: Mapped["User"] = relationship("User")  

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship("User") 

class BeatComment(Base):
    __tablename__ = "beat_comments"

    description = Mapped[str] = mapped_column()
    
    beat_id: Mapped[int] = mapped_column(ForeignKey("beats.id"))
    beat: Mapped["Beat"] = relationship("Beat")  

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship("User")  

class BeatpackComment(Base):
    __tablename__ = "beatpack_comments"

    description = Mapped[str] = mapped_column()
    
    beatpack_id: Mapped[int] = mapped_column(ForeignKey("beatpacks.id"))
    beatpack: Mapped["Beatpack"] = relationship("Beatpack") 

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship("User")
    