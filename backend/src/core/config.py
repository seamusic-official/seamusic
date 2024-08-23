from pydantic import Field
from pydantic_settings import BaseSettings
from dotenv import load_dotenv


load_dotenv()


class Settings(BaseSettings):

    yandex_cloud_oauth_token: str = Field(alias='YANDEX_CLOUD_OAUTH_TOKEN')
    yandex_cloud_id: str = Field(alias="YANDEX_CLOUD_ID")
    aws_access_key_id: str = Field(alias="AWS_ACCESS_KEY_ID")
    aws_secret_access_key: str = Field(alias="AWS_SECRET_ACCESS_KEY")

    spotify_client_id: str = Field(alias="SPOTIFY_CLIENT_ID")
    spotify_client_secret: str = Field(alias="SPOTIFY_CLIENT_SECRET")
    spotify_redirect_uri: str = Field(alias="SPOTIFY_REDIRECT_URI")

    db_host: str = Field(alias="DB_HOST")
    db_port: int = Field(alias="DB_PORT")
    db_name: str = Field(alias="DB_NAME")
    db_user: str = Field(alias="DB_USER")
    db_pass: str = Field(alias="DB_PASS")

    db_host_test: str = Field(alias="DB_HOST_TEST")
    db_port_test: int = Field(alias="DB_PORT_TEST")
    db_name_test: str = Field(alias="DB_NAME_TEST")
    db_user_test: str = Field(alias="DB_USER_TEST")
    db_pass_test: str = Field(alias="DB_PASS_TEST")

    echo: bool = True

    jwt_secret_ket: str = Field("JWT_SECRET_KEY")
    jwt_refresh_secret_key: str = Field("JWT_REFRESH_SECRET_KEY")

    bucket_name: str = Field("BUCKET_NAME")

    @property
    def url(self) -> str:
        return f"postgresql+asyncpg://{self.db_user}:{self.db_pass}@{self.db_host}:{self.db_port}/{self.db_name}"

    @property
    def url_test(self) -> str:
        return f"postgresql+asyncpg://{self.db_user_test}:{self.db_pass_test}@{self.db_host_test}:{self.db_port_test}/{self.db_name_test}"


settings = Settings()
