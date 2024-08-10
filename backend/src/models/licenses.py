from sqlalchemy import Column, Table, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.database import Base


class UserToLicense(Base):
    __tablename__ = "user_to_licenses_association"

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), primary_key=True)
    license_id: Mapped[int] = mapped_column(Integer, ForeignKey("licenses.id"), primary_key=True)


class License(Base):
    __tablename__ = "licenses"

    title: Mapped[str] = mapped_column(nullable=False)
    price: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    picture_url: Mapped[str] = mapped_column(nullable=True)

    user: Mapped["User"] = relationship("User", secondary="user_to_licenses_association")
