from injector import Module, provider, singleton
from ....ioc import injector, implements
from ....interfaces.Rubric import RubricModel, CriterionModel
from ....interfaces.Repository import DigitalObjectModel
from ....types import UUID, Optional, List, Timestamp, SQLAlchemyBase
from ....util.generate_uuid import generate_uuid

import sqlalchemy as db
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

@implements(RubricModel)
class Rubric(Base):
  __tablename__ = 'rubric'
  id: UUID = db.Column('id', db.String, primary_key=True, default=generate_uuid)
  user: UUID = db.Column('user', db.String)
  name: str = db.Column('name', db.String)
  criteria: List[CriterionModel] = relationship('Criterion')
  description: str = db.Column('description', db.String)
  tags: List[str] = relationship('RubricTags')
  timestamp: Timestamp = db.Column('timestamp', db.DateTime, onupdate=datetime.now)
  objects: List[DigitalObjectModel] = relationship('RubricObjects')

class RubricObjects(Base):
  __tablename__ = 'rubric_objects'
  rubric: UUID = db.Column('rubric', db.ForeignKey('rubric.id'), primary_key=True)
  object: UUID = db.Column('object', db.String, primary_key=True)

class RubricTags(Base):
  __tablename__ = 'rubric_tags'
  rubric: UUID = db.Column('rubric', db.ForeignKey('rubric.id'), primary_key=True)
  tag: str = db.Column('tag', db.String, primary_key=True)

@implements(CriterionModel)
class Criterion(Base):
  __tablename__ = 'criterion'
  rubric: UUID = db.Column('rubric', db.String, db.ForeignKey('rubric.id'), primary_key=True)
  id: UUID = db.Column('id', db.String, primary_key=True)
  name: str = db.Column('name', db.String)
  kind: str = db.Column('kind', db.String)

@injector.binder.install
class RepositorySQLAlchemyBaseModule(Module):
  @provider
  @singleton
  def provide_SQLAlchemyBase(self) -> SQLAlchemyBase:
    return [Base]
