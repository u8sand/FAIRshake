from interfaces.Score import ScoreModel
from util.types import Any, UUID, Timestamp, ContentType, HTTPResponse, Optional

class MockScoreAPI:
  def get(self,
      id: Optional[UUID] = None,
      user: Optional[UUID] = None,
      kind: Optional[ContentType] = None,
    ) -> HTTPResponse[Any]:
    return '<svg width="40" height="40"><rect width="13" height="13" x="0" y="0" style="fill: rgb(128, 0, 128); stroke: white; stroke-width: 1; shape-rendering: crispEdges; fill-opacity: 1;"></rect><rect width="13" height="13" x="13" y="0" style="fill: rgb(213, 0, 42); stroke: white; stroke-width: 1; shape-rendering: crispEdges; fill-opacity: 1;"></rect><rect width="13" height="13" x="26" y="0" style="fill: rgb(128, 0, 128); stroke: white; stroke-width: 1; shape-rendering: crispEdges; fill-opacity: 1;"></rect><rect width="13" height="13" x="0" y="13" style="fill: rgb(85, 0, 170); stroke: white; stroke-width: 1; shape-rendering: crispEdges; fill-opacity: 1;"></rect><rect width="13" height="13" x="13" y="13" style="fill: rgb(128, 0, 128); stroke: white; stroke-width: 1; shape-rendering: crispEdges; fill-opacity: 1;"></rect><rect width="13" height="13" x="26" y="13" style="fill: rgb(213, 0, 42); stroke: white; stroke-width: 1; shape-rendering: crispEdges; fill-opacity: 1;"></rect><rect width="13" height="13" x="0" y="26" style="fill: rgb(128, 0, 128); stroke: white; stroke-width: 1; shape-rendering: crispEdges;"></rect><rect width="13" height="13" x="13" y="26" style="fill: rgb(128, 0, 128); stroke: white; stroke-width: 1; shape-rendering: crispEdges;"></rect><rect width="13" height="13" x="26" y="26" style="fill: rgb(128, 0, 128); stroke: white; stroke-width: 1; shape-rendering: crispEdges;"></rect></svg>'\
      if kind == 'text/html' else [ScoreModel(
      criterion='0891293',
      average=10,
      timestamp='',
    )]