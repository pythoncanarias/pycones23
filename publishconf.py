# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)


SITEURL = os.getenv('SITEURL', 'https://2023.es.pycon.org/')

if (build_target := os.getenv('PYCONES_BUILD_TARGET', 'LANDING')) == 'WEB':
    from pelicanconf import *
else:
    from pelicanconf_landing import *
print(f'==> Building {build_target} <==')

# If your site is available via HTTPS, make sure SITEURL begins with https://
RELATIVE_URLS = False

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

# DISQUS_SITENAME = ""
# GOOGLE_ANALYTICS = ""
