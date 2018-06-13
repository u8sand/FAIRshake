from ..ioc import interface, model
from ..types import HTTPResponse, UUID, Timestamp, Optional, List
from ..util.generate_spec import generate_spec

@model
class AnswerModel:
  '''
  type: object
  properties:
    criterion:
      type: string
      description: Criterion id in rubric being evaluated
      example: d290f1ee-6c54-4b01-90e6-d701748f0851
    value:
      type: string
      description: Value of the answer (of rubric-defined type)
      example: 0.8
  '''
  criterion: UUID
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
    object:
      type: string
      format: uuid
      description: ID of object evaluated
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
      example: '2018-05-20T15:59:59-08:00'
    answers:
      type: array
      items:
        $ref: "#/definitions/Answer"
  '''
  id: UUID
  object: UUID
  user: UUID
  rubric: UUID
  timestamp: Optional[Timestamp]
  answers: List[AnswerModel]

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
    Answer: {AnswerModel}
    Assessment: {AssessmentModel}
  '''

  @staticmethod
  def get(
      id: Optional[UUID] = None,
      user: Optional[UUID] = None,
      object: Optional[UUID] = None,
      rubric: Optional[UUID] = None,
      timestamp: Optional[Timestamp] = None,
      skip: Optional[int] = None,
      limit: Optional[int] = None,
    ) -> HTTPResponse[List[AssessmentModel]]:
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
    - name: user
      in: query
      description: Unique user identifier
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

  @staticmethod
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

AssessmentSpec = generate_spec(AssessmentAPI, [AssessmentModel, AnswerModel])
