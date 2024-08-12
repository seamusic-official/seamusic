from dataclasses import dataclass

import aiohttp
import requests


@dataclass
class APIRepository:
    pass


@dataclass
class RequestsRepository(APIRepository):
    @property
    def session(self) -> requests.Session:
        return requests.session()


@dataclass
class AiohttpRepositpry(APIRepository):
    @property
    async def session(self):
        async with aiohttp.ClientSession() as session_:
            yield session_
