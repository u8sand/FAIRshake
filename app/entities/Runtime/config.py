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
    return parse(sys.argv[1:])

  @provider
  @singleton
  def provide_defaults(self) -> Defaults:
    import os
    from binascii import hexlify
    return dict(
      module='FAIRshakeWeb',
      debug=True,
      host='0.0.0.0',
      port=8080,
      threaded=True,
      https=True,
      flask_secret_key='143u89hersadsdihnjksdnf',
      flask_session_type='filesystem',
      oidc_secrets='client_secrets.json',
      oidc_scopes=['openid', 'email'],
    )

  @provider
  @singleton
  @inject
  def provide_config(self, cmd: CommandLine, environ: Environment, defaults: Defaults) -> Config:
    return filter_none_kwargs({
      k: cmd[1].get(k, environ.get(k, v))
      for k, v in defaults.items()
    }, module=cmd[0])
