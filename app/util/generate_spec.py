import re
import yaml
from .first_and_only import first

space_re = re.compile(r'^( +?)[^ ].+$')
spec_ptr = re.compile(r'{(?P<mod>.+?)(__(?P<attr>.+))?}')

def yml_doc_2_json(doc):
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

def generate_spec(doc, objs):
  ''' Create a full specification following reference
  doc pointers. For an example, see `test_generate_spec.py`
  '''
  print('generate_spec({doc}, {objs})'.format(**locals()))
  sub_specs = {}
  for ref in spec_ptr.finditer(doc):
    assert ref.group('mod') in objs.keys(), ref
    if ref.group('attr') is not None:
      assert ref.group('attr') in dir(objs[ref.group('mod')])
      sub_specs[ref.group('mod')+'__'+ref.group('attr')] = generate_spec(
        getattr(
          objs[ref.group('mod')],
          ref.group('attr')
        ).__doc__,
        objs,
      )
    else:
      sub_specs[ref.group('mod')] = generate_spec(
        objs[ref.group('mod')].__doc__,
        objs,
      )
  return yml_doc_2_json(doc.format(**sub_specs))
