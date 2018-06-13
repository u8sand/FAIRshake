from ...interfaces.Assessment import AssessmentAPI, AssessmentModel, AnswerModel
from ...types import HTTPResponse, UUID, Timestamp, Optional, List
from ...ioc import implements

@implements(AssessmentAPI)
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
      answers = [
        AnswerModel(id='1', value='yes'),
        AnswerModel(id='2', value='http://google.com'),
        AnswerModel(id='3', value='some text'),
      ],
    ),
    AssessmentModel(id='2',
      object='2',
      user='1',
      rubric='123891',
      timestamp='111',
      answers=[
        AnswerModel(id='4', value='http://google.com'),
        AnswerModel(id='5', value='yes'),
      ],
    ),
    ]

  def post(
      body: AssessmentModel
    ) -> HTTPResponse[None]:
    return HTTPResponse(201)
