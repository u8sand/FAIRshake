import json
import connexion
from util.generate_spec import generate_spec, json_to_yml
from util.module_resolver import ModuleResolver
from ..api import TestAPI

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
