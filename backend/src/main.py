from contextlib import asynccontextmanager

# import aioredis
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from fastapi_cache import FastAPICache
# from fastapi_cache.backends.redis import RedisBackend
from sqladmin import Admin, ModelView

from src.albums.router import albums
from src.auth.models import User, ProducerProfile, ArtistProfile
from src.auth.router import auth
from src.beatpacks.models import Beatpack
from src.beatpacks.router import beatpacks
from src.beats.models import Beat
from src.beats.router import beats
from src.comments.router import comments
from src.database import engine
from src.licenses.router import licenses
from src.messages.router import messages
from src.music.router import music
from src.soundkits.models import Soundkit
from src.soundkits.router import soundkits
from src.squads.models import Squad
from src.squads.router import squads
from src.subscriptions.router import subscription
from src.tags.models import Tag
from src.tags.router import tags
from src.tracks.router import tracks


class BeatsAdmin(ModelView, model=Beat):  # type: ignore
    column_list = [Beat.id, Beat.title]


class UserAdmin(ModelView, model=User):  # type: ignore
    column_list = [User.id, User.username]


class SquadAdmin(ModelView, model=Squad):  # type: ignore
    column_list = [Squad.id, Squad.name]


class TagAdmin(ModelView, model=Tag):  # type: ignore
    column_list = [Tag.id, Tag.name]


class SoundkitAdmin(ModelView, model=Soundkit):  # type: ignore
    column_list = [Tag.id, Soundkit.name]


class ProducerProfileAdmin(ModelView, model=ProducerProfile):  # type: ignore
    column_list = [ProducerProfile.id, ProducerProfile.user]


class ArtistProfileAdmin(ModelView, model=ArtistProfile):  # type: ignore
    column_list = [ArtistProfile.id, ArtistProfile.user]


class BeatpackAdmin(ModelView, model=Beatpack):  # type: ignore
    column_list = [Beatpack.id, Beatpack.title]


@asynccontextmanager
async def lifespan(application: FastAPI):

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

    admin.add_view(SoundkitAdmin)
    admin.add_view(TagAdmin)
    admin.add_view(SquadAdmin)
    admin.add_view(BeatsAdmin)
    admin.add_view(BeatpackAdmin)
    admin.add_view(UserAdmin)
    admin.add_view(ProducerProfileAdmin)
    admin.add_view(ArtistProfileAdmin)

    # redis = aioredis.from_url("redis://localhost:6379", encoding="utf8")
    # FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")

    yield


app = FastAPI(
    title="SeaMusic",
    description="High-perfomance musical application",
    lifespan=lifespan,
)
admin = Admin(app, engine)

origins = ["http://127.0.0.1:5173", "http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)
