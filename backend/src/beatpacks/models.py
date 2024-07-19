from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from sqlalchemy import Column
from sqlalchemy import Table
from sqlalchemy import ForeignKey
from sqlalchemy import Integer, DateTime, String

import datetime
from src.database import Base
from typing import List


beats_to_beatpacks_association_table = Table('beats_to_beatpacks_association_table', Base.metadata,
    Column('beat_id', Integer, ForeignKey('beats.id')),
    Column('beat_pack_id', Integer, ForeignKey('beatpacks.id'))
)

user_to_beatpacks_association_table = Table('user_to_beatpacks_association_table', Base.metadata,
    Column('beatpack_id', Integer, ForeignKey('beatpacks.id')),
    Column('user_id', Integer, ForeignKey('users.id'))
)

class Beatpack(Base):
    __tablename__ = "beatpacks"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)    
    user: Mapped[List["User"]] = relationship("User", secondary=user_to_beatpacks_association_table)
    beats: Mapped[List["Beat"]] = relationship("Beat", secondary=beats_to_beatpacks_association_table)

