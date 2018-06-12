from app.util.generate_spec import generate_spec

def mods_to_dict(mods):
  return {mod.__name__: mod for mod in mods}

def test_generate_assessment_spec():
  from app.interfaces.Assessment import AssessmentAPI, AssessmentModel, AnswerModel
  try:
    generate_spec(AssessmentAPI, mods_to_dict([ AssessmentModel, AnswerModel ]))
  except Exception as e:
    assert False, e

def test_generate_repository_spec():
  from app.interfaces.Repository import RepositoryAPI, DigitalObjectModel
  try:
    generate_spec(RepositoryAPI, mods_to_dict([ DigitalObjectModel ]))
  except Exception as e:
    assert False, e

def test_generate_rubric_spec():
  from app.interfaces.Rubric import RubricAPI, RubricModel, CriterionModel
  try:
    generate_spec(RubricAPI, mods_to_dict([ RubricModel, CriterionModel ]))
  except Exception as e:
    assert False, e

def test_generate_score_spec():
  from app.interfaces.Score import ScoreAPI, ScoreModel
  try:
    generate_spec(ScoreAPI, mods_to_dict([ ScoreModel ]))
  except Exception as e:
    assert False, e
