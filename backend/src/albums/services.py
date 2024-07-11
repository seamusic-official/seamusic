from src.albums.models import Album
from src.services import SQLAlchemyRepository


class AlbumsRepository(SQLAlchemyRepository):
    model = Album
    