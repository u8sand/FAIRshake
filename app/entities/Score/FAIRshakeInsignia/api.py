from ....interfaces.Assessment import AssessmentAPI
from ....interfaces.Rubric import RubricAPI
from ....interfaces.Score import ScoreAPI
from ....types import ContentType, UUID, HTTPResponse
from ....ioc import implements

from .model import Score
from .views import kinds

from injector import inject
from .types import SQLAlchemy

# @implements(ScoreAPI)
class FAIRshakeInsignia:
  @inject
  def get(
    db: SQLAlchemy,
    rubric: RubricAPI,
    assessment: AssessmentAPI,
    id,# : UUID,
    kind,# : str,
  ) -> HTTPResponse[str]:
    scores = db.query(Score).filter_by(obj=id).all()
    return kinds.get(kind, kinds[''])(scores)
