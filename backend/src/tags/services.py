from src.tags.models import Tag, artist_tags_association, producer_tags_association, listener_tags_association
from src.services import SQLAlchemyRepository


class ListenerTagsDAO(SQLAlchemyRepository):
    model = listener_tags_association

class ProducerTagsDAO(SQLAlchemyRepository):
    model = producer_tags_association

class ArtistTagsDAO(SQLAlchemyRepository):
    model = artist_tags_association

class TagsDAO(SQLAlchemyRepository):
    model = Tag
