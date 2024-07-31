from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.auth import User
from src.core.database import Base


class View(Base):
    __tablename__ = "views"

    beats_id: Mapped[int] = mapped_column(Integer, ForeignKey("beats.id"), index=True)
    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.id"), index=True, nullable=True
    )

    user: Mapped["User"] = relationship("User", back_populates="views")
