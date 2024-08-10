from sqlalchemy import Column, Table, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.database import Base


class ArtistProfileAlbumAssociation(Base):
    __tablename__ = "artist_profile_album_association"

    artist_profile_id: Mapped[int] = mapped_column(ForeignKey("artist_profiles.id"), primary_key=True)
    album_id: Mapped[int] = mapped_column(ForeignKey("albums.id"), primary_key=True)


class AlbumTrackAssociation(Base):
    __tablename__ = "album_track_association"

    album_id: Mapped[int] = mapped_column(ForeignKey("albums.id"), primary_key=True)
    track_id: Mapped[int] = mapped_column(ForeignKey("tracks.id"), primary_key=True)


class Album(Base):
    __tablename__ = "albums"

    name: Mapped[str] = mapped_column(nullable=False)
    picture_url: Mapped[str] = mapped_column(nullable=True)
    description: Mapped[str] = mapped_column(nullable=True)
    co_prod: Mapped[str] = mapped_column(nullable=True)
    
    type: Mapped[str] = mapped_column(nullable=True)

    artist_profiles: Mapped["ArtistProfile"] = relationship(
        secondary="artist_profile_album_association", back_populates="albums"
    )
    tracks: Mapped["Track"] = relationship(
        secondary="album_track_association", back_populates="albums"
    )

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship("User")
