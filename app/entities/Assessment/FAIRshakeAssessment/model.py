from injector import Module, provider, singleton
from ....ioc import injector, implements
from ....interfaces.Assessment import AssessmentModel, AnswerModel
from ....types import UUID, Optional, List, Timestamp, SQLAlchemyBase
from ....util.generate_uuid import generate_uuid

import sqlalchemy as db
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

@implements(AssessmentModel)
class Assessment(Base):
  __tablename__ = 'assessment'
  id: UUID = db.Column(db.String, primary_key=True, default=generate_uuid)
  object: UUID = db.Column(db.String)
  user: UUID = db.Column(db.String)
  rubric: UUID = db.Column(db.String)
  timestamp: Optional[Timestamp] = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
  answers: List[AnswerModel] = relationship('Answer')

@implements(AnswerModel)
class Answer(Base):
  __tablename__ = 'assessment_answer'
  assessment: UUID = db.Column(db.String, db.ForeignKey('assessment.id'), primary_key=True)
  criterion: UUID = db.Column(db.String, primary_key=True)
  value: str = db.Column(db.String)


@injector.binder.install
class RepositorySQLAlchemyBaseModule(Module):
  @provider
  @singleton
  def provide_SQLAlchemyBase(self) -> SQLAlchemyBase:
    return [Base]
