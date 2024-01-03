from services import SQLAlchemyRepository
from music.models import Music


class MusicRepository(SQLAlchemyRepository):
    model = Music
    