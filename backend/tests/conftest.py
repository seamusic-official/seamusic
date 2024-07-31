import pytest
from fastapi.testclient import TestClient
from httpx import Response
from sqlalchemy.ext.asyncio import create_async_engine

from src.auth.schemas import SRegisterUser, Role, SLoginUser, SUserLoginResponse
from src.config import settings
from src.database import Base
from src.main import app


engine_test = create_async_engine(settings.db.url, echo=True)

email = 'test_email@example.com'
password = 'test_password'


@pytest.fixture(scope='session')
def client() -> TestClient:
    return TestClient(app=app)


@pytest.fixture(autouse=True, scope='session')
def login(client: TestClient):
    register = SRegisterUser(
        username='test_username',
        password=password,
        email=email,
        roles=[Role.listener, Role.superuser, Role.moder, Role.producer, Role.listener],
        birthday=None,
        tags=['supertrap', 'newjazz', 'rage', 'hyperpop']
    )
    login = SLoginUser(email=email, password=password)
    client.post(url='/auth/register', json=register.model_dump())
    response: Response = client.post(url='/auth/login', json=login.model_dump())
    yield SUserLoginResponse(**response.json())


@pytest.fixture(autouse=True, scope='session')
async def prepare_database():
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
