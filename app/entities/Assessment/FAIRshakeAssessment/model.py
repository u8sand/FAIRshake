from ....ioc import implements
from ....interfaces.Assessment import AssessmentModel, AnswerModel
from ....types import UUID, Optional, List, Timestamp

import sqlalchemy as db
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

@implements(AnswerModel)
class Answer(Base):
  __tablename__ = 'assessment_answer'
  assessment: db.Column('assessment', db.ForeignKey('assessment.id'), primary_key=True)
  criterion: UUID = db.Column('criterion', db.String, primary_key=True)
  value: str = db.Column('value', db.String)

@implements(AssessmentModel)
class Assessment(Base):
  __tablename__ = 'assessment'
  id: UUID = db.Column('id', db.String, primary_key=True)
  object: UUID = db.Column('object', db.String)
  user: UUID = db.Column('user', db.String)
  rubric: UUID = db.Column('rubric', db.String)
  timestamp: Optional[Timestamp] = db.Column('timestamp', db.DateTime, onupdate=datetime.now)
  answers: List[AnswerModel] = relationship(Answer)
