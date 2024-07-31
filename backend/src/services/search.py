from src.models.beats import Beat
from src.services import SQLAlchemyRepository


class BeatsRepository(SQLAlchemyRepository):
    model = Beat
