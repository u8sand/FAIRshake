from injector import inject

from ....interfaces.Repository import RepositoryAPI, DigitalObjectModel
from ....types import ContentType, UUID, HTTPResponse, Any, SQLAlchemy, Optional, List, Timestamp
from ....util.first_and_only import first_and_only
from ....util.filter_none_kwargs import filter_none_kwargs
from ....ioc import implements

from .model import DigitalObject

@implements(RepositoryAPI)
class FAIRshakeRepository:

  @staticmethod
  def get(
      db: SQLAlchemy,
      id: Optional[UUID] = None,
      tags: Optional[List[str]] = None,
      user: Optional[UUID] = None,
      name: Optional[str] = None,
      url: Optional[str] = None,
      timestamp: Optional[Timestamp] = None,
      skip: Optional[int] = None,
      limit: Optional[int] = None,
    ) -> HTTPResponse[List[DigitalObjectModel]]:
    return db.query(DigitalObject).filter_by(
      **filter_none_kwargs(
        id=id,
        user=user,
        name=name,
        url=url,
      )
    ) \
    .filter(DigitalObject.timestamp >= timestamp) \
    .filter_by(DigitalObject.tags.in_(tags)) \
    .slice(
      skip,
      limit,
    ) \
    .all()

  @staticmethod
  def post(
      body: DigitalObjectModel
    ) -> HTTPResponse[None]:
    # TODO: check authentication
    DigitalObject(body).save()
