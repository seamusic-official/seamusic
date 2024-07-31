from src.auth.models import (
    User,
    ProducerProfile,
    ArtistProfile,
    Role,
    user_to_roles_association,
    artist_tags_association,
    producer_tags_association,
    listener_tags_association,
)

from src.services import SQLAlchemyRepository


class UsersDAO(SQLAlchemyRepository):
    model = User


class ProducerDAO(SQLAlchemyRepository):
    model = ProducerProfile


class ArtistDAO(SQLAlchemyRepository):
    model = ArtistProfile


class RoleDAO(SQLAlchemyRepository):
    model = Role


class UserToRoleDAO(SQLAlchemyRepository):
    model = user_to_roles_association


class ListenerTagsDAO(SQLAlchemyRepository):
    model = listener_tags_association


class ProducerTagsDAO(SQLAlchemyRepository):
    model = producer_tags_association


class ArtistTagsDAO(SQLAlchemyRepository):
    model = artist_tags_association
