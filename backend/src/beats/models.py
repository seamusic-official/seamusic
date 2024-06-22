from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from sqlalchemy import Column
from sqlalchemy import Table, func
from sqlalchemy import ForeignKey
from sqlalchemy import Integer, DateTime

import datetime
from src.database import Base
import os
from typing import List
from src.comments.models import Comment
from src.auth.models import User


STATIC_FILES_PATH = os.path.join(os.path.dirname(__file__), '..', 'STATICFILES')


chosen = Table(
    'user_chosen', Base.metadata,
    Column('user_id', ForeignKey('users.id'), primary_key = True),
    Column('beat_id', ForeignKey('beats.id'), primary_key = True)

)


class Like(Base):
    __tablename__ = "likes"
    
    beat_id: Mapped[int] = mapped_column(ForeignKey("beats.id"))

class Beat(Base):
    __tablename__ = "beats"
    
    title: Mapped[str] = mapped_column(nullable=False)
    picture: Mapped[str] = mapped_column(nullable=True)
    description: Mapped[str] = mapped_column(nullable=True)
    file_path: Mapped[str] = mapped_column(nullable=False)
    co_prod: Mapped[str] = mapped_column(nullable=True)
    prod_by: Mapped[str] = mapped_column(nullable=True)
    
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship("User")  # Указываем связь с таблицей User
    comment: Mapped['Comment'] = relationship(back_populates = 'beat')

    view_count: Mapped[int] = mapped_column()
    views: Mapped['View'] = mapped_column(back_populates = 'beat')



beats_to_beatpacks_association_table = Table('beats_to_beatpacks_association_table', Base.metadata,
    Column('beat_id', Integer, ForeignKey('beats.id')),
    Column('beat_pack_id', Integer, ForeignKey('beatpacks.id'))
)
user_to_beatpacks_association_table = Table('user_to_beatpacks_association_table', Base.metadata,
    Column('beatpack_id', Integer, ForeignKey('beatpacks.id')),
    Column('user_id', Integer, ForeignKey('users.id'))
)
class BeatPack(Base):
    __tablename__ = "beatpacks"
    
    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)    
    
    user: Mapped["User"] = relationship("User", secondary=user_to_beatpacks_association_table)
    beats: Mapped["Beat"] = relationship("Beat", secondary=beats_to_beatpacks_association_table)

        
user_to_licenses_association = Table('user_to_licenses_association', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('license_id', Integer, ForeignKey('licenses.id'))
)

class License(Base):
    __tablename__ = "licenses"
    
    title: Mapped[str] = mapped_column(nullable=False)
    price: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)

    user: Mapped["User"] = relationship("User", secondary=user_to_licenses_association)

    
class Playlist(Base):
    __tablename__ = 'playlists'

    title: Mapped[str] = mapped_column()
    
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship()


class View(Base):
    __tablename__ = 'views'

    id : Mapped[int] = mapped_column(primary_key=True, index=True)
    beat_id : Mapped[int] = mapped_column(ForeignKey('beats.id'), index=True)
    user_id = Column(Integer, ForeignKey('users.id'), index=True, nullable=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

    beat : Mapped['Beat'] = mapped_column(back_populates="views")
    user : Mapped['User'] = mapped_column(back_populates="views")