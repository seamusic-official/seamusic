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
 


class Message(Base):
    __tablename__ = 'messages'
 
