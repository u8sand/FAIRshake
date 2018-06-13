''' Annotation tools
'''

import inspect
from typing import Callable

def func_to_annotations(func: Callable):
  argspec = inspect.getfullargspec(func)

  return dict(
    {k: None for k in argspec.args},
    **argspec.annotations
  )

def annotations_to_str(annotations: str):
  return '%s -> %s' % (
    ', '.join(
      '%s: %s' % (str(key), repr(val))
      for key, val in annotations.items()
      if key != 'return'
    ),
    repr(annotations['return']),
  )

def annotation_subset(iface: Callable, impl: Callable):
  iface_annotations = func_to_annotations(iface)
  impl_annotations = func_to_annotations(impl)
  for k, v in impl_annotations.items():
    if iface_annotations.get(k, None) is not None:
      if v is not None and v is not iface_annotations[k]:
        return False
      del iface_annotations[k]
  return iface_annotations == {}
