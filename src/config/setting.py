from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import computed_field, model_validator
from typing_extensions import Self
from typing import List
from dotenv import load_dotenv
import psutil
import socket

def get_host() -> str | None:
  for iface, addrs in psutil.net_if_addrs().items():
    if "wi" in iface.lower() or "wireless" in iface.lower():
      for addr in addrs:
        if addr.family == socket.AF_INET:
          return addr.address
  return None


load_dotenv()

class Settings(BaseSettings):
  PROJECT_NAME: str
  STACK_NAME: str
  SERVER_PORT: int
  SERVER_DOMAIN: str
  WIFI_DOMAIN: str = get_host()
  BACKEND_CORS_ORIGINS: str
  POSTGRESQL_URI: str
  JWT_ACCESS_TOKEN: str
  JWT_ACCESS_TOKEN_EXPIRE_MINUTES : int
  JWT_REFRESH_TOKEN: str
  JWT_REFRESH_TOKEN_EXPIRE_DAYS: int
  JWT_ALGORITHM: str

  EMAIL_VERIFY_SECRET: str
  EMAIL_VERIFY_SALT: str
  EMAIL_EXP_HOUR: int

  ADMIN_EMAIL: str
  ADMIN_PASSWORD: str
  SMTP_HOST: str
  SMTP_USER: str
  SMTP_PASSWORD: str
  EMAILS_FROM_EMAIL: str
  EMAILS_NAME: str
  SMTP_TLS: str
  SMTP_SSL: str
  SMTP_PORT: int

  FRONTEND_HOST: str

  REDIS_URI: str


  @model_validator(mode="after")
  def _set_default_emails_from(self) -> Self:
    if not self.EMAILS_NAME:
      self.EMAILS_FROM_NAME = self.PROJECT_NAME
    return self

  EMAIL_RESET_TOKEN_EXPIRE_HOURS: int = 3600 * 24 * 2

  @computed_field  # type: ignore[prop-decorator]
  @property
  def emails_enabled(self) -> bool:
    return bool(self.SMTP_HOST and self.EMAILS_FROM_EMAIL)

  model_config = SettingsConfigDict(
    env_file=".env",
    extra='ignore'
  )


settings = Settings()








