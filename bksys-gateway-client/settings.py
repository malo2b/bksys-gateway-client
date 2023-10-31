"""Settings."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    """App settings."""
    OPERAIONS_RULE_MS_HOST: str
    ACCOUNT_MS_HOST: str
    TRANSACTION_MS_HOST: str

    model_config = SettingsConfigDict(env_file=".env")


app_settings = AppSettings()


__all__ = ["app_settings", "AppSettings"]
