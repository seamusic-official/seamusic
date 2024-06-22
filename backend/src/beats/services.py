from src.beats.models import Beat
from src.services import SQLAlchemyRepository

class BeatsRepository(SQLAlchemyRepository):
    model = Beat