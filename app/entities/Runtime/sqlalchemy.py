from injector import Module, provider, singleton, inject
from ...types import SQLAlchemy, SQLAlchemyBase, SQLAlchemyEngine
from ...ioc import injector

@injector.binder.install
class SQLAlchemyModule(Module):
  @provider
  @singleton
  def provide_SQLAlchemyEngine(self, base: SQLAlchemyBase) -> SQLAlchemyEngine:
    import os
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    engine = create_engine(os.environ.get('DB_URI', 'sqlite:///FAIRshake.db'))
    for b in base:
      b.metadata.create_all(engine)
    return engine
  
  @provider
  @singleton
  @inject
  def provide_SQLAlchemy(self, engine: SQLAlchemyEngine) -> SQLAlchemy:
    from sqlalchemy.orm import sessionmaker
    return sessionmaker(bind=engine)
