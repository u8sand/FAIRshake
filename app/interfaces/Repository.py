from util.decorators import interface, model
from util.types import HTTPResponse, List, Optional, Timestamp, UUID

@model
class DigitalObjectModel:
  '''
  required:
  - name
  - url
  properties:
    id:
      type: string
      format: uuid
      example: d290f1ee-6c54-4b01-90e6-d701748f0851
    user:
      type: string
      format: uuid
      example: d290f1ee-6c54-4b01-90e6-d701748f0851
    name:
      type: string
      example: MyTool
    url:
      type: string
      example: https://mytool.com/
    description:
      type: string
      example: My tool is widely used.
    image:
      type: string
      example: http://mytool.com/logo.png
    tags:
      type: array
      items:
        type: string
        example: tool
    timestamp:
      type: string
      format: dateTime
      description: Last updated
      example: '2018-05-20T15:59:60-08:00'
  '''
  id: UUID
  user: Optional[UUID]
  name: Optional[str]
  url: str
  description: Optional[str]
  image: Optional[str]
  tags: Optional[List[str]]
  timestamp: Optional[Timestamp]

@interface
class RepositoryAPI:
  '''
  swagger: '2.0'
  info:
    title: FAIRshakeRepository
    version: 1.0.0
    description: A generic FAIR Repository REST API for storing information about digital objects.
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
      get:
        {RepositoryAPI__get}
      post:
        {RepositoryAPI__post}
  definitions:
    DigitalObject:
      type: object
      {DigitalObjectModel}
  '''
  def get(
      id: Optional[UUID] = None,
      tag: Optional[List[str]] = None,
      user: Optional[UUID] = None,
      name: Optional[str] = None,
      url: Optional[str] = None,
      timestamp: Optional[Timestamp] = None,
      skip: Optional[int] = None,
      limit: Optional[int] = None,
    ) -> HTTPResponse[DigitalObjectModel]:
    '''
    summary: Query for digital objects
    parameters:
    - name: id
      in: query
      description: Unique object identifier
      type: string
      format: uuid
    - name: tag
      in: query
      description: Digital object tags
      type: array
      items:
        type: string
    - name: user
      in: query
      description: User id association
      type: string
      format: uuid
    - name: name
      in: query
      description: Name of the digital object
      type: string
    - name: url
      in: query
      description: URL of the digital object
      type: string
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
        description: Data object matching query
        schema:
          $ref: '#/definitions/DigitalObject'
      201:
        description: Multiple data objects matching query
        schema:
          type: array
          items:
            $ref: '#/definitions/DigitalObject'
      400:
        description: Query types are invalid
      404:
        description: No data object matching this query
      500:
        description: Permission denied, not authenticated
    '''
    raise NotImplemented

  def post(
      body: DigitalObjectModel
    ) -> HTTPResponse[None]:
    '''
    summary: Add or update digital object in the repository
    consumes:
    - application/json
    security:
    - ApiKeyAuth: []
    parameters:
    - name: body
      in: body
      schema:
        $ref: "#/definitions/DigitalObject"
    produces:
      - application/json
    responses:
      201:
        description: Digital object successfully registered
      400:
        description: Digital object invalid
      500:
        description: Permission denied, not authenticated
    '''
    raise NotImplemented
