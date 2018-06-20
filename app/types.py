''' Application types for static type checking
'''

from typing import (
  Any,
  Dict,
  Generator,
  Generic,
  List,
  NewType,
  Optional,
  Tuple,
  Type,
  TypeVar,
)

UUID = NewType("UUID", str)
HTML = NewType("HTML", str)
ContentType = NewType("ContentType", str)
Timestamp = NewType("Timestamp", str)
# HTTPResponse = NewType("HTTPResponse", str)
T = TypeVar('T')

class HTTPResponse(Generic[T]):
  pass

Interface = NewType("Interface", object)
Implementation = NewType("Implementation", object)
Model = NewType("Model", object)

from injector import Key, MappingKey, SequenceKey

API = Key("API")
APISpec = Key("APISpec")
App = Key("App")
Apps = MappingKey("Apps")
CommandLine = Key("CommandLine")
Config = Key("Config")
Defaults = Key("Defaults")
Environment = Key("Environment")
FlaskApp = Key("FlaskApp")
OIDC = Key("OIDC")
SQLAlchemy = Key("SQLAlchemy")
SQLAlchemyBase = SequenceKey("SQLAlchemyBase")
