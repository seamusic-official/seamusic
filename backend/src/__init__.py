"""Не удаляй этот код, поскольку он используется при создании миграций в alembic.
Сюда мы кидаем импорты на модели для миграций
"""

from src.beatpacks.models import Beatpack
from src.squads.models import Squad
from src.auth.models import User, ProducerProfile, ArtistProfile
from src.beats.models import Beat
from src.soundkits.models import Soundkit
from src.tags.models import Tag
