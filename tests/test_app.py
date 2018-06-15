def test_app():
  import app
  from app.ioc import injector
  from app.types import AppRunner
  assert callable(injector.get(AppRunner))
