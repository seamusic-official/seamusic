from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from sqlalchemy import Column
from sqlalchemy import Table
from sqlalchemy import ForeignKey
from sqlalchemy import Integer

from src.database import Base

user_to_licenses_association = Table('user_to_licenses_association', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('license_id', Integer, ForeignKey('licenses.id')),
)
    
class License(Base):
    __tablename__ = "licenses"
    
    title: Mapped[str] = mapped_column(nullable=False)
    price: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    picture_url: Mapped[str] = mapped_column(nullable=True)

    user: Mapped["User"] = relationship("User", secondary=user_to_licenses_association)

