from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from src.config import settings

engine = create_async_engine(
    settings.db.url,
    echo=True
)

async_session_maker = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

class Base(DeclarativeBase):
    __abstract__ = True

    def __repr__(self):
        values = ', '.join(f"{col.name}={getattr(self, col.name)}" for col in self.__table__.columns[:6])
        return f"<{self.__class__.__name__}({values})>"