from ....interfaces.Score import ScoreModel
from ....types import UUID, Timestamp
from ....ioc import implements

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
