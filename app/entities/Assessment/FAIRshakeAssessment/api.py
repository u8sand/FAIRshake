from injector import inject

from ....interfaces.Assessment import AssessmentAPI, AssessmentModel
from ....types import ContentType, UUID, HTTPResponse, Any, SQLAlchemy, Optional, Timestamp, List
from ....util.first_and_only import first_and_only
from ....util.filter_none_kwargs import filter_none_kwargs
from ....ioc import implements

from .model import Assessment

@implements(AssessmentAPI)
class FAIRshakeAssessment:

  @staticmethod
  def get(
      db: SQLAlchemy,
      id: Optional[UUID] = None,
      user: Optional[UUID] = None,
      object: Optional[UUID] = None,
      rubric: Optional[UUID] = None,
      timestamp: Optional[Timestamp] = None,
      skip: Optional[int] = None,
      limit: Optional[int] = None,
    ) -> HTTPResponse[List[AssessmentModel]]:
    return db.query(Assessment).filter_by(
      **filter_none_kwargs(
        id=id,
        user=user,
        object=object,
        rubric=rubric,
      )
    ) \
    .filter(Assessment.timestamp >= timestamp) \
    .slice(
      skip,
      limit,
    ) \
    .all()

  @staticmethod
  def post(
      body: AssessmentModel
    ) -> HTTPResponse[None]:
    # TODO: check authentication
    # TODO: assert that assessment follows rubrics for the object
    Assessment(body).save()
