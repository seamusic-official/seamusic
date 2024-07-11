from src.auth.models import User, ProducerProfile, ArtistProfile
from src.services import SQLAlchemyRepository
from src.database import async_session_maker
from sqlalchemy import insert, select, update, delete, desc

class UsersDAO(SQLAlchemyRepository):
    model = User

class ProducerDAO(SQLAlchemyRepository):
    model = ProducerProfile

class ArtistDAO(SQLAlchemyRepository):
    model = ArtistProfile

