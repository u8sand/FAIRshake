''' Import all modules in entities for their side-effects on the injector.
'''

import os
from .util.importer import walk_directory
walk_directory(os.path.dirname(__file__), 'entities', __package__)
