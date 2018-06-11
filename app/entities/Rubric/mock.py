from interfaces.Rubric import RubricModel, CriterionModel
from util.types import HTTPResponse, UUID, Timestamp, Optional, List

class MockRubricAPI:
  def get(
      self,
      id: Optional[UUID] = None,
      timestamp: Optional[Timestamp] = None,
      skip: Optional[int] = None,
      limit: Optional[int] = None,
    ) -> HTTPResponse[List[RubricModel]]:
    return [RubricModel(
      id='123890',
      user='123231',
      name='yyy',
      criteria=[CriterionModel(id=123, name='blah', kind='yesnobut'),CriterionModel(id=1234, name='blah2', kind='yesnobut')],
      timestamp='0000'
    ),
      RubricModel(
        id='123891',
        user='123231',
        name='zzz',
        criteria=[CriterionModel(id=231, name='xyz1', kind='yesnobut'),
                  CriterionModel(id=41234, name='xyz2', kind='yesnobut')],
        timestamp='0000'
      )
    ]

  def post(
      body: RubricModel,
    ) -> HTTPResponse[None]:
    return HTTPResponse(201)
