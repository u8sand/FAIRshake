import functools

def deep_getattr(obj, attr):
  """
  Recurses through an attribute chain to get the ultimate value.
  Stolen from http://pingfive.typepad.com/blog/2010/04/deep-getattr-python-function.html
  """
  return functools.reduce(getattr, attr.split('.'), obj)
