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

from injector import Key, SequenceKey

API = Key("API")
APISpec = Key("APISpec")
App = Key("App")
AppRunner = Key("AppRunner")
Config = Key("Config")
FlaskApp = Key("FlaskApp")
OIDC = Key("OIDC")
SQLAlchemy = Key("SQLAlchemy")
SQLAlchemyBase = SequenceKey("SQLAlchemyBase")
