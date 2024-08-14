from dataclasses import dataclass

from src.repositories.api.base import BaseAPIRepository
from src.repositories.database.base import BaseDatabaseRepository
from src.repositories.media.base import BaseMediaRepository


@dataclass
class Repositories:
    database: BaseDatabaseRepository | None
    media: BaseMediaRepository | None
    api: BaseAPIRepository | None
