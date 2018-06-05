from dataclasses import dataclass

def model(mod):
  ''' A decorator for model registration.
  '''
  assert mod.__doc__, '%s does not have a docstring' % (mod)
  return dataclass(model)

def interface(iface):
  ''' A decorator for interface registration.
  '''
  assert iface.__doc__, '%s does not have a docstring' % (iface)
  for attr in dir(iface):
    if callable(attr):
      assert attr.__doc__, '%s does not have a docstring' % (iface)
  return iface
