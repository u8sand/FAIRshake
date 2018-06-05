from interfaces.Rubric import RubricModel, CriterionModel
from util.types import HTTPResponse, UUID, Timestamp, Optional, List

class MockRubricAPI:
  def get(
      id: Optional[UUID] = None,
      timestamp: Optional[Timestamp] = None,
      skip: Optional[int] = None,
      limit: Optional[int] = None,
    ) -> HTTPResponse[RubricModel]:
    return [RubricModel(
      id='123890',
      user='123231',
      criteria=[CriterionModel(id=123, name='blah', kind='text')],
    )]

  def post(
      body: RubricModel
    ) -> HTTPResponse[None]:
    return HTTPResponse(201)
