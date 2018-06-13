from ...interfaces.Score import ScoreAPI, ScoreModel
from ...types import Any, UUID, Timestamp, ContentType, HTTPResponse
from ...ioc import implements

@implements(ScoreAPI)
class MockScoreAPI:
  def get(id: UUID, kind: ContentType) -> HTTPResponse[Any]:
    return '<svg viewBox="0 0 1 1" />' if kind == 'text/html' else ScoreModel(
      criterion='0891293',
      average=10,
      timestamp='',
    )
