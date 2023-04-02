import collections

AUTHOR = 'Python España'
SITENAME = 'pycones23'
SITEURL = 'http://localhost:8080'

PATH = 'content'

TIMEZONE = 'Atlantic/Canary'

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
    'organizacion.html': 'organizacion.html',
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

C4P_LINK="https://charlas.2023.es.pycon.org"


## PATROCINIOS
PLANES = [
    {
        "key": "teide",
        "titulo": "Teide",
        "altura": "3.7 km",
        "image": "theme/assets/images/patrocinios/teide_oro.png",
    },
    {
        "key": "tamadaba",
        "titulo": "Tamadaba",
        "altura": "1.4 km",
        "image": "theme/assets/images/patrocinios/tamadaba_zafiro.png",
    },
    {
        "key": "teneguia",
        "titulo": "Teneguia",
        "altura": "430 m",
        "image": "theme/assets/images/patrocinios/teneguia_gema.png",
    },
    {
        "key": "timanfaya",
        "titulo": "Timanfaya",
        "altura": "370 m",
        "image": "theme/assets/images/patrocinios/timanfaya_cobre.png",
    },
]

BENEFICIOS = [
    {
        "titulo": "Descuento entradas",
        "teide": "20%",
        "tamadaba": "15%",
        "teneguia": "10%",
        "timanfaya": "5%",
    },
    {
        "titulo": "Logo en la Web",
        "teide": True,
        "tamadaba": True,
        "teneguia": True,
        "timanfaya": True,
    },
    {
        "titulo": "Obsequio paquete bienvenida",
        "teide": True,
        "tamadaba": True,
        "teneguia": True,
        "timanfaya": True,
    },
    {
        "titulo": "Acceso Add-ons",
        "teide": True,
        "tamadaba": True,
        "teneguia": True,
        "timanfaya": True,
    },
    {
        "titulo": "Publicaciones en RRSS",
        "teide": True,
        "tamadaba": True,
        "teneguia": True,
        "timanfaya": True,
    },
    {
        "titulo": "Publicar ofertas de trabajo",
        "teide": True,
        "tamadaba": True,
        "teneguia": True,
        "timanfaya": True,
    },
    {
        "titulo": "Folleto en paquete bienvenida",
        "teide": True,
        "tamadaba": True,
        "teneguia": True,
        "timanfaya": False,
    },
    {
        "titulo": "Logo cartelería",
        "teide": True,
        "tamadaba": True,
        "teneguia": True,
        "timanfaya": False,
    },
    {
        "titulo": "Anuncio en programa",
        "teide": True,
        "tamadaba": True,
        "teneguia": True,
        "timanfaya": False,
    },
    {
        "titulo": "Stand",
        "teide": True,
        "tamadaba": True,
        "teneguia": True,
        "timanfaya": False,
    },
    {
        "titulo": "Logo newsletter",
        "teide": True,
        "tamadaba": True,
        "teneguia": True,
        "timanfaya": False,
    },
    {
        "titulo": "Logo al proyectar en pausas",
        "teide": True,
        "tamadaba": True,
        "teneguia": False,
        "timanfaya": False,
    },
    {
        "titulo": "Charla Patrocinada",
        "teide": True,
        "tamadaba": True,
        "teneguia": False,
        "timanfaya": False,
    },
    {
        "titulo": "Agradecimiento en vivo",
        "teide": True,
        "tamadaba": True,
        "teneguia": False,
        "timanfaya": False,
    },
    {
        "titulo": "Notas de prensa",
        "teide": True,
        "tamadaba": True,
        "teneguia": False,
        "timanfaya": False,
    },
    {
        "titulo": "Miembro jurado",
        "teide": True,
        "tamadaba": False,
        "teneguia": False,
        "timanfaya": False,
    },
    {
        "titulo": "Entrega premio",
        "teide": True,
        "tamadaba": False,
        "teneguia": False,
        "timanfaya": False,
    }
]


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


### NOTICIAS

NOTICIAS = [
    {
        "titulo":"¡Lanzamiento del sitio web!",
        "fecha":"2023.03.XX",
        "contenido":"Ya hemos publicado la primera versión del sitio web de la conferencia con algunas secciones importantes para las personas interesadas en participar. Estaremos publicando más actualizaciones en las siguientes semanas",
    },
        {
        "titulo":"¡Lanzamiento del sitio web!",
        "fecha":"2023.03.XX",
        "contenido":"Ya hemos publicado la primera versión del sitio web de la conferencia con algunas secciones importantes para las personas interesadas en participar. Estaremos publicando más actualizaciones en las siguientes semanas",
    },

    ]

