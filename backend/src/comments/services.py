from src.beats.models import Beat, BeatPack, Playlist, License
from src.services import SQLAlchemyRepository


class BeatsRepository(SQLAlchemyRepository):
    model = Beat
    