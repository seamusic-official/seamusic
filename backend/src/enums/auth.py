from enum import Enum


class Role(str, Enum):
    superuser = "superuser"
    moder = "moder"
    artist = "artist"
    producer = "producer"
    listener = "listener"
