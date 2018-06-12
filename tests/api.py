from util.types import HTTPResponse

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
