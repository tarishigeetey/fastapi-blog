from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    algorithm: str = "HS256"
    secret_key: SecretStr
    access_token_expire_minutes: int = 30
    max_upload_size_bytes: int = 5 * 1024 * 1024  # 5 MB
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    posts_per_page: int = 10  # Number of posts to display per page in paginated responses
    reset_token_expire_minutes: int = 60 # Expiration time for password reset tokens in minutes
    mail_server: str
    mail_port: int
    mail_username: str
    mail_password: SecretStr = SecretStr("")
    mail_from: str  = "noreply@yourapp.com"
    mail_use_tls: bool = True

    frontend_url: str = "http://localhost:8000"  # Base URL for the frontend application


settings = Settings()  # type: ignore[call-arg] #Loaded settings from .env file
