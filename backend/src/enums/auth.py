from enum import Enum


class Role(str, Enum):
    artist = "artist"
    producer = "producer"
    listener = "listener"


class SystemRole(str, Enum):
    superuser = "superuser"
    moder = "moder"
