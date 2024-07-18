from sqladmin import Admin, ModelView

from src.auth.models import User, ProducerProfile, ArtistProfile
from src.beatpacks.models import Beatpack
from src.beats.models import Beat

from src.soundkits.models import Soundkit
from src.squads.models import Squad
from src.tags.models import Tag


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
