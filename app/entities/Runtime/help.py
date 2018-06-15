from injector import Injector, Module, provider, singleton, inject
from ...ioc import injector
from ...types import Apps

class CommandLineHelp:
  def run():
    apps = injector.get(Apps)
    print('Available modules:', ', '.join(apps.keys()))

injector.binder.bind(Apps, to={'help': CommandLineHelp}, scope=singleton)
