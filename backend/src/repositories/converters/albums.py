from src.models.albums import Album
from src.repositories.dtos.albums import AlbumDTO


def convert_album_db_query_result_to_dto(album: Album):
    return AlbumDTO(
        name=album.name,
        picture_url=album.picture_url,
        description=album.description,
        co_prod=album.co_prod,
        type=album.type,
        user_id=album.user_id
    )
