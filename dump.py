import os
from app.util.generate_spec import generate_spec, json_to_yml

def mods_to_dict(mods):
  return {mod.__name__: mod for mod in mods}

def generate_assessment_spec():
  from app.interfaces.Assessment import AssessmentAPI, AssessmentModel, CriterionModel
  with open('spec/assessment.yml', 'w') as fh:
    print(json_to_yml(generate_spec(AssessmentAPI.__doc__, mods_to_dict([
      AssessmentAPI,
      AssessmentModel,
      CriterionModel,
    ]))), file=fh)

def generate_repository_spec():
  from app.interfaces.Repository import RepositoryAPI, DigitalObjectModel
  with open('spec/repository.yml', 'w') as fh:
    print(json_to_yml(generate_spec(RepositoryAPI.__doc__, mods_to_dict([
      RepositoryAPI,
      DigitalObjectModel,
    ]))), file=fh)

def generate_rubric_spec():
  from app.interfaces.Rubric import RubricAPI, RubricModel, CriterionModel
  with open('spec/rubric.yml', 'w') as fh:
    print(json_to_yml(generate_spec(RubricAPI.__doc__, mods_to_dict([
      RubricAPI,
      RubricModel,
      CriterionModel,
    ]))), file=fh)

def generate_score_spec():
  from app.interfaces.Score import ScoreAPI, ScoreModel
  with open('spec/score.yml', 'w') as fh:
    print(json_to_yml(generate_spec(ScoreAPI.__doc__, mods_to_dict([
      ScoreAPI,
      ScoreModel,
    ]))), file=fh)

if not os.path.isdir('spec'):
  os.mkdir('spec')

generate_assessment_spec()
generate_repository_spec()
generate_rubric_spec()
generate_score_spec()
