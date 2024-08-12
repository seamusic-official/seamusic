from abc import ABC
from dataclasses import dataclass


@dataclass
class BaseUsersRepository(ABC):
    ...


@dataclass
class BaseArtistsRepository(ABC):
    ...


@dataclass
class BaseProducersRepository(ABC):
    ...
