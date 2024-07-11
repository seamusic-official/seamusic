from __future__ import annotations
from typing import List
from datetime import datetime
from src.database import Base
from src.beats.models import Beat
from src.beatpacks.models import Beatpack
from src.licenses.models import License
from src.messages.models import Chat

from sqlalchemy import DateTime
from sqlalchemy import Column
from sqlalchemy import Table
from sqlalchemy import ForeignKey
from sqlalchemy import Integer

from sqlalchemy import ForeignKey
from sqlalchemy import event
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class TelegramAccount(Base):
    __tablename__ = 'telegram_accounts'

    username: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    role: Mapped[str] = mapped_column(nullable=False, default="Listener")
    picture_url: Mapped[str] = mapped_column(nullable=True, default="https://img.favpng.com/22/0/21/computer-icons-user-profile-clip-art-png-favpng-MhMHJ0Fw21MJadYjpvDQbzu5S.jpg")
    is_active: Mapped[bool] = mapped_column(nullable=True, default=False)

    birthday: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    registered_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    artist_profile_id: Mapped[int] = mapped_column(ForeignKey("artist_profiles.id"), nullable=True)
    artist_profile: Mapped["ArtistProfile"] = relationship(back_populates="user")
    producer_profile_id: Mapped[int] = mapped_column(ForeignKey("producer_profiles.id"), nullable=True)
    producer_profile: Mapped["ProducerProfile"] = relationship(back_populates="user")

