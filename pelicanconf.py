
import collections

AUTHOR = 'python españa'
SITENAME = 'pycones23'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Madrid'

DEFAULT_LANG = 'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

THEME="theme/pycones23"


TEMPLATE_PAGES = {
    'patrocinios.html': 'patrocinios.html',
    'principal.html': 'principal.html',
}
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True



TITLE = "PyConES 2023"


PATROCINIOS_CAT_A="CAT A"
PATROCINIOS_CAT_B="CAT B"



PATROCINADORES ={ 
    PATROCINIOS_CAT_A:[{
        "nombre":"PSF",
        "logo":"https://2022.es.pycon.org/theme/images/sponsors/psf.png",
        "enlace":"https://www.python.org/psf/",
    },
    {
        "nombre":"Europython",
        "logo":"https://2022.es.pycon.org/theme/images/sponsors/europython.png",
        "enlace":"https://www.europython-society.org/",
    }],
    PATROCINIOS_CAT_B:[{  
        "nombre":"PyconEs",
        "logo":"https://2022.es.pycon.org/theme/images/pythonES.svg",
        "enlace":"https://es.python.org/",
    }],


}
