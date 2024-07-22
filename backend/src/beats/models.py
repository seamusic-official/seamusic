from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from sqlalchemy import ForeignKey

from src.database import Base


class Like(Base):
    __tablename__ = "likes"
    
    beat_id: Mapped[int] = mapped_column(ForeignKey("beats.id"))

class Beat(Base):
    __tablename__ = "beats"
    
    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    picture_url: Mapped[str] = mapped_column(nullable=True)
    file_url: Mapped[str] = mapped_column(nullable=False)
    co_prod: Mapped[str] = mapped_column(nullable=True)
    prod_by: Mapped[str] = mapped_column(nullable=True)
    type: Mapped[str] = mapped_column(nullable=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship("User") 
    view_count: Mapped[int] = mapped_column(Integer, default = 0)