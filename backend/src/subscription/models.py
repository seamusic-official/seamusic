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


class OnlyTelegramSubscribeMonth(Base):
    __tablename__ = 'only_telegram_subscribe_month'

    telegram_id: Mapped[str] = mapped_column(nullable=False)
    subscribe: Mapped[bool] = mapped_column(nullable=False, default=False)
    
    telegram_account_id = Column(Integer, ForeignKey('telegram_accounts.id'))
    telegram_account = relationship("TelegramAccount", back_populates="only_telegram_subscribe_month")

class OnlyTelegramSubscribeYear(Base):
    __tablename__ = 'only_telegram_subscribe_year'

    telegram_id: Mapped[str] = mapped_column(nullable=False)
    subscribe: Mapped[bool] = mapped_column(nullable=False, default=False)

    telegram_account_id = Column(Integer, ForeignKey('telegram_accounts.id'))
    telegram_account = relationship("TelegramAccount", back_populates="only_telegram_subscribe_year")

class TelegramAccount(Base):
    __tablename__ = 'telegram_accounts'

    telegram_id: Mapped[str] = mapped_column(nullable=False)
    subscribe: Mapped[bool] = mapped_column(nullable=False, default=False)
    only_telegram_subscribe_year: Mapped["OnlyTelegramSubscribeYear"] = relationship(back_populates="telegram_account")
    only_telegram_subscribe_month: Mapped["OnlyTelegramSubscribeMonth"] = relationship(back_populates="telegram_account")