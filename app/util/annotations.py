''' Annotation tools
'''

import inspect
from typing import Callable

def func_to_annotations(func: Callable):
  return inspect.getfullargspec(func).annotations

def annotations_to_str(annotations: str):
  return '%s -> %s' % (
    ', '.join(
      '%s: %s' % (str(key), repr(val))
      for key, val in annotations.items()
      if key != 'return'
    ),
    repr(annotations['return']),
  )
