from injector import Module, provider, singleton, inject
from ...types import App, Apps, Config
from ...ioc import injector

@injector.binder.install
class AppModule(Module):
  @provider
  @singleton
  @inject
  def provide_app(self, apps: Apps, config: Config) -> App:
    return apps.get(config['module'], apps['help'])
