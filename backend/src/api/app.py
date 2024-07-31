from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from fastapi_cache import FastAPICache
# from fastapi_cache.backends.redis import RedisBackend
from sqladmin import Admin, ModelView

from src.api.v1.router import v1
from src.core.database import engine
from src.models.auth import User, ProducerProfile, ArtistProfile
from src.models.beatpacks import Beatpack
from src.models.beats import Beat
from src.models.soundkits import Soundkit
from src.models.squads import Squad
from src.models.tags import Tag


class BeatsAdmin(ModelView, model=Beat):
    column_list = [Beat.id, Beat.title]


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.username]


class SquadAdmin(ModelView, model=Squad):
    column_list = [Squad.id, Squad.name]


class TagAdmin(ModelView, model=Tag):
    column_list = [Tag.id, Tag.name]


class SoundkitAdmin(ModelView, model=Soundkit):
    column_list = [Tag.id, Soundkit.name]


class ProducerProfileAdmin(ModelView, model=ProducerProfile):
    column_list = [ProducerProfile.id, ProducerProfile.user]


class ArtistProfileAdmin(ModelView, model=ArtistProfile):
    column_list = [ArtistProfile.id, ArtistProfile.user]


class BeatpackAdmin(ModelView, model=Beatpack):  # type: ignore
    column_list = [Beatpack.id, Beatpack.title]


@asynccontextmanager
async def lifespan(application: FastAPI):
    admin.add_view(SoundkitAdmin)
    admin.add_view(TagAdmin)
    admin.add_view(SquadAdmin)
    admin.add_view(BeatsAdmin)
    admin.add_view(BeatpackAdmin)
    admin.add_view(UserAdmin)
    admin.add_view(ProducerProfileAdmin)
    admin.add_view(ArtistProfileAdmin)

    application.include_router(v1)

    # redis = Redis(host='localhost', port=6379, decode_responses=True, encoding='utf8')
    # FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")

    yield

    # await redis.aclose()


app = FastAPI(
    title="SeaMusic",
    description="High-perfomance musical application",
    lifespan=lifespan,
)
admin = Admin(app, engine)

origins = ["http://127.0.0.1:5173", "http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,  # type: ignore
    allow_credentials=True,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)
