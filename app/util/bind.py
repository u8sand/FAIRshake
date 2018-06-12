def bind(func, *kargs, **kwargs):
  ''' Bind values to a function's arguments returning a simplified function.
  '''
  def bind_wrapper(*kargs_, **kwargs_):
    return func(*kargs_, *kargs, **kwargs, **kwargs_)
  bind_wrapper.__name__ = func.__name__
  return bind_wrapper
