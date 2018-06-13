from injector import Module, provider, singleton
from ...types import ConnexionConfig, FlaskConfig, FlaskRunConfig
from ...ioc import injector

@injector.binder.install
class ConfigureModule(Module):
  @provider
  @singleton
  def provide_ConnexionConfig(self) -> ConnexionConfig:
    return dict(
      debug=True,
    )

  @provider
  @singleton
  def provide_FlaskConfig(self) -> FlaskConfig:
    return dict(
      debug=True,
    )

  @provider
  @singleton
  def provide_FlaskRunConfig(self) -> FlaskRunConfig:
    return dict(
      host='0.0.0.0',
      port=8080,
      debug=True,
      threaded=True
    )
