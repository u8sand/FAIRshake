import json
from connexion import FlaskApp
from injector import Injector, Module, Key, provider, singleton, inject
from flask_injector import FlaskInjector
from app.types import HTTPResponse
from app.util.generate_spec import generate_spec, json_to_yml
from app.util.module_resolver import ModuleResolver

GoodStatus = Key("GoodStatus")
Test = Key("Test")

class SomeInterface:
  def echo(s: str) -> str:
    raise NotImplemented

class SomeInterfaceImpl:
  def echo(
    status: GoodStatus,
    s: str,
  ) -> str:
    assert status == 200
    return s

class TestAPIInterface:
  '''
  swagger: '2.0'
  info:
    title: TestAPI
    version: 1.0.0
    description: A test api
  schemes:
  - https
  paths:
    /:
      get: {TestAPI__get}
  '''
  @staticmethod
  def get(a: str = None) -> HTTPResponse[str]:
    '''
    summary: A test method
    parameters:
    - name: a
      in: query
      type: string
      description: A test parameter
    produces:
    - application/json
    responses:
      200:
        description: A successful test
        schema:
          type: string
    '''
    raise NotImplemented

class TestAPI:
  @staticmethod
  @inject
  def get(
    impl: SomeInterface,
    good_status: GoodStatus,
    a: str = None
  ) -> HTTPResponse[str]:
    return impl.echo(a), good_status


class ImplModule(Module):
  @provider
  @singleton
  def provide_some_interface(self) -> SomeInterface:
    return SomeInterfaceImpl
  
  @provider
  @singleton
  def provide_api(self) -> TestAPIInterface:
    return TestAPI

class GoodStatusModule(Module):
  @provider
  @singleton
  def provide_good_status(self) -> GoodStatus:
    return 200

class FlaskInjectorModule(Module):
  @provider
  @singleton
  def provide_flask_injected(self, api: TestAPIInterface, injector: Injector) -> FlaskApp:
    spec = generate_spec(TestAPIInterface)
    flask_app = FlaskApp(api.__name__)
    flask_app.add_api(spec, resolver=ModuleResolver(api))
    FlaskInjector(app=flask_app.app, injector=injector)
    return flask_app


def test_connexion_inject():
  injector = Injector()
  injector.binder.bind(Injector, to=injector, scope=singleton)
  injector.binder.install(ImplModule)
  injector.binder.install(GoodStatusModule)
  injector.binder.install(FlaskInjectorModule)

  flask_app = injector.get(FlaskApp)
  with flask_app.app.test_client() as client:
    response = client.get('/?a=test')
    assert response.status_code == 200, response.status_code
    data = json.loads(response.data.decode())
    assert data == 'test', data
