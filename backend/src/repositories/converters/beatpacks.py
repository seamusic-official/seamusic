from src.models.beatpacks import Beatpack
from src.repositories.dtos.beatpacks import BeatpackDTO


def convert_beatpack_db_query_result_to_dto(beatpack: Beatpack) -> BeatpackDTO:
    return BeatpackDTO(
        title=beatpack.title,
        description=beatpack.description,
        users=beatpack.users,
        beats=beatpack.beats
    )
