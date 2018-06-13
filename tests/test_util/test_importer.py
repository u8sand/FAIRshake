from app.util.importer import walk_directory

def test_walk_directory():
  walk_directory(os.path.dirname(__name__), 'test_importer', __package__)
  from test_importer import register
  assert sum(register) == 3
