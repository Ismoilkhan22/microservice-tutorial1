from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    secret_key: str
    postgres_user: str
    postgres_password: str
    postgres_host: str
    db_name: str = "default_db"  # Har service'da o'zgartiring: chat_db_name
    kafka_bootstrap_servers: str = "kafka:9092"
    kafka_topic: str = "payments-topic"
    redis_url: str = "redis://redis:6379/0"
    log_level: str = "INFO"

    class Config:
        env_file = ".env"

settings = Settings()