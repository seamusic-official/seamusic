from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Iterable

from src.models.licenses import License


@dataclass
class BaseLicensesRepository(ABC):
    @abstractmethod
    async def get_user_licenses(self, user_id: int, **filter_by) -> Iterable[License]:
        ...

    @abstractmethod
    async def get_all_licenses(self) -> Iterable[License]:
        ...

    @abstractmethod
    async def get_license_by_id(self, license_id: int) -> License | None:
        ...

    @abstractmethod
    async def add_license(self, license_: License) -> None:
        ...

    @abstractmethod
    async def update_license(self, license_: License) -> None:
        ...

    @abstractmethod
    async def delete_license(self, license_id: int, user_id: int) -> None:
        ...
