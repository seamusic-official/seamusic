from src.models.licenses import License
from src.services import SQLAlchemyRepository


class LicensesRepository(SQLAlchemyRepository):
    model = License
