from injector import inject

from ....interfaces.Repository import RepositoryAPI, DigitalObjectModel
from ....types import ContentType, UUID, HTTPResponse, Any, SQLAlchemy, Optional, List, Timestamp
from ....util.first_and_only import first_and_only
from ....util.filter_none_kwargs import filter_none_kwargs
from ....ioc import injector, implements

from .model import DigitalObject, DigitalObjectTags

@implements(RepositoryAPI)
class FAIRshakeRepository:

  @staticmethod
  @inject
  def get(
      id: Optional[UUID] = None,
      tags: Optional[List[str]] = None,
      user: Optional[UUID] = None,
      name: Optional[str] = None,
      url: Optional[str] = None,
      timestamp: Optional[Timestamp] = '2000-01-01',
      skip: Optional[int] = None,
      limit: Optional[int] = None,
    ) -> HTTPResponse[List[DigitalObjectModel]]:
    db = injector.get(SQLAlchemy)()
    return db.query(DigitalObject).filter_by(
      **filter_none_kwargs(
        id=id,
        user=user,
        name=name,
        url=url,
      )
    ).filter(
      DigitalObject.timestamp >= timestamp
    ).join(
      DigitalObjectTags
    ).slice(
      skip,
      limit,
    ).all()

  @staticmethod
  def post(
      body: DigitalObjectModel
    ) -> HTTPResponse[None]:
    # TODO: check authentication
    db = injector.get(SQLAlchemy)() # TODO: inject via args
    db.add(DigitalObject(body))
    db.commit()
