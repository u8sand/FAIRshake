from injector import Module, provider, singleton, inject
from flask_oidc import OpenIDConnect
from ...types import OAuth, FlaskApp
from ...ioc import injector

@injector.binder.install
class OAuthModule(Module):
  @provider
  @singleton
  def provide_OAuth(self, flask_app: FlaskApp) -> OAuth:
    return OpenIDConnect(flask_app)
