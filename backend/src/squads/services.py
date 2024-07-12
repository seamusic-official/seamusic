from src.squads.models import Squad
from src.services import SQLAlchemyRepository


class SquadRepository(SQLAlchemyRepository):
    model = Squad
    