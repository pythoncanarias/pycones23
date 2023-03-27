
import collections

AUTHOR = 'python españa'
SITENAME = 'pycones23'
SITEURL = 'http://localhost:8080'

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
    'ciudad.html': 'ciudad.html',
    'codigo_conducta.html': 'codigo_conducta.html',
    'c4p.html': 'c4p.html',
    'ediciones_anteriores.html': 'ediciones_anteriores.html',
}
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True



TITLE = "PyConES 2023"


## EDICIONES PASADAS
PAST_EDITIONS=[
 {
        "name": "PyConES 2013 - Madrid",
        "logo": "theme/assets/images/past_editions/2013.png",
        "url": "https://2013.es.pycon.org/",
    },
    {
        "name": "PyConES 2014 - Zaragoza",
        "logo": "theme/assets/images/past_editions/2014.png",
        "url": "https://2014.es.pycon.org/",
    },
    {
        "name": "PyConES 2015 - Valencia",
        "logo": "theme/assets/images/past_editions/2015.png",
        "url": "https://2015.es.pycon.org/",
    },
    {
        "name": "PyConES 2016 - Almería",
        "logo": "theme/assets/images/past_editions/2016.jpg",
        "url": "https://2016.es.pycon.org/",
    },
    {
        "name": "PyConES 2017 - Cáceres",
        "logo": "theme/assets/images/past_editions/2017.png",
        "url": "https://2017.es.pycon.org/",
    },
    {
        "name": "PyConES 2018 - Málaga",
        "logo": "theme/assets/images/past_editions/2018.png",
        "url": "https://2018.es.pycon.org/",
    },
    {
        "name": "PyConES 2019 - Alicante",
        "logo": "theme/assets/images/past_editions/2019.png",
        "url": "https://2019.es.pycon.org/",
    },
    {
        "name": "PyConES 2020 - Pandemic Edition",
        "logo": "theme/assets/images/past_editions/2020.png",
        "url": "https://2020.es.pycon.org/",
    },
    {
        "name": "PyConES 2021 - Vaccine Edition",
        "logo": "theme/assets/images/past_editions/2021.png",
        "url": "https://2021.es.pycon.org/",
    },
    {
        "name": "PyConES 2022 - Granada",
        "logo": "theme/assets/images/past_editions/2022.png",
        "url": "https://2022.es.pycon.org/",
    },
    ]

## CALL FOR SPONSORS

SPONSORS_DOSSIER_ES="" 
SPONSORS_DOSSIER_EN=""


## CALL FOR PAPERS

C4P_LINK="https://pretalx.com/orga/event/pycones-2023/"


## PATROCINIOS

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
