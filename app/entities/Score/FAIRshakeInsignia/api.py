from ....interfaces.Score import ScoreAPI
from ....interfaces.Rubric import RubricAPI
from ....interfaces.Assessment import AssessmentAPI, AssessmentModel, AnswerModel
from ....types import ContentType, UUID, HTTPResponse, Any, SQLAlchemy
from ....util.first_and_only import first_and_only
from ....ioc import implements

from .model import Score
from .views import kinds

from injector import inject

def answer_value(value: str):
  try:
    return float(value)
  except:
    return 1 if value != '' else 0

@implements(ScoreAPI)
class FAIRshakeInsignia:

  @staticmethod
  @inject
  def get(
    db: SQLAlchemy,
    rubric_api: RubricAPI,
    assessment_api: AssessmentAPI,
    object: UUID,
    kind: ContentType,
  ) -> HTTPResponse[Any]:
    # Update scores as required
    rubrics = rubric_api.get(object=object)
    for rubric in rubrics:
      new_assessments = assessment_api.get(object=object, rubric=rubric.id, timestamp=timestamp)
      new_assessments_score_sums = {}
      for assessment in new_assessments:
        for answer in assessment.answers:
          new_assessments_score_sums[answer.criterion] += new_assessments_score_sums.get(answer.criterion, 0) + answer_value(answer.value)
      for criterion in rubric.criteria:
        score = get_or_create(db, Score, object=object, criterion=criterion.id)
        score.average = score.average / score.count + new_assessments_score_sums[criterion.id] / len(new_assessments_score_sums[criterion.id])
        score.save()
    # Build visualization
    scores = db.query(Score).filter_by(obj=id).all()
    return kinds.get(kind, kinds[''])(scores)
