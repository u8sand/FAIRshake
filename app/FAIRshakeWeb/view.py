from flask import Flask, render_template
from interfaces.Repository import RepositoryAPI

app = Flask(__name__)

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
    projects=repository.get(limit=10),
  )

@app.route('/start_project', methods=['GET'])
def start_project():
  return render_template('start_project.html')

@app.route('/bookmarklet', methods=['GET'])
def bookmarklet():
  return render_template('bookmarklet.html')

@app.route('/chrome_extension', methods=['GET'])
def chrome_extension():
  return render_template('chrome_extension.html')

@app.route('/register', methods=['GET'])
def register():
  return render_template('register.html')

@app.route('/login', methods=['GET'])
def login():
  return render_template('login.html')
