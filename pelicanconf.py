import os
import sys

sys.path.append(os.curdir)

if os.getenv('PYCONES_BUILD_TARGET', 'LANDING').upper() == 'WEB':
    from config.web import *
else:
    from config.landing import *

SITEURL = os.getenv('SITEURL', 'http://localhost:8000')
