# db.py

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from dotenv import dotenv_values
import os

metadata = MetaData()
Base = declarative_base()


def db_connect():
  config = dotenv_values("./.env")
  username = config.get("DATABASE_USERNAME")
  password = config.get("DATABASE_PASSWORD")
  dbname = config.get("DATABASE_NAME")
  port = config.get("DATABASE_PORT")
  host = config.get("DATABASE_HOST")

  engine = create_engine(
    f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{dbname}?client_encoding=utf8",
    echo=True
    )
  connection = engine.connect()

  return engine, connection
  

def create_session(engine):
  Session = sessionmaker(bind=engine)
  session = Session()

  return session





