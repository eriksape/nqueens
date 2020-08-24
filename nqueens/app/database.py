import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

database_string = "postgresql+psycopg2://{}:{}@{}:{}/{}".format(
    os.environ['DB_USERNAME'],
    os.environ['DB_PASSWORD'],
    os.environ['DB_HOST'],
    os.environ['DB_PORT'],
    os.environ['DB_DATABASE']
)

engine = create_engine(database_string, executemany_mode='batch')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
