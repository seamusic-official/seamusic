from typing import List

from sqlalchemy import Integer, String, Table, ForeignKey, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.auth import User
from src.models.beats import Beat
from src.core.database import Base


class BeatToBeatpack(Base):
    __tablename__ = "beats_to_beatpacks_association_table"

    beat_id: Mapped[int] = mapped_column(Integer, ForeignKey("beats.id"), primary_key=True)
    beatpack_id: Mapped[int] = mapped_column(Integer, ForeignKey("beatpacks.id"), primary_key=True)


class UserToBeatpack(Base):
    __tablename__ = "user_to_beatpacks_association_table"

    beatpack_id: Mapped[int] = mapped_column(Integer, ForeignKey("beatpacks.id"), primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), primary_key=True)


class Beatpack(Base):
    __tablename__ = "beatpacks"

    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)

    users: Mapped[List["User"]] = relationship(
        "User", secondary="user_to_beatpacks_association_table"
    )
    beats: Mapped[List["Beat"]] = relationship(
        "Beat", secondary="beats_to_beatpacks_association_table"
    )
