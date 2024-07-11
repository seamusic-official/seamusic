from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from sqlalchemy import Column
from sqlalchemy import Table
from sqlalchemy import ForeignKey
from sqlalchemy import Integer, DateTime

import datetime
from src.database import Base
import os
from typing import List


class Track(Base):
    __tablename__ = "tracks"
    
    title: Mapped[str] = mapped_column(nullable=False)
    picture: Mapped[str] = mapped_column(nullable=True)
    description: Mapped[str] = mapped_column(nullable=True)
    file_path: Mapped[str] = mapped_column(nullable=False)
    co_prod: Mapped[str] = mapped_column(nullable=True)
    prod_by: Mapped[str] = mapped_column(nullable=True)
    type: Mapped[str] = mapped_column(nullable=True)
    
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship("User")  # Указываем связь с таблицей User