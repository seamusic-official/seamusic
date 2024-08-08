from src.core.cruds import SQLAlchemyRepository
from src.models.beats import Beat


class BeatsRepository(SQLAlchemyRepository):
    model = Beat
