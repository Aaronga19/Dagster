from pydantic import BaseSettings

class Settings(BaseSettings):
    dagster_home:str
    dagster_pg_username:str
    dagster_pg_password: str
    dagster_pg_host:str
    dagster_pg_db: str
    dagster_pg_port: str

    class Config:
        env_file = ".env"

    
settings = Settings()