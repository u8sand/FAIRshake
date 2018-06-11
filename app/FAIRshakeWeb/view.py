from flask import Flask, render_template, request, redirect
from interfaces.Repository import RepositoryAPI
from interfaces.Assessment import AssessmentAPI
from interfaces.Rubric import RubricAPI
from interfaces.Score import ScoreAPI
import json

app = Flask(__name__)

current_user={'id':1}

@app.route('/', methods=['GET'])
def index(repository: RepositoryAPI):
  ''' FAIRshakeHub Home Page
  '''
  return render_template('index.html',
    top_projects=repository.get(limit=4),
    current_user={},
  )

@app.route('/projects', methods=['GET'])
def projects(repository: RepositoryAPI):
  return render_template('projects.html',
    projects=repository.get(),
    current_user={},
  )

@app.route('/start_project', methods=['GET'])
def start_project():
  return render_template('start_project.html',
    current_user={},
  )

@app.route('/chrome_extension', methods=['GET'])
def chrome_extension():
  return render_template('chrome_extension.html',
    current_user={},
  )

@app.route('/bookmarklet', methods=['GET'])
def bookmarklet():
  return render_template('bookmarklet.html',
    current_user={},
  )

@app.route('/login', methods=['GET'])
def login():
  return render_template('login.html',
    current_user={},
  )

@app.route('/register', methods=['GET'])
def register():
  return render_template('register.html',
    current_user={},
  )

@app.route('/project/<int:project>/resources', methods=['GET'])
def resources(repository: RepositoryAPI, assessment: AssessmentAPI, score: ScoreAPI, project):
  resources=repository.get(tag=project)
  current_user_assessments = []
  assessment_count = {}
  aggregate_scores = {}
  for resource in resources: #resource-id=1-7
    try:
      assessment.get(object=resource.id, user=current_user['id']) ### redesign, if there is an assessment for this object for this user
      current_user_assessments.append(resource.id) # just array with resource ids
    except:
      pass
    assessment_count[resource.id] = len(assessment.get(object=resource.id)) # all assessments from all users for all rubrics
    aggregate_scores[resource.id] = score.get(id=resource.id,kind='text/html') # scores is an array of html with tooltip script
  current_user_assessments=['1'] ###
  return render_template('project_resources.html',
    project=repository.get(id=project,limit=1), ###
    resources=resources,
    aggregate_scores=aggregate_scores,
    assessment_count=assessment_count,
    current_user_assessments=current_user_assessments,
    current_user={},
  )

@app.route('/project/<int:project>/my_evaluations', methods=['GET'])
def my_evaluations(repository: RepositoryAPI, assessment: AssessmentAPI, score: ScoreAPI, project):
  project_resources=repository.get(tag=project)
  current_user_assessed_resources = []
  assessment_count = {}
  aggregate_scores = {}
  current_user_scores = {}
  for resource in project_resources:
    try:
      assessment.get(object=resource.id, user=current_user['id'])
      current_user_assessed_resources.append(resource)
    except:
      pass
    assessment_count[resource.id] = len(assessment.get(object=resource.id)) # all assessments from all users for all rubrics
    aggregate_scores[resource.id] = score.get(id=resource.id,kind='text/html') # scores is an array of html with tooltip script
    current_user_scores[resource.id] = score.get(id=resource.id,user=current_user['id'],kind='text/html')
  current_user_assessed_resources=[repository.get(limit=1)] ###
  return render_template('project_evaluated_resources.html',
    project=repository.get(id=project,limit=1), ###
    aggregate_scores=aggregate_scores,
    current_user_scores=current_user_scores,
    assessment_count=assessment_count,
    current_user_assessed_resources=current_user_assessed_resources,
    current_user={},
  )

@app.route('/new_evaluation', methods=['GET','POST'])
def new_evaluation(repository: RepositoryAPI, rubric: RubricAPI, assessment: AssessmentAPI):
  if request.method == 'GET':
    resource_id = request.args.get('id')
    return render_template('new_evaluation.html',
      resource=repository.get(id=resource_id,limit=1),
      rubrics=rubric.get(id=resource_id),
      rubric_ids=[rubric.id for rubric in rubric.get(id=resource_id)],
      current_user={},
    )
  else:
    resource_id=request.form.get('resource_id')
    rubric_ids=json.loads(request.form.get('rubric_ids'))
    rubrics=[rubric.get(id=rubric_id)[0] for rubric_id in rubric_ids]
    for rubric_index, rubric in enumerate(rubrics):
      criteria = [] # evaluations
      for criterion_index, criterion in enumerate(rubric.criteria): # questions
        criteria.append(
          {
            'name': criterion.name,
            'value': request.form.get('q-{:d}.{:d}'.format(rubric_index,criterion_index))
          }
        )
      assessmentModel = {
        'object': resource_id,
        'user': current_user['id'],
        'rubric': rubric.id,
        'criteria': criteria
      }
      assessment.post(json.dumps(assessmentModel)) # post consumes json, assessmentmodel representation
    project=repository.get(resource_id).tag
    return redirect('/project/{:d}/resources'.format(project))

@app.route('/modify_evaluation', methods=['GET','POST'])
def modify_evaluation(repository: RepositoryAPI, rubric: RubricAPI, assessment: AssessmentAPI):
  if request.method == 'GET':
    resource_id = request.args.get('id')
    return render_template('modify_evaluation.html',
      resource=repository.get(id=resource_id,limit=1),
      rubrics=rubric.get(id=resource_id),
      current_user_assessment=assessment.get(id=resource_id,user=current_user['id']),
      current_user={},
    )
  else:
    for rubric_index, rubric in enumerate(json.loads(request.form.get('rubrics'))):
      criteria = [] # evaluations
      for criterion_index, criterion in enumerate(rubric.criteria): # questions
        criteria.append(
          {
            'name': criterion.name,
            'value': request.form.get('q-{:d}.{:d}'.format(rubric_index,criterion_index))
          }
        )
      assessmentModel = {
        'object': request.form.get('resource_id'),
        'user': current_user['id'],
        'rubric': rubric.id,
        'criteria': criteria
      }
      assessment.post(json.dumps(assessmentModel)) # post consumes json, assessmentmodel representation
    project=1
    return redirect('/project/{:d}/resources'.format(project))

@app.route('/evaluated_projects', methods=['GET'])
def evaluated_projects(repository: RepositoryAPI, assessment: AssessmentAPI):
  evaluated_projects = set()
  for assessment in assessment.get(user=current_user['id']):
    evaluated_projects.add(repository.get(id=repository.get(id=assessment.object).tag))
  return render_template('evaluated_projects.html',
    evaluated_projects=evaluated_projects,
    current_user={},
  )

# @app.route('/logout', methods=['GET'])
# def logout():
#   return redirect('/login')