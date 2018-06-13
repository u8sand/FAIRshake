''' Global injector instance and decorator helpers
'''

from injector import Injector, singleton

injector = Injector()
injector.binder.bind(Injector, to=injector, scope=singleton)

from .util.annotations import func_to_annotations, annotations_to_str, annotation_subset
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
  def not_constructable(self):
    raise Exception("Interfaces are not constructable (%s)" % (iface.__name__))
  iface.__init__ = not_constructable
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
      iface_attr = getattr(iface, attr, None)
      impl_attr = getattr(impl, attr, None)
      assert impl_attr is not None, '%s does not implement %s.%s' % (impl.__name__, iface.__name__, attr)

      if callable(impl_attr):
        assert annotation_subset(iface_attr, impl_attr), '%s does not implement %s.%s\n%s != %s' % (
          impl.__name__, iface.__name__, attr,
          annotations_to_str(func_to_annotations(impl_attr_annotations)),
          annotations_to_str(func_to_annotations(impl_attr_annotations_with_iface_attr_annotations)),
        )

        try:
          setattr(impl_attr, '__doc__', iface_attr.__doc__)
        except:
          pass
    injector.binder.bind(iface, to=impl, scope=singleton)
    return impl
  return implements_decorator
