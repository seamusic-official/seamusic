from src.services import SQLAlchemyRepository
from src.tracks.models import Track


class TracksRepository(SQLAlchemyRepository):
    model = Track
