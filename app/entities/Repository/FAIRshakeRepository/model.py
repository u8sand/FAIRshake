from ....ioc import implements
from ....interfaces.Repository import DigitalObjectModel
from ....types import UUID, Optional, List, Timestamp

import sqlalchemy as db
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class DigitalObjectTags(Base):
  __tablename__ = 'digital_object_tags'
  object = db.Column('object', db.ForeignKey('digital_object.id'), primary_key=True)
  tag: str = db.Column('tag', db.String, primary_key=True)

@implements(DigitalObjectModel)
class DigitalObject(Base):
  __tablename__ = 'digital_object'
  id: UUID = db.Column('id', db.String, primary_key=True)
  url: str = db.Column('url', db.String, primary_key=True)
  user: Optional[UUID] = db.Column('user', db.String)
  name: Optional[str] = db.Column('name', db.String)
  license: Optional[str] = db.Column('license', db.String)
  description: Optional[str] = db.Column('description', db.String)
  image: Optional[str] = db.Column('image', db.String)
  tags: Optional[List[str]] = relationship(DigitalObjectTags)
  timestamp: Optional[Timestamp] = db.Column('timestamp', db.DateTime, onupdate=datetime.now)
