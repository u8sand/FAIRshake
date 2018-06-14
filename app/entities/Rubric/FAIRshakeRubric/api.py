from injector import inject

from ....interfaces.Rubric import RubricAPI, RubricModel
from ....types import ContentType, UUID, HTTPResponse, Any, SQLAlchemy, Optional, Timestamp, List
from ....util.first_and_only import first_and_only
from ....util.filter_none_kwargs import filter_none_kwargs
from ....ioc import injector, implements

from .model import Rubric, Criterion, RubricObjects
from .util import answer_value

@implements(RubricAPI)
class FAIRshakeRubric:

  @staticmethod
  @inject
  def get(
      id: Optional[UUID] = None,
      user: Optional[UUID] = None,
      object: Optional[UUID] = None,
      timestamp: Optional[Timestamp] = '2000-01-01',
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
      Rubric.timestamp >= timestamp
    ).slice(
      skip,
      limit,
    ).all()

  @staticmethod
  def post(
      body: RubricModel
    ) -> HTTPResponse[None]:
    # TODO: check authentication
    Rubric(body).save()
