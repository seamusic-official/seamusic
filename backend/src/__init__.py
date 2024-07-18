"""Не удаляй этот код, поскольку он используется при создании миграций в alembic.
Сюда мы кидаем импорты на модели для миграций
"""
from src.messages.models import Chat, Message
from src.notifications.models import Notification
from src.comments.models import BaseComment
from src.licenses.models import License
from src.albums.models import Album
from src.beatpacks.models import Beatpack
from src.squads.models import Squad
from src.auth.models import Role, User, ProducerProfile, ArtistProfile
from src.beats.models import Beat
from src.soundkits.models import Soundkit
from src.tags.models import Tag
from src.subscription.models import OnlyTelegramSubscribeMonth, OnlyTelegramSubscribeYear, TelegramAccount
from src.tracks.models import Track


