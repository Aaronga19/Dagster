import sqlalchemy.ext.declarative
import sqlalchemy.ext.declarative
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sqlalchemy.ext.declarative
from .settings import settings

Base = sqlalchemy.ext.declarative.declarative_base()
engine = create_engine(f'postgresql://{settings.dagster_pg_username}:{settings.dagster_pg_password}@{settings.dagster_pg_host}:{settings.dagster_pg_port}/{settings.dagster_pg_db}')

Session = sessionmaker(engine)
session = Session()