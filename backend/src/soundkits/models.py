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

from src.auth.models import User

class Soundkit(Base):
    __tablename__ = "soundkits"
    
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    picture_url: Mapped[str] = mapped_column(nullable=True)
    file_url: Mapped[str] = mapped_column(nullable=False)
    
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship("User") 

user_to_soundkits_association_table = Table('user_to_soundkits_association_table', Base.metadata,
    Column('soundkit_id', Integer, ForeignKey('soundkits.id')),
    Column('user_id', Integer, ForeignKey('users.id'))
)