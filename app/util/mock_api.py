from .generate_spec import generate_spec
from swagger_stub import swagger_stub
from bravado.client import SwaggerClient

def MockAPISwagger(api):
  ''' Mock an API with swagger tools extracting the swagger
  spec, building a swagger_stub, and connecting to it with a
  bravado-based SwaggerClient.
  '''
  mock_url = 'http://{id}'.format(api.__name__)
  # Generate swagger spec from interface
  spec = generate_spec(doc.__doc__, {api.__name__: api})
  spec['host'] = mock_url
  # Create stub with swagger spec
  swagger_stub([(spec, mock_url)])
  # Connect to stub with bravado
  return SwaggerClient.from_url(mock_url)
