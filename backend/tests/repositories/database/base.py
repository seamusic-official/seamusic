from abc import ABC
from dataclasses import dataclass

from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database import sessionmaker


@dataclass
class BaseDatabaseRepository(ABC):
    pass


@dataclass
class SQLAlchemyRepository(BaseDatabaseRepository):
    @property
    async def session(self) -> AsyncSession:
        async with sessionmaker() as session:
            yield session
            await session.commit()
