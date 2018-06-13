
from injector import Module, provider, singleton, inject
from ...util.types import FlaskApp
from ... import injector

@injector.binder.install
class FAIRshakeWeb(Module):
  @singleton
  @provider
  def provide_web_app(self) -> FlaskApp:
    from .view import app
    return app
