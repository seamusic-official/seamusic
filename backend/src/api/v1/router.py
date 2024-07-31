from contextlib import asynccontextmanager

from fastapi import APIRouter

from src.api.v1.albums import albums
from src.api.v1.auth import auth
from src.api.v1.beatpacks import beatpacks
from src.api.v1.beats import beats
from src.api.v1.comments import comments
from src.api.v1.licenses import licenses
from src.api.v1.messages import messages
from src.api.v1.music import music
from src.api.v1.soundkits import soundkits
from src.api.v1.squads import squads
from src.api.v1.subscriptions import subscription
from src.api.v1.tags import tags
from src.api.v1.tracks import tracks


@asynccontextmanager
async def lifespan(application: APIRouter):
    application.include_router(auth)
    application.include_router(licenses)
    application.include_router(beats)
    application.include_router(beatpacks)
    application.include_router(tracks)
    application.include_router(albums)
    application.include_router(soundkits)
    application.include_router(messages)
    application.include_router(music)
    application.include_router(subscription)
    application.include_router(tags)
    application.include_router(squads)
    application.include_router(comments)
    yield


v1 = APIRouter(prefix='/v1', lifespan=lifespan)
