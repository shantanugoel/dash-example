import os

from .common import *

if os.getenv('ENABLE_DASH_PROD', False) == True:
  from .prod import *
else:
  from .dev import *
