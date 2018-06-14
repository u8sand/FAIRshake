from injector import Module, provider, singleton
from ....interfaces.Score import ScoreModel
from ....types import UUID, Timestamp, SQLAlchemyBase
from ....ioc import injector, implements

import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

@implements(ScoreModel)
class Score(Base):
  __tablename__ = 'score'
  object: UUID = db.Column('obj', db.Integer, primary_key=True)
  criterion: UUID = db.Column('criterion', db.Integer, primary_key=True)
  average: float = db.Column('average', db.Float)
  count: int = db.Column('count', db.Integer)
  timestamp: Timestamp = db.Column('timestamp', db.DateTime, onupdate=datetime.now)

@injector.binder.install
class ScoreSQLAlchemyBaseModule(Module):
  @provider
  @singleton
  def provide_SQLAlchemyBase(self) -> SQLAlchemyBase:
    return [Base]
