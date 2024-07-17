from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from redis import asyncio as aioredis
from sqladmin import Admin, ModelView 

from src.auth.router import auth
from src.auth.models import User, ProducerProfile, ArtistProfile
from src.comments.router import comments
from src.beats.router import beats
from src.beats.models import Beat

from src.music.router import music

from src.beatpacks.router import beatpacks
from src.beatpacks.models import Beatpack

from src.soundkits.router import soundkits
from src.soundkits.models import Soundkit

from src.albums.router import albums
from src.albums.models import Album

from src.tracks.router import tracks
from src.tracks.models import Track

from src.subscription.router import subscription
from src.subscription.models import TelegramAccount

from src.tags.router import tags
from src.tags.models import Tag

from src.licenses.router import licenses
from src.messages.router import messages

from src.squads.models import Squad
from src.squads.router import squads

from src.database import engine
from src.config import settings

app = FastAPI(
    title = "SeaMusic",
    description = "High-perfomance musical application",
)

app.include_router(auth)
app.include_router(licenses)
app.include_router(beats)
app.include_router(beatpacks)
app.include_router(tracks)
app.include_router(albums)
app.include_router(soundkits)
app.include_router(messages)
app.include_router(music)
app.include_router(subscription)
app.include_router(tags)
app.include_router(squads)
app.include_router(comments)



admin = Admin(app, engine)

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

class BeatpackAdmin(ModelView, model=Beatpack):
    column_list = [Beatpack.id, Beatpack.title]

admin.add_view(SoundkitAdmin)
admin.add_view(TagAdmin)
admin.add_view(SquadAdmin)
admin.add_view(BeatsAdmin)
admin.add_view(BeatpackAdmin)
admin.add_view(UserAdmin)
admin.add_view(ProducerProfileAdmin)
admin.add_view(ArtistProfileAdmin)

origins = [
    "http://127.0.0.1:5173", "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.on_event("startup")
# async def startup():
#     redis = aioredis.from_url("redis://localhost:6379", encoding="utf8")
#     FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
