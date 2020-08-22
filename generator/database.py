import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, ARRAY, ForeignKey, BigInteger
from sqlalchemy.ext.declarative import declarative_base

database_string = "postgresql://{}:{}@{}:{}/{}".format(
    os.environ['DB_USERNAME'],
    os.environ['DB_PASSWORD'],
    os.environ['DB_HOST'],
    os.environ['DB_PORT'],
    os.environ['DB_DATABASE']
)
database = create_engine(database_string)

Session = sessionmaker(database)
connection = Session()

models = declarative_base()


class Case(models):
    """The NQueen's case"""
    __tablename__ = 'cases'
    id = Column(Integer, primary_key=True)
    dimension = Column(Integer)
    solutions = Column(BigInteger)


class Answer(models):
    """The NQueen Solutions model"""
    __tablename__ = 'answers'
    id = Column(BigInteger, primary_key=True)
    case_id = Column(Integer, ForeignKey('cases.id'))
    solution = Column(ARRAY(Integer))


models.metadata.create_all(database)
