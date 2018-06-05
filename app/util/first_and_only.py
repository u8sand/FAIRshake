from typing import Any, Iterable

def first(iterable: Iterable[Any]) -> Any:
  return next(iter(iterable))

def first_and_only(iterable: Iterable[Any]) -> Any:
  ''' Get the first element of an iterable asserting it is the only element.
  '''
  try:
    it = iter(iterable)
    val = next(it)
    try:
      next(it)
      raise Exception("Iterable contained more than one element.")
    except StopIteration:
      return val
  except StopIteration:
    raise Exception("Iterable was empty.")
