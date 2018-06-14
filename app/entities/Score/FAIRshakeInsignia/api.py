from ....interfaces.Score import ScoreAPI
from ....interfaces.Rubric import RubricAPI
from ....interfaces.Assessment import AssessmentAPI, AssessmentModel, AnswerModel
from ....types import ContentType, UUID, HTTPResponse, Any, SQLAlchemy
from ....util.first_and_only import first_and_only
from ....ioc import injector, implements

from .model import Score
from .views import kinds
from sqlalchemy.sql import func

from injector import inject

def answer_value(value: str):
  try:
    return float(value)
  except:
    return 1 if value != '' else 0

def get_or_create(session, model, defaults=None, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance, False
    else:
        params = dict((k, v) for k, v in kwargs.iteritems() if not isinstance(v, ClauseElement))
        params.update(defaults or {})
        instance = model(**params)
        session.add(instance)
        return instance, True

@implements(ScoreAPI)
class FAIRshakeInsignia:

  @staticmethod
  @inject
  def get(
    object: UUID,
    kind: ContentType,
  ) -> HTTPResponse[Any]:
    db = injector.get(SQLAlchemy)()
    rubric_api = injector.get(RubricAPI)
    assessment_api = injector.get(AssessmentAPI)

    timestamp = db.query(
      func.min(Score.timestamp)
    ).all()

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
        # TODO: write to database
    # Build visualization
    scores = db.query(Score).filter_by(object=object).all()
    return kinds.get(kind, kinds[''])(scores)
