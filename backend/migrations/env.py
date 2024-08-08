import asyncio
from logging.config import fileConfig

from alembic import context
from sqlalchemy import pool
from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import async_engine_from_config

from src.core.config import settings
from src.core.database import Base
from src.models.albums import Album, album_track_association, artist_profile_album_association  # noqa 401
from src.models.auth import User, ProducerProfile, ArtistProfile, Role, user_to_roles_association  # noqa 401
from src.models.beatpacks import Beatpack  # noqa 401
from src.models.beats import Beat  # noqa 401
from src.models.comments import BaseComment  # noqa 401
from src.models.licenses import License  # noqa 401
from src.models.soundkits import Soundkit  # noqa 401
from src.models.subscriptions import TelegramAccount, OnlyTelegramSubscribeMonth, OnlyTelegramSubscribeYear  # noqa 401
from src.models.tags import Tag  # noqa 401
from src.models.tracks import Track  # noqa 401

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)


target_metadata = Base.metadata
config.set_main_option("sqlalchemy.url", settings.db.url)


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection: Connection) -> None:
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()


async def run_async_migrations() -> None:
    """In this scenario we need to create an Engine
    and associate a connection with the context.

    """

    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    asyncio.run(run_async_migrations())


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
