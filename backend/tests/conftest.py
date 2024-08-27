import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from src.api.app import create_app
from src.core.config import settings
from src.core.database import Base


engine_test = create_async_engine(url=settings.db.url, echo=True)
sessionmaker = async_sessionmaker(engine_test, expire_on_commit=False)

@pytest.fixture(scope='session')
def client() -> TestClient:
    return TestClient(app=create_app())

@pytest.fixture(autouse=True, scope='session')
async def prepare_database():
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)