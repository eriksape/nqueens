import datetime
from sqlalchemy import Column, Integer, ARRAY, ForeignKey, BigInteger
from sqlalchemy.orm import relationship
from .database import Base

class DictMixIn:
    def to_dict(self):
        return {
            column.name: getattr(self, column.name)
            if not isinstance(
                getattr(self, column.name), (datetime.datetime, datetime.date)
            )
            else getattr(self, column.name).isoformat()
            for column in self.__table__.columns
        }

class Case(Base, DictMixIn):
    """The NQueen's case"""
    __tablename__ = 'cases'
    id = Column(Integer, primary_key=True)
    dimension = Column(Integer)
    solutions = Column(BigInteger)


class Answer(Base, DictMixIn):
    """The NQueen Solutions model"""
    __tablename__ = 'answers'
    id = Column(BigInteger, primary_key=True)
    dimension = Column(Integer)
    solution = Column(ARRAY(Integer))