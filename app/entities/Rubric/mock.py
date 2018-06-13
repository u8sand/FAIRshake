from interfaces.Rubric import RubricAPI, RubricModel, CriterionModel
from util.types import HTTPResponse, UUID, Timestamp, Optional, List
from util.decorators import implements

@implements(RubricAPI)
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
      name='Rubric1',
      criteria=[CriterionModel(id='1', name='Question 1 for rubric1', kind='yesnobut'),
                CriterionModel(id='2', name='Please enter URL for question 1 for rubric1', kind='url'),
                CriterionModel(id='3', name='Please explain your answer for question 1 for rubric1', kind='text')],
      timestamp='0000'
    ),
      RubricModel(
        id='123891',
        user='123231',
        name='Rubric2',
        criteria=[CriterionModel(id='4', name='Question 1 for rubric2', kind='url'),
                  CriterionModel(id='5', name='Question 2 for rubric2', kind='yesnobut')],
        timestamp='0000'
      )
    ]

  def post(
      body: RubricModel,
    ) -> HTTPResponse[None]:
    return HTTPResponse(201)
