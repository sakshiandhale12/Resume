# erplib/config.py
from pydantic_settings import BaseSettings
from pydantic import Extra

class Settings(BaseSettings):
    ERPLIB_PRIMARY_POSTGRES_DB: str
    ERPLIB_PRIMARY_POSTGRES_USER: str
    ERPLIB_PRIMARY_POSTGRES_PASSWORD: str
    ERPLIB_PRIMARY_POSTGRES_HOST: str
    ERPLIB_PRIMARY_POSTGRES_PORT: int

    ERPLIB_POOL_MIN_SIZE: int
    ERPLIB_POOL_MAX_SIZE: int
    ERPLIB_POOL_IDLE_TIMEOUT: int
    ERPLIB_POOL_MAX_OVERFLOW: int
    ERPLIB_POOL_RECYCLE: int
    ERPLIB_POOL_PRE_PING: bool

    ERPLIB_HOST: str
    ERPLIB_PORT: int
    ERPLIB_PRIMARY_DB_URI: str

    class Config:
        env_file = ".env"
        extra = Extra.ignore

settings = Settings()
print("Loaded settings:", settings.dict())
