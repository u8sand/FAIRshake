from app.util.bind import bind

def test_bind():
  def test_func(*kargs, **kwargs):
    return sum(kargs) + sum(kwargs.values())
  bound_func = bind(test_func, 1, 2, a=1, b=2)
  assert bound_func(3, c=3) == 12
