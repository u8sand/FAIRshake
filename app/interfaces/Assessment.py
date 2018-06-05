from util.decorators import interface, model
from util.types import HTTPResponse, UUID, Timestamp, Optional, List

@model
class CriterionModel:
  '''
  type: object
  properties:
    name:
      type: string
      description: Criterion being evaluated
      example: Coolness
    value:
      type: string
      description: Value of the criterion (of rubric-defined type)
      example: 0.8
  '''
  name: str
  value: str

@model
class AssessmentModel:
  '''
  description: An evaluation on a digital object based on a rubric
  type: object
  properties:
    id:
      type: string
      format: uuid
      description: ID of evaluation
      example: d290f1ee-6c54-4b01-90e6-d701748f0851
    user:
      type: string
      format: uuid
      description: ID of user who made the evaluation
      example: d290f1ee-6c54-4b01-90e6-d701748f0851
    rubric:
      type: string
      format: uuid
      description: ID of rubric used to make this evaluation
      example: d290f1ee-6c54-4b01-90e6-d701748f0851
    timestamp:
      type: string
      description: When the evaluation was made
      format: dateTime
      example: '2018-05-20T15:59:60-08:00'
    criteria:
      type: array
      items:
        $ref: "#/definitions/Criterion"
  '''
  id: UUID
  user: UUID
  rubric: UUID
  timestamp: Optional[Timestamp]
  criteria: List[CriterionModel]

@interface
class AssessmentAPI:
  '''
  swagger: '2.0'
  info:
    title: FAIRshakeAssessment
    version: 1.0.0
    description: A generic FAIRshake Assessment REST API for performing and storing manual assessments.
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
      get: {AssessmentAPI__get}
      post: {AssessmentAPI__post}
  definitions:
    Criterion: {CriterionModel}
    Assessment: {AssessmentModel}
  '''
  def get(
      id: Optional[UUID],
      object: Optional[UUID],
      rubric: Optional[UUID],
      timestamp: Optional[Timestamp],
      skip: Optional[int],
      limit: Optional[int],
    ) -> HTTPResponse[AssessmentModel]:
    '''
    summary: Query assessments for a given digital object
    consumes:
    - application/json
    parameters:
    - name: id
      in: query
      description: Unique assessment identifier
      type: string
      format: uuid
    - name: object
      in: query
      description: Unique object identifier
      type: string
      format: uuid
    - name: rubric
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
        description: Assessments as json
        schema:
          type: array
          items:
            $ref: "#/definitions/Assessment"
      404:
        description: Assessments not found
    '''
    raise NotImplemented

  def post(
      body: AssessmentModel
    ) -> HTTPResponse[None]:
    '''
    summary: Submit assessment for a given digital object with a given rubric
    consumes:
    - application/json
    security:
    - ApiKeyAuth: []
    parameters:
    - name: body
      in: body
      schema:
        $ref: "#/definitions/Assessment"
    produces:
    - application/json
    responses:
      201:
        description: Assessment successfully made
      400:
        description: Parameters invalid
      401:
        description: Something else went wrong
      500:
        description: Permission denied, not authenticated
    '''
    raise NotImplemented
