from injector import Injector, Module, provider, singleton, inject
from ...ioc import injector
from ...types import Apps

class CommandLineDump:
  def run():
    import os
    from app.util.generate_spec import json_to_yml

    from app.interfaces.Assessment import AssessmentSpec
    from app.interfaces.Repository import RepositorySpec
    from app.interfaces.Rubric import RubricSpec
    from app.interfaces.Score import ScoreSpec

    if not os.path.isdir('spec'):
      os.mkdir('spec')

    for name, spec in {
      'assessment': AssessmentSpec,
      'repository': RepositorySpec,
      'rubric': RubricSpec,
      'score': ScoreSpec,
    }.items():
      with open('spec/%s.yml' % (name), 'w') as fh:
        print(
          json_to_yml(
            spec
          ),
          file=fh,
        )

injector.binder.bind(Apps, to={'dump': CommandLineDump}, scope=singleton)
