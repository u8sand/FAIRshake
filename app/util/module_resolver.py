import re
from .deep_getattr import deep_getattr
from connexion.resolver import Resolver

class RestyResolverEx(Resolver):
    """
    Resolves endpoint functions using REST semantics (unless overridden by specifying operationId)
    """

    def __init__(self, default_module_name, collection_endpoint_name='search', **kwargs):
        """
        :param default_module_name: Default module name for operations
        :type default_module_name: str
        """
        Resolver.__init__(self, **kwargs)
        self.default_module_name = default_module_name
        self.collection_endpoint_name = collection_endpoint_name

    def resolve_operation_id(self, operation):
        """
        Resolves the operationId using REST semantics unless explicitly configured in the spec
        :type operation: connexion.operation.Operation
        """
        if operation.operation.get('operationId'):
            return Resolver.resolve_operation_id(self, operation)

        return self.resolve_operation_id_using_rest_semantics(operation)

    def resolve_operation_id_using_rest_semantics(self, operation):
        """
        Resolves the operationId using REST semantics
        :type operation: connexion.operation.Operation
        """
        path_match = re.search(
            '^/?(?P<resource_name>([\w\-](?<!/))*)(?P<trailing_slash>/*)(?P<extended_path>.*)$', operation.path
        )

        def get_controller_name():
            x_router_controller = operation.operation.get('x-swagger-router-controller')

            name = self.default_module_name
            resource_name = path_match.group('resource_name')

            if x_router_controller:
                name = x_router_controller

            elif resource_name:
                resource_controller_name = resource_name.replace('-', '_')
                name += '.' + resource_controller_name

            return name

        def get_function_name():
            method = operation.method

            is_collection_endpoint = \
                method.lower() == 'get' \
                and path_match.group('resource_name') \
                and not path_match.group('extended_path')

            return self.collection_endpoint_name if is_collection_endpoint else method.lower()

        return '{}.{}'.format(get_controller_name(), get_function_name())

class ModuleResolver(RestyResolverEx):
  def __init__(self, module, collection_endpoint_name='search'):
    """
    :param module: Default module name for operations
    :type module: any
    """
    RestyResolverEx.__init__(
      self,
      default_module_name=module.__name__,
      collection_endpoint_name=collection_endpoint_name,
      function_resolver=self.get_function_from_name,
    )
    self.module = module

  def get_function_from_name(self, function_name):
    """
    Tries to get function by fully qualified name (e.g. "mymodule.myobj.myfunc")
    :type function_name: str
    """
    if function_name is None:
      raise ValueError("Empty function name")
    function_name_parts = function_name.split('.')
    assert function_name_parts[0] == self.module.__name__
    return deep_getattr(self.module, '.'.join(function_name_parts[1:]))
