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

Interface = NewType("Interface", Any)
Implementation = NewType("Implementation", Any)
Model = NewType("Model", Any)

from injector import Key

App = Key("App")
API = Key("API")
APISpec = Key("APISpec")
FlaskApp = Key("FlaskApp")
AppRunner = Key("AppRunner")
ConnexionConfig = Key("ConnexionConfig")
FlaskConfig = Key("FlaskConfig")
FlaskRunConfig = Key("FlaskRunConfig")
Modules = Key("Modules")
SQLAlchemyEngine = Key("SQLAlchemyEngine")
