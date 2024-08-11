from dataclasses import dataclass

from src.repositories.base import SQLAlchemyRepository
from src.repositories.comments.base import BaseCommentsRepository


@dataclass
class CommentsRepository(SQLAlchemyRepository, BaseCommentsRepository):
    pass
