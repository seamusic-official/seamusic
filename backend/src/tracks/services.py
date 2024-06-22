from src.tracks.models import Track
from src.services import SQLAlchemyRepository


class TracksRepository(SQLAlchemyRepository):
    model = Track
    