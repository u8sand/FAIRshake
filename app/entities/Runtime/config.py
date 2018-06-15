from injector import Module, Key, provider, singleton, inject
from ...util.filter_none_kwargs import filter_none_kwargs
from ...types import Config
from ...ioc import injector

Environment = Key("Environment")
CommandLine = Key("CommandLine")
Defaults = Key("Defaults")

@injector.binder.install
class ConfigureModule(Module):
  @provider
  @singleton
  def provide_environment(self) -> Environment:
    import os
    return os.environ
  
  @provider
  @singleton
  def provide_cmdline(self) -> CommandLine:
    import sys
    from ...util.command_line_parse import parse
    return parse(sys.argv)

  @provider
  @singleton
  def provide_defaults(self) -> Defaults:
    import os
    from binascii import hexlify
    return dict(
      module='app.entities.FAIRshakeWeb.view',
      debug=True,
      host='0.0.0.0',
      port=8080,
      threaded=True,
      https=True,
      flask_secret_key='143u89hersadsdihnjksdnf',
      flask_session_type='filesystem',
      oidc_secrets='client_secrets.json',
      oidc_scopes=['openid', 'email'],
      sqlalchemy_uri='sqlite3:///FAIRshake.db',
    )

  @provider
  @singleton
  @inject
  def provide_config(self, cmd: CommandLine, environ: Environment, defaults: Defaults) -> Config:
    kargs, kwargs = cmd
    return filter_none_kwargs({
      k: kwargs.get(k, environ.get(k, v))
      for k, v in defaults.items()
    }, module=kargs[1] if len(kargs) > 1 else None)
