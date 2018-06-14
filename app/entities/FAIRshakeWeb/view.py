import re
import json
from flask import Flask, render_template, request, redirect
from ...interfaces.Repository import RepositoryAPI, DigitalObjectModel
from ...interfaces.Assessment import AssessmentAPI, AssessmentModel
from ...interfaces.Rubric import RubricAPI
from ...interfaces.Score import ScoreAPI
from ...util.first_and_only import first_and_only, first
from flask_oidc import OpenIDConnect

import os

app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']
app.config.update({
  'OIDC_CLIENT_SECRETS': os.environ['OIDC_CLIENT_SECRETS'],
  'OIDC_SCOPES': ['openid', 'sub', 'name', 'email'],
  'SESSION_TYPE': 'filesystem',
})
oidc = OpenIDConnect(app)

current_user = {'id': '1'}

project_id_tag_re = re.compile(r'^project:(?P<id>\d+)$')

def get_project_id(repository: DigitalObjectModel):
  ''' Figure out the project this resource is related to.
  '''
  return first_and_only(
    filter(
      None,
      [
        project_id_tag_re.match(tag)
        for tag in repository.tags
      ],
    )
  ).group('id')

def current_user():
  return {
    'id': oidc.user_getfield('sub') if oidc.user_loggedin else None,
    'name': oidc.user_getfield('name') if oidc.user_loggedin else '',
    'email': oidc.user_getfield('email') if oidc.user_loggedin else '',
    'is_authenticated': oidc.user_loggedin,
  }

@app.route('/', methods=['GET'])
def index(repository: RepositoryAPI):
  ''' FAIRshakeHub Home Page
  '''
  return render_template('index.html',
    top_projects=repository.get(limit=4),
    current_user=current_user(),
  )

@app.route('/projects', methods=['GET'])
def projects(repository: RepositoryAPI):
  return render_template('projects.html',
    projects=repository.get(tags=['project']),
    current_user=current_user(),
  )

@app.route('/start_project', methods=['GET'])
def start_project():
  return render_template('start_project.html',
    current_user=current_user(),
  )

@app.route('/chrome_extension', methods=['GET'])
def chrome_extension():
  return render_template('chrome_extension.html',
    current_user=current_user(),
  )

@app.route('/bookmarklet', methods=['GET'])
def bookmarklet():
  return render_template('bookmarklet.html',
    current_user=current_user(),
  )

@app.route('/login', methods=['GET'])
@oidc.require_login
def login():
  return render_template('login.html',
    current_user=current_user(),
  )

@app.route('/register', methods=['GET'])
def register():
  return render_template('register.html',
    current_user=current_user(),
  )

@app.route('/project/<int:project>/resources', methods=['GET'])
def resources(repository: RepositoryAPI, assessment: AssessmentAPI, score: ScoreAPI, project):
  resources=repository.get(tags=['project:{:d}'.format(project)])
  current_user_assessed_resources = [
    resource.id for resource in resources
    if assessment.get(object=resource.id, user=current_user['id']) != []
  ]
  assessment_count = {
    resource.id: len(assessment.get(object=resource.id))
    for resource in resources
  }
  aggregate_scores = {
    resource.id: score.get(object=resource.id, kind='text/html')
    for resource in resources
  }
  return render_template('project_resources.html',
    project=first(repository.get(id='{:d}'.format(project), limit=1)),
    resources=resources,
    aggregate_scores=aggregate_scores,
    assessment_count=assessment_count,
    current_user_assessed_resources=current_user_assessed_resources,
    current_user=current_user(),
  )

@app.route('/project/<int:project>/my_evaluations', methods=['GET'])
def my_evaluations(repository: RepositoryAPI, assessment: AssessmentAPI, score: ScoreAPI, project):
  current_user_assessed_resources = [
    resource for resource in repository.get(tags=['project:{:d}'.format(project)])
    if assessment.get(object=resource.id, user=current_user['id']) != []
  ]
  assessment_count = {
    resource.id: len(assessment.get(object=resource.id))
    for resource in current_user_assessed_resources
  }
  aggregate_scores = {
    resource.id: score.get(object=resource.id, kind='text/html')
    for resource in current_user_assessed_resources
  }
  current_user_scores = {
    resource.id: score.get(object=resource.id, user=current_user['id'], kind='text/html')
    for resource in current_user_assessed_resources
  }
  return render_template('project_evaluated_resources.html',
    project=first(repository.get(id='{:d}'.format(project), limit=1)),
    aggregate_scores=aggregate_scores,
    current_user_scores=current_user_scores,
    assessment_count=assessment_count,
    current_user_assessed_resources=current_user_assessed_resources,
    current_user=current_user(),
  )

@app.route('/evaluation', methods=['GET', 'POST'])
def evaluation(repository: RepositoryAPI, rubric: RubricAPI, assessment: AssessmentAPI):
  if request.method == 'GET':
    resource_id = request.args.get('id')
    return render_template('evaluation.html',
      resource=first(repository.get(id=resource_id, limit=1)),
      rubrics=rubric.get(),
      rubric_ids=[rubric.id for rubric in rubric.get()],
      current_user_assessment=assessment.get(object=resource_id, user=current_user['id']),
      current_user=current_user(),
    )
  else:
    resource_id=request.form.get('resource_id')
    rubric_ids=json.loads(request.form.get('rubric_ids'))
    rubrics=[first(rubric.get(id=rubric_id)) for rubric_id in rubric_ids]
    for rubric in rubrics:
      answers = [
        {
          'id': criterion.id,
          'value': request.form.get(criterion.id)
        }
        for criterion in rubric.criteria
      ]
      assessment.post(
        AssessmentModel(
          object=resource_id,
          user=current_user['id'],
          rubric=rubric.id,
          answers=answers,
        )
      )
    project = get_project_id(first(repository.get(resource_id)))
    return redirect('/project/{:d}/resources'.format(project))

@app.route('/evaluated_projects', methods=['GET'])
def evaluated_projects(repository: RepositoryAPI, assessment: AssessmentAPI):
  evaluated_projects_id_list = {
    first(
      repository.get(
        id=get_project_id(
          first(
            repository.get(id=assessment_each.object)
          )
        )
      )
    ).id
    for assessment_each in assessment.get(user=current_user['id'])
  }
  evaluated_projects = [
    first(repository.get(id=id_each))
    for id_each in evaluated_projects_id_list
  ]
  return render_template('evaluated_projects.html',
    evaluated_projects=evaluated_projects,
    current_user=current_user(),
  )

@app.route('/logout', methods=['GET'])
def logout():
  oidc.logout()
  return ''
