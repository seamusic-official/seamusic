from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column, Integer, ForeignKey, DateTime
from datetime import datetime
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from src.database import CreatedAtOnlyMixin

Base = declarative_base()

class Notification(Base, CreatedAtOnlyMixin):
    __tablename__ = "notifications"

    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column()