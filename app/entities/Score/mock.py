from interfaces.Score import ScoreAPI, ScoreModel
from util.types import Any, UUID, Timestamp, ContentType, HTTPResponse
from util.decorators import implements

@implements(ScoreAPI)
class MockScoreAPI:
  def get(id: UUID, kind: ContentType) -> HTTPResponse[Any]:
    return '<svg viewBox="0 0 1 1" />' if kind == 'text/html' else ScoreModel(
      criterion='0891293',
      average=10,
      timestamp='',
    )
