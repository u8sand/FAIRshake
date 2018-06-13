
from injector import Module, provider, singleton, inject
from ...types import FlaskApp
from ...ioc import injector

@injector.binder.install
class FAIRshakeWeb(Module):
  @singleton
  @provider
  def provide_web_app(self) -> FlaskApp:
    from .view import app
    return app
