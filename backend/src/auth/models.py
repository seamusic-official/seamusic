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



class Tag(Base):
    __tablename__ = 'tags'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    
liked_users = Table(
    'liked_users', Base.metadata,
    Column('like_id', Integer, ForeignKey('likes.id')),
    Column('user_id', Integer, ForeignKey('users.id'))
)

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    role: Mapped[str] = mapped_column(nullable=False, default="Listener")
    
    birthday: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    registered_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    artist_profile_id: Mapped[int] = mapped_column(ForeignKey("artist_profiles.id"), nullable=True)
    artist_profile: Mapped["ArtistProfile"] = relationship(back_populates="user")
    producer_profile_id: Mapped[int] = mapped_column(ForeignKey("producer_profiles.id"), nullable=True)
    producer_profile: Mapped["ProducerProfile"] = relationship(back_populates="user")

    likes = relationship("Like", secondary=liked_users)

class ArtistProfile(Base):
    __tablename__ = 'artist_profiles'

    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column()

    user: Mapped["User"] = relationship("User")

class ProducerProfile(Base):
    __tablename__ = 'producer_profiles'

    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column()
    
    user: Mapped["User"] = relationship("User")
