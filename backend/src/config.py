import os
from typing import Union
from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic_settings import BaseSettings

load_dotenv()

class YandexCloudSettings(BaseModel):
    YANDEX_CLOUD_OAUTH_TOKEN: str = os.environ.get("YANDEX_CLOUD_OAUTH_TOKEN")
    YANDEX_CLOUD_ID: str = os.environ.get("YANDEX_CLOUD_ID")
    AWS_ACCESS_KEY_ID: str = os.environ.get("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY: str = os.environ.get("AWS_SECRET_ACCESS_KEY")

class SpotifySettings(BaseModel):
    CLIENT_SECRET: str = os.environ.get("SPOTIFY_CLIENT_SECRET")
    CLIENT_ID: str = os.environ.get("SPOTIFY_CLIENT_ID")
    REDIRECT_URI: str = os.environ.get("REDIRECT_URI")

class DbSettings(BaseModel):
    DB_HOST: str = os.environ.get("DB_HOST")
    DB_PORT: int = int(os.environ.get("DB_PORT"))
    DB_NAME: str = os.environ.get("DB_NAME")
    DB_USER: str = os.environ.get("DB_USER")
    DB_PASS: str = os.environ.get("DB_PASS")

    @property
    def url(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    echo: bool = True

class AuthSettings(BaseModel):
    JWT_SECRET_KEY: str = os.environ.get("JWT_SECRET_KEY")
    JWT_REFRESH_SECRET_KEY: str = os.environ.get("JWT_REFRESH_SECRET_KEY")


class Settings(BaseSettings):
    api_v1_prefix: str = "/api/v1"
    db: DbSettings = DbSettings()
    auth: AuthSettings = AuthSettings()
    spotify: SpotifySettings = SpotifySettings()
    yandex_cloud: YandexCloudSettings = YandexCloudSettings()

settings = Settings()