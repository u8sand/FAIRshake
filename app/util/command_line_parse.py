import re
import json
from typing import (
  Optional,
  Any,
  List,
  Tuple,
  Mapping,
)

def json_with_fallback(s: Optional[str]) -> Any:
  if s is None:
    return True
  try:
    return json.loads(s)
  except:
    return s

kwarg_re = re.compile(r'^--(?P<key>.+?)(=(?P<val>.+))?$')

def parse(args: List[str]) -> Tuple[List[str], Mapping[str, str]]:
  kargs = []
  kwargs = {}

  for arg in args:
    m = kwarg_re.match(arg)
    if m:
      kwargs[m.group('key')] = json_with_fallback(m.group('val'))
    else:
      kargs.append(json_with_fallback(arg))

  return (kargs, kwargs)
