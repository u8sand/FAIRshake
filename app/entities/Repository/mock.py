from ...interfaces.Repository import RepositoryAPI, DigitalObjectModel
from ...types import HTTPResponse, List, Optional, Timestamp, UUID
from ...ioc import implements

@implements(RepositoryAPI)
class MockRepositoryAPI:
  def get(
      id: Optional[UUID] = None,
      tag: Optional[List[str]] = None,
      user: Optional[UUID] = None,
      name: Optional[str] = None,
      url: Optional[str] = None,
      timestamp: Optional[Timestamp] = None,
      skip: Optional[int] = None,
      limit: Optional[int] = None,
    ) -> HTTPResponse[List[DigitalObjectModel]]:
    return [DigitalObjectModel(
      id='',
      user='',
      name='',
      url='',
      tags=[],
      timestamp='',
    )]

  def post(
      body: DigitalObjectModel
    ) -> HTTPResponse[None]:
    return HTTPResponse(201)
