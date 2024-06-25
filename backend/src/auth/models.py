from __future__ import annotations
from typing import List
from datetime import datetime
from src.database import Base
from src.beats.models import Beat, License, BeatPack, Playlist
from src.messages.models import Chat
from sqlalchemy import DateTime
from sqlalchemy import Column
from sqlalchemy import Table
from sqlalchemy import ForeignKey
from sqlalchemy import Integer

from sqlalchemy import ForeignKey
from sqlalchemy import event
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from src.beats.models import View,  Beat


class Tag(Base):
    __tablename__ = 'tags'

    title: Mapped[str] = mapped_column(nullable=False)
    
liked_users = Table(
    'liked_users', Base.metadata,
    Column('like_id', Integer, ForeignKey('likes.id')),
    Column('user_id', Integer, ForeignKey('users.id'))
)

# src/auth/models.py

from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, DateTime, String
from src.database import Base
from src.comments.models import Comment
from src.beats.models import Beat, View
from datetime import datetime

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False, default="Listener")
    picture_url = Column(String, nullable=True, default="https://img.favpng.com/22/0/21/computer-icons-user-profile-clip-art-png-favpng-MhMHJ0Fw21MJadYjpvDQbzu5S.jpg")
    is_active = Column(Boolean, nullable=True, default=False)
    birthday = Column(DateTime, nullable=False)
    registered_at = Column(DateTime, default=datetime.utcnow)

    artist_profile = relationship("ArtistProfile", back_populates="user", uselist=False)
    producer_profile = relationship("ProducerProfile", back_populates="user", uselist=False)
    comments = relationship('Comment', back_populates='author')
    views = relationship('View', back_populates='user')
    likes = relationship('Like', secondary=liked_users, back_populates='users')

class ArtistProfile(Base):
    __tablename__ = 'artist_profiles'

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="artist_profile")

class ProducerProfile(Base):
    __tablename__ = 'producer_profiles'

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="producer_profile")
