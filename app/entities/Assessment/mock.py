from interfaces.Assessment import AssessmentModel, CriterionModel
from util.types import HTTPResponse, UUID, Timestamp, Optional, List

class MockAssessmentAPI:
  def get(
      self,
      id: Optional[UUID] = None,
      user: Optional[UUID] = None,
      object: Optional[UUID] = None,
      rubric: Optional[UUID] = None,
      timestamp: Optional[Timestamp] = None,
      skip: Optional[int] = None,
      limit: Optional[int] = None,
    ) -> HTTPResponse[AssessmentModel]:
    return [AssessmentModel(id = '1',
      object = '1',
      user = '1',
      rubric = '111',
      timestamp = '111',
      criteria = [CriterionModel(id='123',value='abc')]
    ),
    AssessmentModel(id='2',
      object='2',
      user='1',
      rubric='111',
      timestamp='111',
      criteria=[CriterionModel(id='321', value='abc')]
    ),
    ]

  def post(
      body: AssessmentModel
    ) -> HTTPResponse[None]:
    return HTTPResponse(201)