ORG = [
    {
        "name": "Álex Samarín",
        "title": "Technical Lead",
        "img": "theme/assets/images/org/alex.jpg",
        "community": "Python Canarias",
        "wg": ["Infraestructura", "Voluntariado"],
        "github_username": "",
        "twitter_username": "SamarinAlex",
        "mastodon_url": "",
        "linkedin_url": "",
    },
    {
        "name": "Andrés Orcajo",
        "title": "...",
        "img": "",
        "community": "",
        "wg": ["Infraestructura", "Voluntariado"],
        "github_username": "",
        "twitter_username": "",
        "mastodon_url": "",
        "linkedin_url": "",
    },
    {
        "name": "Carlos Sosa",
        "title": "Software Developer",
        "img": "theme/assets/images/org/sosa.jpg",
        "community": "Python Canarias",
        "wg": ["Web"],
        "github_username": "",
        "twitter_username": "",
        "mastodon_url": "",
        "linkedin_url": "https://www.linkedin.com/in/carlos-sosa-hdez/",
    },
    {
        "name": "Cristián Maureira-Fredes",
        "title": "Senior R&D Manager",
        "img": "theme/assets/images/org/cristian.jpg",
        "community": "Python España",
        "wg": ["Programa", "Patrocinios", "Web"],
        "github_username": "cmaureir",
        "twitter_username": "cmaureir",
        "mastodon_url": "https://mastodon.social/@cmaureir",
        "linkedin_url": "https://www.linkedin.com/in/cmaureir/",
    },
    {
        "name": "Christian Prada Osuna",
        "title": "Technical Lead Software Developer",
        "img": "theme/assets/images/org/christian.jpeg",
        "community": "Python Granada",
        "wg": ["Patrocinios"],
        "github_username": "cprada87",
        "twitter_username": "dev_morphheus",
        "mastodon_url": "",
        "linkedin_url": "https://es.linkedin.com/in/christian-prada-osuna-0741217b",
    },
    {
        "name": "Esther",
        "title": "Software Developer",
        "img": "theme/assets/images/org/esther.jpg",
        "community": "",
        "wg": ["Voluntariado"],
        "github_username": "EstherJP",
        "twitter_username": "estherxjp",
        "mastodon_url": "",
        "linkedin_url": "https://es.linkedin.com/in/esther-jorge-paramio-275567198",
    },
    {
        "name": "Fran Escobar González",
        "title": "Senior Backend developer",
        "img": "theme/assets/images/org/fran.jpg",
        "community": "Python Canarias",
        "wg": ["Programa", "Patrocinios"],
        "github_username": "",
        "twitter_username": "sheikLoves",
        "mastodon_url": "",
        "linkedin_url": "",
    },
    {
        "name": "Javier Alonso Silva",
        "title": "Ingeniero I+D en Teldat",
        "img": "theme/assets/images/org/javi.jpeg",
        "community": "Python España",
        "wg": ["Diversidad", "Patrocinios", "Web"],
        "github_username": "Javinator9889",
        "twitter_username": "Javinator9889",
        "mastodon_url": "",
        "linkedin_url": "https://linkedin.com/in/javinator9889",
    },
    {
        "name": "Jesús Torres Jorge",
        "title": "Profesor y Director Académico",
        "img": "theme/assets/images/org/jesus.jpg",
        "community": "",
        "wg": ["Diversidad", "Infraestructura", "Patrocinios", "Voluntariado"],
        "github_username": "jesustorresdev",
        "twitter_username": "jesustorresdev",
        "mastodon_url": "",
        "linkedin_url": "https://www.linkedin.com/in/jesusmtorres/",
    },
    {
        "name": "Jimena E. Bermúdez",
        "title": "Ingeniera de Software",
        "img": "theme/assets/images/org/jimena.jpeg",
        "community": "PyLadies",
        "wg": ["Diversidad"],
        "github_username": "JimenaEB",
        "twitter_username": "jimena_y_yo",
        "mastodon_url": "",
        "linkedin_url": "https://www.linkedin.com/in/jimena-eb/",
    },
    {
        "name": "Johanna Sanchez",
        "title": "Fullstack Developer y Química",
        "img": "theme/assets/images/org/johanna.jpg",
        "community": "Python España",
        "wg": ["Diversidad", "Redes sociales", "Patrocinios", "Web"],
        "github_username": "",
        "twitter_username": "EllaQuimica",
        "mastodon_url": "",
        "linkedin_url": "https://www.linkedin.com/in/johanna-sanchez-vallejo/",
    },
    {
        "name": "Juan Ignacio Rodríguez de León",
        "title": "Python Developer",
        "img": "theme/assets/images/org/jileon.jpg",
        "community": "Python Canarias",
        "wg": ["Infraestructura", "Web"],
        "github_username": "euribates",
        "twitter_username": "",
        "mastodon_url": "https://tkz.one/@euribates",
        "linkedin_url": "https://linkedin.com/in/jileon",
    },
    {
        "name": "Lucía Cabrera Garabote",
        "title": "Estudiante de Ingeniería Informática",
        "img": "theme/assets/images/org/lucia.jpg",
        "community": "",
        "wg": ["Patrocinios", "Voluntariado"],
        "github_username": "",
        "twitter_username": "lucdevmind03",
        "mastodon_url": "",
        "linkedin_url": "",
    },
    {
        "name": "Nazaret Miranda López",
        "title": "Software Developer",
        "img": "theme/assets/images/org/nazaret.jpg",
        "community": "AdaLoveDev",
        "wg": ["Voluntariado"],
        "github_username": "",
        "twitter_username": "",
        "mastodon_url": "",
        "linkedin_url": "https://www.linkedin.com/in/zaretmir/",
    },
    {
        "name": "Pablo Benavides",
        "title": "Modelador de transportes",
        "img": "theme/assets/images/org/pablo.jpeg",
        "community": "Python Granada",
        "wg": ["Programa", "Patrocinios"],
        "github_username": "PybloBenavides",
        "twitter_username": "",
        "mastodon_url": "",
        "linkedin_url": "",
    },
    {
        "name": "Jose Torres Aguera",
        "title": "Technical Leader",
        "img": "theme/assets/images/org/pepe.jpg",
        "community": "Python Málaga",
        "wg": ["Infraestructura", "Patrocinios", "Web"],
        "github_username": "jata84",
        "twitter_username": "Jata1984",
        "mastodon_url": "",
        "linkedin_url": "",
    },
    {
        "name": "Samuel López Santamaría",
        "title": "Senior Data Scientist",
        "img": "theme/assets/images/org/samuel.jpg",
        "community": "",
        "wg": ["Programa", "Infraestructura", "Patrocinios"],
        "github_username": "",
        "twitter_username": "",
        "mastodon_url": "",
        "linkedin_url": "https://www.linkedin.com/in/slopezsantamaria/",
    },
    {
        "name": "Sara Medrano Sánchez",
        "title": "...",
        "img": "theme/assets/images/org/sara.jpeg",
        "community": "",
        "wg": ["Programa", "Diversidad", "Infraestructura", "Redes Sociales", "Patrocinios", "Web", "Voluntariado"],
        "github_username": "",
        "twitter_username": "SrtSanz_",
        "mastodon_url": "",
        "linkedin_url": "",
    },
    {
        "name": "Sergio Delgado Quintero",
        "title": "Ingeniero Informático y Profesor",
        "img": "theme/assets/images/org/sergio.jpg",
        "community": "Python Canarias",
        "wg": ["Infraestructura", "Redes Sociales", "Web"],
        "github_username": "sdelquin",
        "twitter_username": "sdelquin",
        "mastodon_url": "",
        "linkedin_url": "https://www.linkedin.com/in/sdelquin",
    },
    {
        "name": "Silvia García Hernández",
        "title": "Estudiante",
        "img": "",
        "community": "",
        "wg": ["Diversidad", "Redes Sociales", "Voluntariado"],
        "github_username": "",
        "twitter_username": "",
        "mastodon_url": "",
        "linkedin_url": "",
    },
    {
        "name": " Victor Vicente-Palacios",
        "title": "Clinical Data Scientist",
        "img": "theme/assets/images/org/victor.jpg",
        "community": "",
        "wg": ["Programa", "Diversidad"],
        "github_username": "victorvicpal",
        "twitter_username": "victorvicpal",
        "mastodon_url": "https://dair-community.social/@victorvicpal",
        "linkedin_url": "https://www.linkedin.com/in/victorvicpal/",
    },
    {
        "name": "Yodra López Herrera",
        "title": "Software Developer",
        "img": "theme/assets/images/org/yodra.jpg",
        "community": "AdaLoveDev",
        "wg": ["Programa", "Diversidad", "Infraestructura", "Patrocinios", "Voluntariado"],
        "github_username": "",
        "twitter_username": "yodralopez",
        "mastodon_url": "",
        "linkedin_url": "https://www.linkedin.com/in/yodralopez",
    },
]
# Shuffle team per deployment
import random
random.shuffle(ORG)
