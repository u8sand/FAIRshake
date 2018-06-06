from util.decorators import interface, model
from util.types import UUID, Timestamp, ContentType, HTTPResponse

@model
class ScoreModel:
  '''
  type: object
  required:
  - criterion
  - average
  - timestamp
  properties:
    criterion:
      type: string
      format: uuid
      description: Criterion rubric identifier
      example: d290f1ee-6c54-4b01-90e6-d701748f0851
    average:
      type: number
      description: Average score for this criterion
      example: 0.54
    timestamp:
      type: string
      description: Last updated
      example: '2018-05-20T15:59:59-08:00'
  '''
  criterion: UUID
  average: float
  timestamp: Timestamp

@interface
class ScoreAPI:
  '''
  swagger: '2.0'
  info:
    title: FAIRshakeScore
    version: 1.0.0
    description: A generic FAIRshake Score REST API for aggregating and visualizing the results of FAIRshake assessments.
    contact:
      email: daniel.clarke@mssm.edu
    license:
      name: Apache 2.0
      url: http://www.apache.org/licenses/LICENSE-2.0.html
  schemes:
  - https
  paths:
    /:
      get: {ScoreAPI__get}
  definitions:
    Score: {ScoreModel}
  '''

  def get(
    id: UUID,
    kind: ContentType,
  ) -> HTTPResponse[str]:
    '''
    summary: Query score for a given digital object
    parameters:
    - name: id
      in: query
      type: string
      description: Unique Digital Object Identifier
      required: true
    - name: kind
      in: query
      type: string
      description: Content type of the score we want (e.g. application/json or text/html)
    produces:
    - text/html
    - application/json
    responses:
      200:
        description: Score as json
        schema:
          type: array
          items:
            $ref: "#/definitions/Score"
      201:
        description: Score as html
        schema:
          type: string
          example: '<svg viewBox="0 0 1 1" />'
      401:
        description: ContentType not recognized
      404:
        description: Digital object not found
    '''
    raise NotImplemented
