from typing import List

from sqlalchemy import Integer, String, Table, ForeignKey, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.database import Base
from src.models.auth import User
from src.models.beats import Beat

beats_to_beatpacks_association_table = Table(
    "beats_to_beatpacks_association_table",
    Base.metadata,
    Column("beat_id", Integer, ForeignKey("beats.id")),
    Column("beat_pack_id", Integer, ForeignKey("beatpacks.id")),
)

user_to_beatpacks_association_table = Table(
    "user_to_beatpacks_association_table",
    Base.metadata,
    Column("beatpack_id", Integer, ForeignKey("beatpacks.id")),
    Column("user_id", Integer, ForeignKey("users.id")),
)


class Beatpack(Base):
    __tablename__ = "beatpacks"

    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)

    users: Mapped[List["User"]] = relationship(
        "User", secondary=user_to_beatpacks_association_table
    )
    beats: Mapped[List["Beat"]] = relationship(
        "Beat", secondary=beats_to_beatpacks_association_table
    )
