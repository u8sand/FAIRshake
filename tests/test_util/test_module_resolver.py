import json
import connexion
from app.util.generate_spec import generate_spec, json_to_yml
from app.util.module_resolver import ModuleResolver
from app.util.types import HTTPResponse

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
    /test:
      post: {TestAPI__test__post}
  '''
  def get(a: str) -> HTTPResponse[str]:
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
    return a, 200

  class test:
    def post(a) -> HTTPResponse[str]:
      '''
      summary: Another test method
      consumes:
      - application/json
      parameters:
      - name: a
        in: body
        schema:
          type: object
          properties:
            b:
              type: string
        description: A test parameter
      produces:
      - application/json
      responses:
        404:
          description: A successful test
          schema:
            type: string
      '''
      return a, 200

def test_module_resolver():
  spec = generate_spec(TestAPI)
  flask_app = connexion.FlaskApp(TestAPI.__name__)
  flask_app.add_api(spec, resolver=ModuleResolver(TestAPI))

  with flask_app.app.test_client() as client:
    response = client.get('/?a=test')
    assert response.status_code == 200, response.status_code
    data = json.loads(response.data.decode())
    assert data == 'test', data

    response = client.post('/test', json={'b': 'test'})
    assert response.status_code == 200, response.status_code
    data = json.loads(response.data.decode())
    assert data == {'b': 'test'}, data
