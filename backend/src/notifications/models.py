from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column

from src.database import CreatedAtOnlyMixin


Base = declarative_base()


class Notification(Base, CreatedAtOnlyMixin):
    __tablename__ = "notifications"

    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column()
