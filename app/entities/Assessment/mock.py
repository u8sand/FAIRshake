from interfaces.Assessment import AssessmentAPI, AssessmentModel
from util.types import HTTPResponse, UUID, Timestamp, Optional, List
from util.decorators import implements

@implements(AssessmentAPI)
class MockAssessmentAPI:
  def get(
      id: Optional[UUID] = None,
      object: Optional[UUID] = None,
      rubric: Optional[UUID] = None,
      timestamp: Optional[Timestamp] = None,
      skip: Optional[int] = None,
      limit: Optional[int] = None,
    ) -> HTTPResponse[List[AssessmentModel]]:
    return [AssessmentModel()]

  def post(
      body: AssessmentModel
    ) -> HTTPResponse[None]:
    return HTTPResponse(201)
