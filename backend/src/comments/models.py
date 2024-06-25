from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Column, ForeignKey, Integer, DateTime
import datetime
from src.database import Base
from typing import List

class Comment(Base):
    __tablename__ = 'comments'

    id: Mapped[int] = mapped_column(index=True, primary_key=True)
    comment: Mapped[str] = mapped_column(nullable=False)
    date_pub = Column(DateTime, default=datetime.datetime.utcnow)
    
    author_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    author: Mapped['User'] = relationship('User', back_populates='comments')

    beat_id: Mapped[int] = mapped_column(ForeignKey("beats.id"))    
    beat: Mapped['Beat'] = relationship('Beat', back_populates='comments')
