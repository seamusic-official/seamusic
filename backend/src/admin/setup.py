from sqladmin import Admin

from admin.views import SoundkitAdmin, TagAdmin, SquadAdmin, BeatsAdmin, BeatpackAdmin, UserAdmin, ProducerProfileAdmin, \
    ArtistProfileAdmin
from database import engine


def setup_admin(app):
    admin = Admin(app, engine)
    admin.add_view(SoundkitAdmin)
    admin.add_view(TagAdmin)
    admin.add_view(SquadAdmin)
    admin.add_view(BeatsAdmin)
    admin.add_view(BeatpackAdmin)
    admin.add_view(UserAdmin)
    admin.add_view(ProducerProfileAdmin)
    admin.add_view(ArtistProfileAdmin)
