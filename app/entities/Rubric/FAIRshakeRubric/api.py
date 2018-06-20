from injector import inject
from datetime import datetime
from dateutil import parser

from ....interfaces.Rubric import RubricAPI, RubricModel
from ....types import ContentType, UUID, HTTPResponse, Any, SQLAlchemy, Optional, Timestamp, List
from ....util.first_and_only import first_and_only
from ....util.filter_none_kwargs import filter_none_kwargs
from ....ioc import injector, implements

from .model import Rubric, Criterion, RubricObjects, RubricTags
from .util import answer_value

@implements(RubricAPI)
class FAIRshakeRubric:

  @staticmethod
  @inject
  def get(
      id: Optional[UUID] = None,
      user: Optional[UUID] = None,
      object: Optional[UUID] = None,
      timestamp: Optional[Timestamp] = None,
      skip: Optional[int] = None,
      limit: Optional[int] = None,
    ) -> HTTPResponse[List[RubricModel]]:
    db = injector.get(SQLAlchemy)()
    return db.query(Rubric).filter_by(
      **filter_none_kwargs(
        id=id,
        user=user,
      )
    ).join(
      RubricObjects
    ).filter(
      Rubric.timestamp >= (
        timestamp if timestamp is not None else datetime.min
      )
    ).slice(
      skip,
      limit,
    ).all()

  @staticmethod
  def post(
      body: RubricModel
    ) -> HTTPResponse[None]:
    # TODO: check authentication
    db = injector.get(SQLAlchemy)() # TODO: inject via args
    rubric = Rubric(
      id=body.id,
      user=body.user,
      name=body.name,
      description=body.description,
      timestamp=parser.parse(body.timestamp),
    )
    db.add(rubric)
    for tag in body.tags:
      db.add(RubricTags(
        rubric=rubric.id,
        tag=tag,
      ))
    for criterion in body.criteria:
      db.add(Criterion(
        rubric=rubric.id,
        id=criterion.id,
        name=criterion.name,
        kind=criterion.kind,
      ))
    db.commit()
