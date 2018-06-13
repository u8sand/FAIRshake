from ...interfaces.Rubric import RubricAPI, RubricModel, CriterionModel
from ...types import HTTPResponse, UUID, Timestamp, Optional, List
from ...ioc import implements

@implements(RubricAPI)
class MockRubricAPI:
  def get(
      id: Optional[UUID] = None,
      timestamp: Optional[Timestamp] = None,
      skip: Optional[int] = None,
      limit: Optional[int] = None,
    ) -> HTTPResponse[List[RubricModel]]:
    return [RubricModel(
      id='123890',
      user='123231',
      name='blah rubric',
      criteria=[CriterionModel(id=123, name='blah', kind='text')],
    )]

  def post(
      body: RubricModel,
    ) -> HTTPResponse[None]:
    return HTTPResponse(201)
