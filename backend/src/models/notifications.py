from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

from src.core.database import CreatedAtOnlyMixin


class Base(DeclarativeBase):
    pass


class Notification(Base, CreatedAtOnlyMixin):
    __tablename__ = "notifications"

    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column()
