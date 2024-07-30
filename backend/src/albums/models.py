from sqlalchemy import Column, Table, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.auth.models import ArtistProfile, User
from src.database import Base
from src.tracks.models import Track

artist_profile_album_association = Table(
    "artist_profile_album_association",
    Base.metadata,
    Column("artist_profile_id", Integer, ForeignKey("artist_profiles.id")),
    Column("album_id", Integer, ForeignKey("albums.id")),
)

album_track_association = Table(
    "album_track_association",
    Base.metadata,
    Column("album_id", Integer, ForeignKey("albums.id")),
    Column("track_id", Integer, ForeignKey("tracks.id")),
)


class Album(Base):
    __tablename__ = "albums"

    name: Mapped[str] = mapped_column(nullable=False)
    picture_url: Mapped[str] = mapped_column(nullable=True)
    description: Mapped[str] = mapped_column(nullable=True)
    co_prod: Mapped[str] = mapped_column(nullable=True)
    prod_by: Mapped[str] = mapped_column(nullable=True)
    type: Mapped[str] = mapped_column(nullable=True)

    artist_profiles: Mapped["ArtistProfile"] = relationship(
        secondary=artist_profile_album_association, back_populates="albums"
    )
    tracks: Mapped["Track"] = relationship(
        secondary=album_track_association, back_populates="albums"
    )

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship("User")
