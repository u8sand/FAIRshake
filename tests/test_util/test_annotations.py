from app.util.annotations import func_to_annotations, annotations_to_str, annotation_subset

def test_func_to_annotations():
  def test_func(a: int, b: str, c: float) -> str:
    pass
  
  assert func_to_annotations(test_func) == {
    'a': int,
    'b': str,
    'c': float,
    'return': str,
  }

def test_func_partial_annotations():
  def test_func(a, b: str, c: float) -> str:
    pass
  
  assert func_to_annotations(test_func) == {
    'a': None,
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

def test_annotation_subset():
  def test_func_iface(a: int, b: str, c: float) -> str:
    pass
  
  def test_func_impl(a, b: str, c, d: int) -> str:
    pass
  
  def test_func_bad_impl(a, b: float, c, d: int) -> str:
    pass

  assert annotation_subset(test_func_iface, test_func_impl), "Good implementation was successful"
  assert not annotation_subset(test_func_iface, test_func_bad_impl), "Bad implementation wasn't caught"

