from injector import Module, provider, singleton, inject

from flask import Flask
from flask_injector import FlaskInjector

from interfaces.Assessment import AssessmentAPI
from interfaces.Rubric import RubricAPI
from interfaces.Repository import RepositoryAPI
from interfaces.Score import ScoreAPI

from entities.Assessment.mock import MockAssessmentAPI
from entities.Rubric.mock import MockRubricAPI
from entities.Repository.mock import MockRepositoryAPI
from entities.Score.mock import MockScoreAPI

class APIMod(Module):
  @provider
  @singleton
  def provide_AssessmentAPI(self) -> AssessmentAPI:
    return MockAssessmentAPI()

  @provider
  @singleton
  def provide_RubricAPI(self) -> RubricAPI:
    return MockRubricAPI()

  @provider
  @singleton
  def provide_RepositoryAPI(self) -> RepositoryAPI:
    return MockRepositoryAPI()

  @provider
  @singleton
  def provide_ScoreAPI(self) -> ScoreAPI:
    return MockScoreAPI()

def main():
  from .view import app

  FlaskInjector(
    app=app,
    modules=[
      APIMod
    ],
  )

  app.run(debug=True)
