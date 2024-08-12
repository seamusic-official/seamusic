from src.models.beats import Beat
from src.repositories.dtos.beats import BeatDTO


def convert_beat_db_query_result_to_dto(beat: Beat) -> BeatDTO:
    return BeatDTO(
        title=beat.title,
        description=beat.description,
        picture_url=beat.picture_url,
        file_url=beat.file_url,
        co_prod=beat.co_prod,
        type=beat.type,
        user_id=beat.user_id
    )
