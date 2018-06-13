from injector import Injector, Module, provider, singleton, inject
from ...types import App, AppRunner, FlaskApp, API, APISpec, ConnexionConfig, FlaskConfig, FlaskRunConfig
from ...ioc import injector

@injector.binder.install
class ConnexionAppModule(Module):
  @provider
  @singleton
  @inject
  def provide_app(self, api: API, api_spec: APISpec, connexion_config: ConnexionConfig, injector: Injector) -> FlaskApp:
    import connexion
    from flask_injector import FlaskInjector
    from ...util.module_resolver import ModuleResolver
    connexion_app = connexion.FlaskApp(api.__name__, **connexion_config)
    connexion_app.add_api(specification=api_spec, resolver=ModuleResolver(api))
    flask_app = connexion_app.app
    return flask_app

@injector.binder.install
class FlaskAppModule(Module):
  @provider
  @singleton
  @inject
  def provide_flask_app(self, flask_app: FlaskApp, flask_config: FlaskConfig, injector: Injector) -> App:
    from flask_injector import FlaskInjector
    FlaskInjector(app=flask_app, injector=injector)
    return flask_app

@injector.binder.install
class FlaskAppRunner(Module):
  @singleton
  @provider
  @inject
  def provide_app_runner(self, app: App, flask_run_config: FlaskRunConfig) -> AppRunner:
    from ...util.bind import bind
    return bind(app.run, **flask_run_config)
