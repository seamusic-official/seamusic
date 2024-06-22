from src.licenses.models import License
from src.services import SQLAlchemyRepository
from src.config import settings

    
class LicensesRepository(SQLAlchemyRepository):
    model = License
    