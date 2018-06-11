from interfaces.Repository import DigitalObjectModel
from util.types import HTTPResponse, List, Optional, Timestamp, UUID

class MockRepositoryAPI:
  def get(
      self,
      id: Optional[UUID] = None,
      tag: Optional[List[str]] = None,
      user: Optional[UUID] = None,
      name: Optional[str] = None,
      url: Optional[str] = None,
      timestamp: Optional[Timestamp] = None,
      skip: Optional[int] = None,
      limit: Optional[int] = None,
    ) -> HTTPResponse[List[DigitalObjectModel]]:
    return [DigitalObjectModel(
      id='1',
      user='aaa',
      name='FAIRness of LINCS Datasets and Tools',
      url='',
      tags=['project'],
      timestamp='',
      description='FAIR evaluation of LINCS',
      image='https://www.commonfund.nih.gov/sites/default/files/phenotypic_them1.gif'
    ),
      DigitalObjectModel(
        id='2',
        user='aaa',
        name='FAIRness of MOD',
        url='',
        tags=[],
        timestamp='',
        description='FAIR evaluation of MOD',
        image='https://www.commonfund.nih.gov/sites/default/files/phenotypic_them1.gif'
      ),
      DigitalObjectModel(
        id='3',
        user='aaa',
        name='L1000CDS2',
        url='',
        tags=['resource', 'project:1'],
        timestamp='',
        description='FAIR evaluation of LINCS',
        image='https://www.commonfund.nih.gov/sites/default/files/phenotypic_them1.gif'
      ),
      DigitalObjectModel(
        id='4',
        user='aaa',
        name='iLINCS',
        url='',
        tags=['resource', 'project:1'],
        timestamp='',
        description='FAIR evaluation of LINCS',
        image='https://www.commonfund.nih.gov/sites/default/files/phenotypic_them1.gif'
      ),
      DigitalObjectModel(
        id='5',
        user='aaa',
        name='FAIRness of LINCS Datasets and Tools',
        url='',
        tags=[],
        timestamp='',
        description='FAIR evaluation of LINCS',
        image='https://www.commonfund.nih.gov/sites/default/files/phenotypic_them1.gif'
      ),
      DigitalObjectModel(
        id='6',
        user='aaa',
        name='FAIRness of LINCS Datasets and Tools',
        url='',
        tags=[],
        timestamp='',
        description='FAIR evaluation of LINCS',
        image='https://www.commonfund.nih.gov/sites/default/files/phenotypic_them1.gif'
      ),
      DigitalObjectModel(
        id='7',
        user='aaa',
        name='FAIRness of LINCS Datasets and Tools',
        url='',
        tags=[],
        timestamp='',
        description='FAIR evaluation of LINCS',
        image='https://www.commonfund.nih.gov/sites/default/files/phenotypic_them1.gif'
      )
    ]
    # return DigitalObjectModel(
    #   id='1',
    #   user='aaa',
    #   name='FAIRness of LINCS Datasets and Tools',
    #   url='',
    #   tags=[],
    #   timestamp='',
    #   description='FAIR evaluation of LINCS',
    #   image='https://www.commonfund.nih.gov/sites/default/files/phenotypic_them1.gif'
    # )

  def post(
      body: DigitalObjectModel
    ) -> HTTPResponse[None]:
    return HTTPResponse(201)
