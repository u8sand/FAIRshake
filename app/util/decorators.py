from dataclasses import dataclass

def model(mod):
  ''' A decorator for model registration.
  '''
  assert mod.__doc__, '%s does not have a docstring' % (mod)
  return dataclass(mod)

def interface(iface):
  ''' A decorator for interface registration.
  '''
  assert iface.__doc__, '%s does not have a docstring' % (iface)
  for attr in dir(iface):
    if callable(attr):
      assert attr.__doc__, '%s does not have a docstring' % (iface)
  return iface

def implements(iface):
  ''' A decorator for asserting that an implementation fully implements its interface/model.
  '''
  def implements_decorator(impl):
    try:
      setattr(impl, '__doc__', iface.__doc__)
    except:
      pass
    for attr in dir(iface):
      if attr.startswith('_'):
        continue
      assert getattr(impl, attr, None) is not None, '%s does not implement %s.%s' % (impl.__name__, iface.__name__, attr)
      try:
        setattr(getattr(impl, attr), '__doc__', getattr(iface, attr).__doc__)
      except:
        pass
    return impl
  return implements_decorator
