from dataclasses import dataclass

from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database import session_factory


@dataclass
class SQLAlchemyRepository:
    @property
    async def _session(self) -> AsyncSession:
        async with session_factory() as session:
            yield session
            await session.commit()
