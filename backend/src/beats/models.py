# src/beats/models.py

from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String, func, DateTime
from src.database import Base
from src.auth.models import User
from src.comments.models import Comment
from src.auth.models import User

class Beat(Base):
    __tablename__ = "beats"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    picture = Column(String, nullable=True)
    description = Column(String, nullable=True)
    file_path = Column(String, nullable=False)
    co_prod = Column(String, nullable=True)
    prod_by = Column(String, nullable=True)
    
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="beats")
    comments = relationship('Comment', back_populates='beat')
    views = relationship('View', back_populates='beat') 

class View(Base):
    __tablename__ = 'views'

    id = Column(Integer, primary_key=True, index=True)
    beat_id = Column(Integer, ForeignKey('beats.id'), index=True)
    user_id = Column(Integer, ForeignKey('users.id'), index=True, nullable=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

    beat = relationship('Beat', back_populates='views') 
    user = relationship('User', back_populates='views')


class Like(Base):
    __tablename__ = "likes"
    
    id = Column(Integer, primary_key=True, index=True)
    beat_id = Column(Integer, ForeignKey("beats.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    
    user = relationship("User", back_populates="likes")
    beat = relationship("Beat", back_populates="likes")
