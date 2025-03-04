from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="BRUMALINK_", env_file=".env")

    database_url: str = "postgresql+psycopg://brumalink:brumalink@localhost:5432/shipments"
    alert_email_from: str = "alerts@brumalink.example"
    alert_smtp_host: str = "localhost"
    alert_webhook_timeout_s: float = 5.0
    tracker_shared_secret: str = "change-me"


settings = Settings()
