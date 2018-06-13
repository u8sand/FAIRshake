from ....ioc import implements
from ....interfaces.Rubric import RubricModel, CriterionModel
from ....types import UUID, Optional, List, Timestamp

import sqlalchemy as db
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

@implements(CriterionModel)
class Criterion(Base):
  __tablename__ = 'criterion'
  id: UUID = db.Column('id', db.String, primary_key=True)
  name: str = db.Column('name', db.String)
  kind: str = db.Column('kind', db.String)

class RubricTags(Base):
  __tablename__ = 'rubric_tags'
  rubric: UUID = db.Column('rubric', db.ForeignKey('rubric.id'), primary_key=True)
  tag: str = db.Column('tag', db.String, primary_key=True)

@implements(RubricModel)
class Rubric(Base):
  __tablename__ = 'rubric'
  id: UUID = db.Column('id', db.String, primary_key=True)
  user: UUID = db.Column('user', db.String)
  name: str = db.Column('name', db.String)
  criteria: List[CriterionModel] = relationship(Criterion)
  description: Optional[str] = db.Column('description', db.String)
  tags: Optional[List[str]] = relationship(RubricTags)
  timestamp: Optional[Timestamp] = db.Column('timestamp', db.DateTime, onupdate=datetime.now)
