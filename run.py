#!/usr/bin/env python3
import logging
logging.getLogger('injector').setLevel(logging.DEBUG)
from injector import Injector, Module, Key, Binder, provider, singleton, inject, InstanceProvider
import connexion
from flask_injector import FlaskInjector
from app.util.module_resolver import ModuleResolver
from app.util.types import List, Interfaces
from app.util.generate_spec import generate_spec
from app.util.bind import bind
from app.interfaces.Rubric import RubricAPI
from app.interfaces.Assessment import AssessmentAPI
from app.interfaces.Score import ScoreAPI, ScoreSpec
from app.interfaces.Repository import RepositoryAPI
from app.entities.Score.FAIRshakeInsignia.types import SQLAlchemy

API = Key("API")
APISpec = Key("APISpec")
App = Key("App")
AppRunner = Key("AppRunner")
ConnexionConfig = Key("ConnexionConfig")
FlaskConfig = Key("FlaskConfig")
FlaskRunConfig = Key("FlaskRunConfig")
Modules = Key("Modules")
SQLAlchemyEngine = Key("SQLAlchemyEngine")

class ConnexionAppModule(Module):
  @provider
  @singleton
  @inject
  def provide_app(self, api: API, api_spec: APISpec, depends: Modules, connexion_config: ConnexionConfig) -> App:
    flask_app = connexion.FlaskApp(api.__name__, **connexion_config)
    flask_app.add_api(specification=api_spec, resolver=ModuleResolver(api))
    FlaskInjector(app=flask_app.app, modules=depends)
    return flask_app

class FlaskAppModule(Module):
  @provider
  @singleton
  @inject
  def provide_flask_app(self, api: API, depends: Modules, flask_config: FlaskConfig) -> App:
    flask_app = Flask(api.__name__, **flask_config)
    FlaskInjector(app=flask_app, modules=depends)
    return flask_app

class FlaskAppRunner(Module):
  @singleton
  @provider
  @inject
  def provide_app_runner(self, app: App, flask_run_config: FlaskRunConfig) -> AppRunner:
    return bind(app.run, **flask_run_config)

class MockRubricModule(Module):
  @singleton
  @provider
  def provide_MockRubric(self) -> RubricAPI:
    from entities.Rubric.mock import MockRubricAPI
    return MockRubricAPI

class MockRepositoryModule(Module):
  @singleton
  @provider
  def provide_MockRepository(self) -> RepositoryAPI:
    from entities.Repository.mock import MockRepositoryAPI
    return MockRepositoryAPI

class MockAssessmentModule(Module):
  @singleton
  @provider
  def provide_MockAssessment(self) -> AssessmentAPI:
    from entities.Assessment.mock import MockAssessmentAPI
    return MockAssessmentAPI

class MockScoreModule(Module):
  @singleton
  @provider
  def provide_FAIRshakeInsignia(self) -> ScoreAPI:
    from entities.Score.mock import MockScoreAPI
    return MockScoreAPI

class FAIRshakeInsigniaDatabaseModule(Module):
  @singleton
  @provider
  def provide_engine(self) -> SQLAlchemyEngine:
    import os
    from sqlalchemy import create_engine
    from app.entities.Score.FAIRshakeInsignia.model import Base
    engine = create_engine(os.environ.get('DB_URI', 'sqlite:///FAIRshakeInsignia.db'))
    Base.metadata.create_all(engine)
    return engine

  @singleton
  @provider
  @inject
  def provide_db(self, engine: SQLAlchemyEngine) -> SQLAlchemy:
    from sqlalchemy.orm import sessionmaker
    return sessionmaker(bind=engine)()

def FAIRshakeInsigniaDepends(binder):
  binder.multibind(Modules, to=[
    MockRubricModule,
    MockAssessmentModule,
    FAIRshakeInsigniaDatabaseModule,
  ], scope=singleton)
  return binder

class FAIRshakeInsigniaModule(Module):
  @singleton
  @provider
  @inject
  def provide_API(self, rubric: RubricAPI, assessment: AssessmentAPI) -> API:
    from entities.Score.FAIRshakeInsignia.api import FAIRshakeInsignia
    return FAIRshakeInsignia

  @singleton
  @provider
  def provide_API_spec(self) -> APISpec:
    return ScoreSpec

class ConfigureModule(Module):
  @provider
  @singleton
  def provide_ConnexionConfig(self) -> ConnexionConfig:
    return dict(
      debug=True
    )
  
  @provider
  @singleton
  def provide_FlaskConfig(self) -> FlaskConfig:
    return dict(
      debug=True,
    )
  
  @provider
  @singleton
  def provide_FlaskRunConfig(self) -> FlaskRunConfig:
    return dict(
      host='0.0.0.0',
      port=8082,
      debug=True,
      threaded=True
    )

Injector([
  ConfigureModule,

  FAIRshakeInsigniaModule,

  ConnexionAppModule,
  FlaskAppRunner,

  FAIRshakeInsigniaDepends,
]).get(AppRunner)()
