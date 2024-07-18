from sqlalchemy import String, Integer, ForeignKey, func, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database import Base
from datetime import datetime


class View(Base):
    __tablename__ = 'view'

    id: Mapped[int] = mapped_column(Integer, index = True, primary_key = True, autoincrement=True, nullable  = True)

    beats_id: Mapped[int] = mapped_column(Integer, ForeignKey('beats.id'), index=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'), index=True, nullable=True)

    user: Mapped["User"] = relationship("User", back_populates="views")