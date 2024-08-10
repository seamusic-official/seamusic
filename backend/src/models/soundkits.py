from sqlalchemy import Column, Table, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.auth import User
from src.core.database import Base


class UserToSoundkit(Base):
    __tablename__ = "user_to_soundkits_association_table"

    soundkit_id: Mapped[int] = mapped_column(Integer, ForeignKey("soundkits.id"), primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), primary_key=True)


class Soundkit(Base):
    __tablename__ = "soundkits"

    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    picture_url: Mapped[str] = mapped_column(nullable=True)
    file_url: Mapped[str] = mapped_column(nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship("User", secondary="user_to_soundkits_association_table")

