import json
import connexion
from injector import Module, Key, provider, singleton, inject
from flask_injector import FlaskInjector
from util.generate_spec import generate_spec, json_to_yml
from util.module_resolver import ModuleResolver
from util.types import HTTPResponse

GoodStatus = Key("GoodStatus")

class SomeInterface:
  def echo(s: str) -> str:
    raise NotImplemented

class SomeInterfaceImpl:
  def echo(s: str) -> str:
    return s

class ImplModule(Module):
  @provider
  @singleton
  def provide_good_status(self) -> SomeInterface:
    return SomeInterfaceImpl

class GoodStatusModule(Module):
  @provider
  @singleton
  def provide_good_status(self) -> GoodStatus:
    return 200

class TestAPI:
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
  def get(a: str, impl: SomeInterface, good_status: GoodStatus) -> HTTPResponse[str]:
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
    return impl.echo(a), good_status

def test_connexion_inject():
  spec = generate_spec(TestAPI)
  flask_app = connexion.FlaskApp(TestAPI.__name__)
  flask_app.add_api(spec, resolver=ModuleResolver(TestAPI))
  FlaskInjector(app=flask_app.app, modules=[ImplModule, GoodStatusModule])

  with flask_app.app.test_client() as client:
    response = client.get('/?a=test')
    assert response.status_code == 200, response.status_code
    data = json.loads(response.data.decode())
    assert data == 'test', data
