from injector import Module, Key, provider, singleton, inject
from ...types import SQLAlchemy, SQLAlchemyBase
from ...ioc import injector

SQLAlchemyEngine = Key("SQLAlchemyEngine")

@injector.binder.install
class SQLAlchemyModule(Module):
  @provider
  @singleton
  def provide_SQLAlchemyEngine(self, base: SQLAlchemyBase, config: Config) -> SQLAlchemyEngine:
    import os
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    engine = create_engine(config['sqlalchemy_uri'])
    for b in base:
      b.metadata.create_all(engine)
    return engine
  
  @provider
  @singleton
  @inject
  def provide_SQLAlchemy(self, engine: SQLAlchemyEngine) -> SQLAlchemy:
    from sqlalchemy.orm import sessionmaker
    return sessionmaker(bind=engine)
