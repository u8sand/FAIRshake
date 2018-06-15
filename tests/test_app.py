def test_app():
  import app
  from app.ioc import injector
  from app.types import App
  injector.get(App)
