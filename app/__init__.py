'''
Global injector
'''

from injector import Injector, singleton
injector = Injector()
injector.binder.bind(Injector, to=injector, scope=singleton)

import os
from .util.importer import walk_directory
walk_directory(os.path.dirname(__file__), 'entities', __package__)
