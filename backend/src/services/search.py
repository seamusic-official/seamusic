from src.models.beats import Beat
from src.core.cruds import SQLAlchemyRepository


class BeatsRepository(SQLAlchemyRepository):
    model = Beat
