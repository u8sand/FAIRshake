from util.decorators import interface, model
from util.types import HTTPResponse, UUID, Timestamp, Optional, List

@model
class CriterionModel:
  '''
  type: object  
  properties:
    id:
      type: string
      description: Criterion ID
      example: d290f1ee-6c54-4b01-90e6-d701748f0851
    name:
      type: string
      description: Criterion being evaluated
      example: Coolness
    kind:
      type: string
      description: Value type of the criterion
      example: number
  '''
  id: UUID
  name: str
  kind: str

@model
class RubricModel:
  '''
  type: object
  description: An rubric for evaluating a digital object
  properties:
    id:
      type: string
      format: uuid
      description: ID of rubric
      example: d290f1ee-6c54-4b01-90e6-d701748f0851
    user:
      type: string
      format: uuid
      description: ID of user who made the rubric
      example: d290f1ee-6c54-4b01-90e6-d701748f0851
    timestamp:
      type: string
      description: When the rubric was made
      format: dateTime
      example: 2018-05-20T15:59:59-08:00
    criteria:
      type: array
      items:
        $ref: "#/definitions/Criterion"
  '''
  id: UUID
  user: UUID
  timestamp: Optional[Timestamp]
  criteria: List[CriterionModel]

@interface
class RubricAPI:
  '''
  swagger: '2.0'
  info:
    title: FAIRshakeRubric
    version: 1.0.0
    description: A generic FAIRshake Rubric REST API for storing questions to be answered.
    contact:
      email: daniel.clarke@mssm.edu
    license:
      name: Apache 2.0
      url: http://www.apache.org/licenses/LICENSE-2.0.html
  schemes:
  - https
  securityDefinitions:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: X-API-Key
  paths:
    /:
      get: {RubricAPI__get}
      post: {RubricAPI__post}
  definitions:
    Criterion: {CriterionModel}
    Rubric: {RubricModel}
  '''

  def get(
      id: Optional[UUID] = None,
      timestamp: Optional[Timestamp] = None,
      skip: Optional[int] = None,
      limit: Optional[int] = None,
    ) -> HTTPResponse[RubricModel]:
    '''
    summary: Query rubrics
    consumes:
    - application/json
    parameters:
    - name: id
      in: query
      description: Unique rubric identifier
      type: string
      format: uuid
    - name: timestamp
      in: query
      description: Updated at least since timestamp
      type: string
      format: dateTime
    - name: skip
      in: query
      description: Start index for limited results
      type: number
    - name: limit
      in: query
      description: Limit number of results
      type: number
    produces:
    - application/json
    responses:
      200:
        description: Rubrics as json
        schema:
          type: array
          items:
            $ref: "#/definitions/Rubric"
      404:
        description: Rubrics not found
    '''
    raise NotImplemented

  def post(
      body: RubricModel
    ) -> HTTPResponse[None]:
    '''
    summary: Submit rubric
    consumes:
    - application/json
    security:
    - ApiKeyAuth: []
    parameters:
    - name: body
      in: body
      schema:
        $ref: "#/definitions/Rubric"
    produces:
    - application/json
    responses:
      201:
        description: Rubric successfully made
      400:
        description: Parameters invalid
      500:
        description: Permission denied, not authenticated
    '''
    raise NotImplemented
