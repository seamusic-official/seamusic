from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from sqlalchemy import Column
from sqlalchemy import Table
from sqlalchemy import ForeignKey
from sqlalchemy import Integer

import datetime
from src.database import Base
import os

class Chat(Base):
    __tablename__ = 'chats'
 
    id: Mapped[int] = mapped_column(primary_key=True)

class Message(Base):
    __tablename__ = 'messages'
 
    id: Mapped[int] = mapped_column(primary_key=True)
