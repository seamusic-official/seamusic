from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from sqlalchemy import Column
from sqlalchemy import Table
from sqlalchemy import ForeignKey
from sqlalchemy import Integer, DateTime
from src.albums.models import album_track_association

import datetime
from src.database import Base
import os
from typing import List

artist_profile_track_association = Table(
    'artist_profile_track_association',
    Base.metadata,
    Column('artist_profile_id', Integer, ForeignKey('artist_profiles.id')),
    Column('track_id', Integer, ForeignKey('tracks.id'))
)


class Track(Base):
    __tablename__ = "tracks"
    
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    picture_url: Mapped[str] = mapped_column(nullable=True)
    file_url: Mapped[str] = mapped_column(nullable=False)
    co_prod: Mapped[str] = mapped_column(nullable=True)
    prod_by: Mapped[str] = mapped_column(nullable=True)
    type: Mapped[str] = mapped_column(nullable=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    
    artist_profiles: Mapped["ArtistProfile"] = relationship(secondary=artist_profile_track_association, back_populates="tracks")
    albums: Mapped["Album"] = relationship(secondary=album_track_association, back_populates="tracks")
    user: Mapped["User"] = relationship("User")  # Указываем связь с таблицей User