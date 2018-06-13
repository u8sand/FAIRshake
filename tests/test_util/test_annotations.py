from app.util.annotations import func_to_annotations, annotations_to_str

def test_func_to_annotations():
  def test_func(a: int, b: str, c: float) -> str:
    pass
  
  assert func_to_annotations(test_func) == {
    'a': int,
    'b': str,
    'c': float,
    'return': str,
  }

def test_annotations_to_str():
  import re
  from collections import OrderedDict
  desc = annotations_to_str(OrderedDict([
    ('return', str,),
    ('a', int,),
    ('b', str,),
    ('c', float,),
  ]))
  assert re.match(
    r'a: .*int.*, b: .*str.*, c: .*float.* -> .*str.*',
    desc,
  ) is not None, desc
