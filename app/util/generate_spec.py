import re
import yaml
from .deep_getattr import deep_getattr
from .first_and_only import first

space_re = re.compile(r'^( +?)[^ ].+$')
spec_ptr = re.compile(r'{(?P<mod>.+?)(__(?P<attr>.+))?}')

def yml_to_json(doc):
  '''
  Convert a yml doc to a json ignoring leading spaces
    (for source docstrings)
  '''
  spaces = len(space_re.match(first(
    line
    for line in doc.splitlines()
    if line.strip() != ''
  )).group(1))

  return yaml.load('\n'.join(
    line[spaces:]
    for line in doc.splitlines()
  ))

def json_to_yml(obj):
  ''' Dump the json specification as yml.
  '''
  return yaml.dump(obj, default_flow_style=False)

def docs_of(objs):
  return {name: obj.__doc__ for name, obj in objs.items()}

def generate_spec(obj, objs={}):
  ''' Create a full specification following reference
  doc pointers. For an example, see `test_generate_spec.py`
  '''
  doc = obj.__doc__
  docs = {}
  objs = dict(objs, **{obj.__name__: obj})
  for ref in spec_ptr.finditer(doc):
    assert ref.group('mod') in objs.keys(), ref
    if ref.group('attr') is not None:
      attr = deep_getattr(objs[ref.group('mod')], ref.group('attr').replace('__', '.'))
      docs[ref.group('mod')+'__'+ref.group('attr')] = generate_spec(attr, objs)
    else:
      docs[ref.group('mod')] = generate_spec(objs[ref.group('mod')], objs)
  return yml_to_json(doc.format(**docs))
