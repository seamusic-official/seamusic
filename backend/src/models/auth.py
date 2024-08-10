from datetime import datetime, UTC
from typing import List

from sqlalchemy import DateTime, Column, Table, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.albums import Album, ArtistProfileAlbumAssociation
from src.core.database import Base
from src.models.squads import (
    Squad,
    squad_producer_profile_association,
    squad_artist_profile_association,
)
from src.models.tags import (
    Tag,
    artist_tags_association,
    producer_tags_association,
    listener_tags_association,
)
from src.models.tracks import Track, artist_profile_track_association
from src.enums.auth import Role, SystemRole


class User(Base):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    picture_url: Mapped[str] = mapped_column(
        nullable=True,
        default="https://img.favpng.com/22/0/21/computer-icons-user-profile-clip-art-png-favpng-MhMHJ0Fw21MJadYjpvDQbzu5S.jpg",
    )
    birthday: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    artist_profile_id: Mapped[int] = mapped_column(
        ForeignKey("artist_profiles.id"), nullable=True
    )
    producer_profile_id: Mapped[int] = mapped_column(
        ForeignKey("producer_profiles.id"), nullable=True
    )

    artist_profile: Mapped["ArtistProfile"] = relationship(back_populates="user")
    producer_profile: Mapped["ProducerProfile"] = relationship(back_populates="user")
    roles: Mapped[List["Role"]] = relationship(
        secondary="user_to_roles_association", back_populates="users"
    )
    system_roles: Mapped[List["SystemRole"]] = relationship(
        secondary="user_to_system_roles_association", back_populates="users"
    )
    tags: Mapped[List["Tag"]] = relationship(
        secondary=listener_tags_association, back_populates="listener_profiles"
    )
    squads: Mapped["Squad"] = relationship("Squad", overlaps="user")


class ArtistProfile(Base):
    __tablename__ = "artist_profiles"

    description: Mapped[str] = mapped_column()

    tracks: Mapped[List["Track"]] = relationship(
        secondary=artist_profile_track_association, back_populates="artist_profiles"
    )
    albums: Mapped[List["Album"]] = relationship(
        secondary="ArtistProfileAlbumAssociation", back_populates="artist_profiles"
    )
    squads: Mapped[List["Squad"]] = relationship(
        secondary=squad_artist_profile_association, back_populates="artist_profiles"
    )
    tags: Mapped[List["Tag"]] = relationship(
        secondary=artist_tags_association, back_populates="artist_profiles"
    )
    user: Mapped["User"] = relationship("User")


class ProducerProfile(Base):
    __tablename__ = "producer_profiles"

    description: Mapped[str] = mapped_column()

    user: Mapped["User"] = relationship("User")
    tags: Mapped[List["Tag"]] = relationship(
        secondary="producer_tags_association", back_populates="producer_profiles"
    )
    squads: Mapped[List["Squad"]] = relationship(
        secondary="squad_producer_profile_association", back_populates="producer_profiles"
    )
