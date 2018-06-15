from injector import Injector, Module, provider, singleton, inject
from flask_injector import FlaskInjector
from ...types import App, AppRunner, FlaskApp, API, APISpec, Config, OIDC
from ...ioc import injector
from ...util.filter_none_kwargs import filter_none_kwargs

@injector.binder.install
class ConnexionAppModule(Module):
  @provider
  @singleton
  @inject
  def provide_app(self, api: API, api_spec: APISpec, config: Config, injector: Injector) -> FlaskApp:
    import connexion
    from ...util.module_resolver import ModuleResolver
    connexion_app = connexion.FlaskApp(api.__name__, **filter_none_kwargs(
      debug=config['debug']
    ))
    connexion_app.add_api(specification=api_spec, resolver=ModuleResolver(api))
    flask_app = connexion_app.app
    return flask_app

@injector.binder.install
class FlaskAppModule(Module):
  @provider
  @singleton
  @inject
  def provide_flask_app(self, flask_app: FlaskApp, oidc: OIDC, config: Config, injector: Injector) -> App:
    # Configure
    flask_app.secret_key = config['flask_secret_key']
    flask_app.config.update(filter_none_kwargs(**{
      'DEBUG': config['debug'],
      'OIDC_CLIENT_SECRETS': config['oidc_secrets'],
      'OIDC_SCOPES': config['oidc_scopes'],
      'SESSION_TYPE': config['flask_session_type'],
    }))

    # Initialize extensions
    oidc.init_app(flask_app)

    # Attach injector
    FlaskInjector(app=flask_app, injector=injector)

    return flask_app

@injector.binder.install
class FlaskAppRunner(Module):
  @singleton
  @provider
  @inject
  def provide_app_runner(self, app: App, config: Config) -> AppRunner:
    from ...util.bind import bind
    # TODO: make App a MappingKey and use command-line[0]
    return bind(app.run, **filter_none_kwargs(
      host=config['host'],
      port=config['port'],
      debug=config['debug'],
      threaded=config['threaded'],
      ssl_context='adhoc' if config['https'] else None,
    ))
