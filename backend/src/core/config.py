import os

from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic_settings import BaseSettings


load_dotenv()


class YandexCloudSettings(BaseModel):
    YANDEX_CLOUD_OAUTH_TOKEN: str = os.environ["YANDEX_CLOUD_OAUTH_TOKEN"]
    YANDEX_CLOUD_ID: str = os.environ["YANDEX_CLOUD_ID"]
    AWS_ACCESS_KEY_ID: str = os.environ["AWS_ACCESS_KEY_ID"]
    AWS_SECRET_ACCESS_KEY: str = os.environ["AWS_SECRET_ACCESS_KEY"]


class SpotifySettings(BaseModel):
    CLIENT_SECRET: str = os.environ["SPOTIFY_CLIENT_SECRET"]
    CLIENT_ID: str = os.environ["SPOTIFY_CLIENT_ID"]
    # REDIRECT_URI: str = os.environ["REDIRECT_URI"]


class DbSettings(BaseModel):

    DB_HOST: str = os.environ["DB_HOST"]
    DB_PORT: int = int(os.environ["DB_PORT"])
    DB_NAME: str = os.environ["DB_NAME"]
    DB_USER: str = os.environ["DB_USER"]
    DB_PASS: str = os.environ["DB_PASS"]

    DB_HOST_TEST: str = os.environ["DB_HOST_TEST"]
    DB_PORT_TEST: int = int(os.environ["DB_PORT_TEST"])
    DB_NAME_TEST: str = os.environ["DB_NAME_TEST"]
    DB_USER_TEST: str = os.environ["DB_USER_TEST"]
    DB_PASS_TEST: str = os.environ["DB_PASS_TEST"]

    @property
    def url(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def url_test(self):
        return f"postgresql+asyncpg://{self.DB_USER_TEST}:{self.DB_PASS_TEST}@{self.DB_HOST_TEST}:{self.DB_PORT_TEST}/{self.DB_NAME_TEST}"

    echo: bool = True


class AuthSettings(BaseModel):
    JWT_SECRET_KEY: str = os.environ["JWT_SECRET_KEY"]
    JWT_REFRESH_SECRET_KEY: str = os.environ["JWT_REFRESH_SECRET_KEY"]


class Settings(BaseSettings):
    root_url: str = os.environ["ROOT_URL"]
    db: DbSettings = DbSettings()
    auth: AuthSettings = AuthSettings()
    spotify: SpotifySettings = SpotifySettings()
    yandex_cloud: YandexCloudSettings = YandexCloudSettings()


settings = Settings()
