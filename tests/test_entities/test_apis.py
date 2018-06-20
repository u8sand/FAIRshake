from app.ioc import injector
from app.types import SQLAlchemy, Environment
from app.interfaces.Score import ScoreAPI, ScoreModel
from app.interfaces.Repository import RepositoryAPI, DigitalObjectModel
from app.interfaces.Rubric import RubricAPI, RubricModel, CriterionModel
from app.interfaces.Assessment import AssessmentAPI, AssessmentModel, AnswerModel

def test_all():
    injector.binder.bind(Environment, to={
        'sqlalchemy_uri': 'sqlite:///FAIRshakeTest.db',
    })
    score_api = injector.get(ScoreAPI)
    repository_api = injector.get(RepositoryAPI)
    rubric_api = injector.get(RubricAPI)
    assessment_api = injector.get(AssessmentAPI)

    rubric = RubricModel(
        id='1',
        user='1',
        name='AwesomeRubric',
        description='My Awesome Rubric',
        tags=['test', 'awesome', 'rubric'],
        timestamp='2018-06-20',
        criteria=[
            CriterionModel(
                id='1',
                name='Awesomeness',
                kind='text',
            ),
            CriterionModel(
                id='2',
                name='Unawesomeness',
                kind='yesno',
            ),
        ],
    )
    rubric_api.post(rubric)
    ret = rubric_api.get(id='1')
    assert ret == [rubric], ret

    object = DigitalObjectModel(
        id='1',
        url='http://test.com',
        user='1',
        name='Test',
        description='My test website',
        tags=['test', 'object'],
        timestamp='2018-06-20',
    )
    registry_api.post(object)
    assert registry_api.get(id='1') == [object]

    assessment = AssessmentModel(
        id='1',
        object='1',
        user='1',
        rubric='1',
        timestamp='2018-06-20',
        # TODO: Answers here really shouldn't be specified here
        answers=[
            AnswerModel(
                criterion='1',
                value='very',
            ),
            AnswerModel(
                criterion='2',
                value='no',
            )
        ]
    )
    assessment_api.post(assessment)
    assert assessment_api.get(id='1') == [assessment]

    assert score_api.get(
        object='1',
        kind='application/json',
    ) is not None
