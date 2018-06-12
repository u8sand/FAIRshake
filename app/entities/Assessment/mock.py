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
      rubric = '123890',
      timestamp = '111',
      criteria = [CriterionModel(id='1',value='yes'),
                  CriterionModel(id='2', value='http://google.com'),
                  CriterionModel(id='3', value='some text')]
    ),
    AssessmentModel(id='2',
      object='2',
      user='1',
      rubric='123891',
      timestamp='111',
      criteria=[CriterionModel(id='4', value='http://google.com'),
                CriterionModel(id='5', value='yes')]
    ),
    ]


  def post(
      body: AssessmentModel
    ) -> HTTPResponse[None]:
    return HTTPResponse(201)
