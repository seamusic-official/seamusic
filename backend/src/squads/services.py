from src.services import SQLAlchemyRepository
from src.squads.models import Squad


class SquadRepository(SQLAlchemyRepository):
    model = Squad
