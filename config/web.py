import random


AUTHOR = 'Python España'
SITENAME = 'PyConES23'

PATH = 'content'
OUTPUT_PATH = 'output'
ARTICLE_SAVE_AS = '{slug}.html'
ARTICLE_URL = '{slug}.html'

TIMEZONE = 'Atlantic/Canary'

DEFAULT_LANG = 'es'

THEME = "theme/pycones23"

PLUGINS =["i18n_subsites"]

NAV_VALUES = [
    {"slug": "ciudad", "text": "Ciudad"},
    {"slug": "viaje", "text": "Viaje"},
    {"slug": "patrocinios", "text": "Patrocinios"},
    {"slug": "c4p", "text": "Llamado de Propuestas"},
    {"slug": "faq", "text": "Preguntas frecuentes"},
]

# i18n
# - We are using the simple option but more difficult to maintain
#   approach which is using two templates, one for each language.
# - We have two options to provide information for the subsite,
#   we either override the variable like 'CRONOGRAMA' with English
#   content, or we could provide structures with a simple 'en' and
#   'es' sections, like NOTICIAS (further down)
I18N_SUBSITES = {
        'en': {
            'SITENAME': 'PyConES23 - EN',
            'OUTPUT_PATH': 'output/en',
            'THEME': "theme/pycones23_en",
            'NAV_VALUES':  [
                {"slug": "ciudad", "text": "City"},
                {"slug": "viaje", "text": "Trip"},
                {"slug": "patrocinios", "text": "Sponsors"},
                {"slug": "c4p", "text": "Call for Proposals"},
                {"slug": "faq", "text": "FAQ"},
            ],
            'CRONOGRAMA':  [
                {"fecha": "February", "desc": "We present the PyConES in Canary Islands!"},
                {"fecha": "April", "desc": "Opening for submissiuon of proposals and tutorials 🗒️"},
                {"fecha": "May", "desc": "Opening for ticket sales 🎟️"},
                {"fecha": "June", "desc": "Opening for grants applications 🧞"},
                {"fecha": "June 23th", "desc": "Closing call for proposals and tutorials ✋"},
                {"fecha": "July 9th", "desc": "Announcement of accepted talks and tutorials 🏆"},
                {"fecha": "October 6th", "desc": "The show starts! 🐍"},
            ]
        },
}

languages_lookup = {
    'es': 'ES',
    'en': 'EN',
    }

def lookup_lang_name(lang_code):
    return languages_lookup[lang_code]

JINJA_FILTERS = {
    'lookup_lang_name': lookup_lang_name,
    }

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Pelican', 'https://getpelican.com/'),
    ('Python.org', 'https://www.python.org/'),
    ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
    ('You can modify those links in your config file', '#'),
)

# Social widget
SOCIAL = (
    ('You can add links in your config file', '#'),
    ('Another social link', '#'),
)

DEFAULT_PAGINATION = 10



TEMPLATE_PAGES = {
    'CNAME': 'CNAME',
    'ediciones_anteriores.html': 'ediciones_anteriores/index.html',
}
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True


TITLE = "PyConES 2023"


# EDICIONES PASADAS
PAST_EDITIONS = [
    {
        "name": "PyConES 2013 - Madrid",
        "logo": "/theme/assets/images/past_editions/2013.png",
        "url": "https://2013.es.pycon.org/",
    },
    {
        "name": "PyConES 2014 - Zaragoza",
        "logo": "/theme/assets/images/past_editions/2014.png",
        "url": "https://2014.es.pycon.org/",
    },
    {
        "name": "PyConES 2015 - Valencia",
        "logo": "/theme/assets/images/past_editions/2015.png",
        "url": "https://2015.es.pycon.org/",
    },
    {
        "name": "PyConES 2016 - Almería",
        "logo": "/theme/assets/images/past_editions/2016.jpg",
        "url": "https://2016.es.pycon.org/",
    },
    {
        "name": "PyConES 2017 - Cáceres",
        "logo": "/theme/assets/images/past_editions/2017.png",
        "url": "https://2017.es.pycon.org/",
    },
    {
        "name": "PyConES 2018 - Málaga",
        "logo": "/theme/assets/images/past_editions/2018.png",
        "url": "https://2018.es.pycon.org/",
    },
    {
        "name": "PyConES 2019 - Alicante",
        "logo": "/theme/assets/images/past_editions/2019.png",
        "url": "https://2019.es.pycon.org/",
    },
    {
        "name": "PyConES 2020 - Pandemic Edition",
        "logo": "/theme/assets/images/past_editions/2020.png",
        "url": "https://2020.es.pycon.org/",
    },
    {
        "name": "PyConES 2021 - Vaccine Edition",
        "logo": "/theme/assets/images/past_editions/2021.png",
        "url": "https://2021.es.pycon.org/",
    },
    {
        "name": "PyConES 2022 - Granada",
        "logo": "/theme/assets/images/past_editions/2022.png",
        "url": "https://2022.es.pycon.org/",
    },
]

# CALL FOR SPONSORS

SPONSORS_DOSSIER_ES = "/theme/assets/files/pycones2023_patrocinios.pdf"
SPONSORS_DOSSIER_EN = "/theme/assets/files/pycones2023_sponsors.pdf"
SPONSORS_DOSSIER_SUM_ES = "/theme/assets/files/pycones2023_patrocinios_breve.pdf"
SPONSORS_DOSSIER_SUM_EN = "/theme/assets/files/pycones2023_sponsors_brief.pdf"


# CALL FOR PAPERS

C4P_LINK = "https://charlas.2023.es.pycon.org"


# PATROCINIOS
PLANES = [
    {
        "key": "teide",
        "titulo": "Teide",
        "altura": "3.7 km",
        "image": "/theme/assets/images/patrocinios/teide_oro.png",
    },
    {
        "key": "tamadaba",
        "titulo": "Tamadaba",
        "altura": "1.4 km",
        "image": "/theme/assets/images/patrocinios/tamadaba_zafiro.png",
    },
    {
        "key": "teneguia",
        "titulo": "Teneguia",
        "altura": "430 m",
        "image": "/theme/assets/images/patrocinios/teneguia_gema.png",
    },
    {
        "key": "timanfaya",
        "titulo": "Timanfaya",
        "altura": "370 m",
        "image": "/theme/assets/images/patrocinios/timanfaya_cobre.png",
    },
]

AGOTADOS = ["tamadaba"]

BENEFICIOS = [
    {
        "titulo": {"es": "Descuento entradas", "en": "Tickets discount"},
        "teide": "20%",
        "tamadaba": "15%",
        "teneguia": "10%",
        "timanfaya": "5%",
    },
    {
        "titulo": {"es": "Logo en la Web", "en": "Logo in the Web"},
        "teide": True,
        "tamadaba": True,
        "teneguia": True,
        "timanfaya": True,
    },
    {
        "titulo": {"es": "Obsequio paquete bienvenida", "en": "Gift inside the welcome pack"},
        "teide": True,
        "tamadaba": True,
        "teneguia": True,
        "timanfaya": True,
    },
    {
        "titulo": {"es": "Acceso Add-ons", "en": "Access to Add-ons"},
        "teide": True,
        "tamadaba": True,
        "teneguia": True,
        "timanfaya": True,
    },
    {
        "titulo": {"es": "Publicaciones en RRSS", "en": "Social Network publications"},
        "teide": True,
        "tamadaba": True,
        "teneguia": True,
        "timanfaya": True,
    },
    {
        "titulo": {"es": "Publicar ofertas de trabajo", "en": "Publish Job Offers"},
        "teide": True,
        "tamadaba": True,
        "teneguia": True,
        "timanfaya": True,
    },
    {
        "titulo": {"es": "Folleto en paquete bienvenida", "en": "Brochure in the welcome pack"},
        "teide": True,
        "tamadaba": True,
        "teneguia": True,
        "timanfaya": False,
    },
    {
        "titulo": {"es": "Logo cartelería", "en": "Logo in posters"},
        "teide": True,
        "tamadaba": True,
        "teneguia": True,
        "timanfaya": False,
    },
    {
        "titulo": {"es": "Anuncio en programa", "en": "Announcement in the program"},
        "teide": True,
        "tamadaba": True,
        "teneguia": True,
        "timanfaya": False,
    },
    {
        "titulo": {"es": "Stand", "en": "Booth"},
        "teide": True,
        "tamadaba": True,
        "teneguia": True,
        "timanfaya": False,
    },
    {
        "titulo": {"es": "Logo newsletter", "en": "Logo in newsletter"},
        "teide": True,
        "tamadaba": True,
        "teneguia": True,
        "timanfaya": False,
    },
    {
        "titulo": {"es": "Logo al proyectar en pausas", "en": "Logo in the break screens"},
        "teide": True,
        "tamadaba": True,
        "teneguia": False,
        "timanfaya": False,
    },
    {
        "titulo": {"es": "Charla Patrocinada", "en": "Sponsored talk"},
        "teide": True,
        "tamadaba": True,
        "teneguia": False,
        "timanfaya": False,
    },
    {
        "titulo": {"es": "Agradecimiento en vivo", "en": "Public thank you live"},
        "teide": True,
        "tamadaba": True,
        "teneguia": False,
        "timanfaya": False,
    },
    {
        "titulo": {"es": "Notas de prensa", "en": "Press releases"},
        "teide": True,
        "tamadaba": True,
        "teneguia": False,
        "timanfaya": False,
    },
    {
        "titulo": {"es": "Miembro jurado", "en": "Jury membership"},
        "teide": True,
        "tamadaba": False,
        "teneguia": False,
        "timanfaya": False,
    },
    {
        "titulo": {"es": "Entrega premio", "en": "Prize delivery"},
        "teide": True,
        "tamadaba": False,
        "teneguia": False,
        "timanfaya": False,
    },
    {
        "titulo": {"es": "PRECIO", "en": "PRICE"},
        "teide": "+6000€",
        "tamadaba": "<span style='text-decoration:line-through;'>4500€</span><br>Agotado",
        "teneguia": "3000€",
        "timanfaya": "1000€",
    },
]


PATROCINIOS_CAT_A = "CAT A"
PATROCINIOS_CAT_B = "CAT B"


PATROCINADORES = {
    PATROCINIOS_CAT_A: [
        {
            "nombre": "PSF",
            "logo": "https://2022.es.pycon.org/theme/images/sponsors/psf.png",
            "enlace": "https://www.python.org/psf/",
        },
        {
            "nombre": "Europython",
            "logo": "https://2022.es.pycon.org/theme/images/sponsors/europython.png",
            "enlace": "https://www.europython-society.org/",
        },
    ],
    PATROCINIOS_CAT_B: [
        {
            "nombre": "PyconEs",
            "logo": "https://2022.es.pycon.org/theme/images/pythonES.svg",
            "enlace": "https://es.python.org/",
        }
    ],
}


# NOTICIAS

NOTICIAS = [
    {
        'es': {
            "titulo": "7 días más para presentar tu propuesta.",
            "fecha": "22/6/2023",
            "contenido": ("Recibimos varias peticiones para dar tiempo extra "
                          "para el llamado de propuesta, con lo que el equipo "
                          "encargado del programa aceptó aumentar el plazo hasta "
                          "el Viernes 30 de Junio. ¡No te quedes sin enviar tu "
                          "idea!"),
        },
        'en': {
            "titulo": "7 more days to submit your proposal.",
            "fecha": "22/6/2023",
            "contenido": ("We got many requests to extend our cfp, so the team "
                          "in charge of the program agreed to move the CfP "
                          "deadline until Friday June 30th. Don't forget to "
                          "submit your proposal!"),
        },
    },
    {
        'es': {
            "titulo": "¡Prepárate para la segunda tanda de entradas!",
            "fecha": "9/6/2023",
            "contenido": ("Después del éxito de las entradas Early bird, y la "
                          "primera tanda, agradecemos mucho su confianza en la "
                          "PyConES23. Tenemos una próxima tanda de entradas "
                          "disponibles el Viernes 7 de Julio. No te olvides de "
                          "seguirnos en nuestras redes sociales para estar al "
                          "tanto.")
        },
        'en': {
            "titulo": "Prepare yourself for the second batch of tickets!",
            "fecha": "9/6/2023",
            "contenido": ("After the success of the Early bird entries, and the "
                          "first batch, we really appreciate your trust in "
                          "PyConES23. We have a next batch of tickets to be "
                          "available on Friday 7th, July. Don't forget to follow us in "
                          "social media to stay up to date"),
        },
    },
    {
        'es': {
            "titulo": "¡Ya puedes comprar tus entradas!",
            "fecha": "5/5/2023",
            "contenido": ("¡Por fin ha llegado el día! Ya están aquí las entradas del evento más "
                          "esperado del año de la comunidad Python en España. "
                          "Luego de las Early Bird, atención a nuestras redes para las siguientes "
                          "tandas de entradas"),
        },
        'en': {
            "titulo": "You can buy your tickets now!",
            "fecha": "5/5/2023",
            "contenido": ("Finally the day has come! The tickets for the most anticipated event "
                          "of the year for the Python community in Spain are here. "
                          "After the Early Bird, keep an eye in our social media for the next "
                          "ticket rounds."),
        },
    },
    {
        'es': {
            "titulo": "Website launch!",
            "fecha": "4/12/2023",
            "contenido": ("We welcome you to PyConES, the most important Python conference in "
                          "Spain. An event that will bring together hundreds of enthusiasts of "
                          "the Python programming language, with an incredible agenda in the best "
                          "possible location. If you want to be part of our sponsors to make this "
                          "conference even more impressive, you can have your own space within "
                          "the event."),
        },
        'en': {
            "titulo": "¡Lanzamiento del sitio web!",
            "fecha": "4/12/2023",
            "contenido": ("Os damos la bienvenida a la PyConES, la conferencia de Python más "
                          "importante de España. Un evento que reunirá a cientos de entusiastas "
                          "del lenguaje de programación Python, con una agenda increíble en la "
                          "mejor localización posible. Si quieres formar parte de nuestros "
                          "patrocinadores para hacer esta conferencia aún mas impresionante "
                          "puedes disponer de espacio propio dentro del evento."),
        },

    },
]

ORG = [
    {
        "name": "Álex Samarín",
        "title": "Technical Lead",
        "img": "/theme/assets/images/org/alex.jpg",
        "community": "Python Canarias",
        "wg": ["Infraestructura", "Voluntariado"],
        "github_username": "",
        "twitter_username": "SamarinAlex",
        "mastodon_url": "",
        "linkedin_url": "",
        "instagram_username": "",
    },
    {
        "name": "Andrés Orcajo",
        "title": "Senior Python Developer",
        "img": "/theme/assets/images/org/andres.jpeg",
        "community": "",
        "wg": ["Infraestructura", "Voluntariado"],
        "github_username": "",
        "twitter_username": "",
        "mastodon_url": "",
        "linkedin_url": "",
        "instagram_username": "",
    },
    {
        "name": "Cristián Maureira-Fredes",
        "title": "Senior R&D Manager",
        "img": "/theme/assets/images/org/cristian.jpg",
        "community": "Python España",
        "wg": ["Programa", "Patrocinios", "Web"],
        "github_username": "cmaureir",
        "twitter_username": "cmaureir",
        "mastodon_url": "https://mastodon.social/@cmaureir",
        "linkedin_url": "https://www.linkedin.com/in/cmaureir/",
        "instagram_username": "",
    },
    {
        "name": "Esther",
        "title": "Software Developer",
        "img": "/theme/assets/images/org/esther.jpg",
        "community": "",
        "wg": ["Voluntariado"],
        "github_username": "EstherJP",
        "twitter_username": "estherxjp",
        "mastodon_url": "",
        "linkedin_url": "https://es.linkedin.com/in/esther-jorge-paramio-275567198",
        "instagram_username": "",
    },
    {
        "name": "Fran Escobar González",
        "title": "Senior Backend developer",
        "img": "/theme/assets/images/org/fran.jpg",
        "community": "Python Canarias",
        "wg": ["Programa", "Patrocinios"],
        "github_username": "",
        "twitter_username": "sheikLoves",
        "mastodon_url": "",
        "linkedin_url": "",
        "instagram_username": "",
    },
    {
        "name": "Javier Alonso Silva",
        "title": "Ingeniero I+D en Teldat",
        "img": "/theme/assets/images/org/javi.jpeg",
        "community": "Python España",
        "wg": ["Diversidad", "Patrocinios", "Web"],
        "github_username": "Javinator9889",
        "twitter_username": "Javinator9889",
        "mastodon_url": "",
        "linkedin_url": "https://linkedin.com/in/javinator9889",
        "instagram_username": "",
    },
    {
        "name": "Jesús Torres Jorge",
        "title": "Profesor y Director Académico",
        "img": "/theme/assets/images/org/jesus.jpg",
        "community": "Python Canarias",
        "wg": ["Diversidad", "Infraestructura", "Patrocinios", "Voluntariado"],
        "github_username": "jesustorresdev",
        "twitter_username": "jesustorresdev",
        "mastodon_url": "",
        "linkedin_url": "https://www.linkedin.com/in/jesusmtorres/",
        "instagram_username": "",
    },
    {
        "name": "Jimena E. Bermúdez",
        "title": "Ingeniera de Software",
        "img": "/theme/assets/images/org/jimena.jpeg",
        "community": "PyLadies",
        "wg": ["Diversidad"],
        "github_username": "JimenaEB",
        "twitter_username": "jimena_y_yo",
        "mastodon_url": "",
        "linkedin_url": "https://www.linkedin.com/in/jimena-eb/",
        "instagram_username": "",
    },
    {
        "name": "Johanna Sanchez",
        "title": "Fullstack Developer y Química",
        "img": "/theme/assets/images/org/johanna.jpg",
        "community": "Python España",
        "wg": ["Diversidad", "Redes sociales", "Patrocinios", "Web"],
        "github_username": "",
        "twitter_username": "EllaQuimica",
        "mastodon_url": "",
        "linkedin_url": "https://www.linkedin.com/in/johanna-sanchez-vallejo/",
        "instagram_username": "",
    },
    {
        "name": "Juan Ignacio Rodríguez de León",
        "title": "Python Developer",
        "img": "/theme/assets/images/org/jileon.jpg",
        "community": "Python Canarias",
        "wg": ["Infraestructura", "Web"],
        "github_username": "euribates",
        "twitter_username": "",
        "mastodon_url": "https://tkz.one/@euribates",
        "linkedin_url": "https://linkedin.com/in/jileon",
        "instagram_username": "",
    },
    {
        "name": "Lucía Cabrera Garabote",
        "title": "Estudiante de Ingeniería Informática",
        "img": "/theme/assets/images/org/lucia.jpg",
        "community": "",
        "wg": ["Patrocinios", "Voluntariado"],
        "github_username": "",
        "twitter_username": "lucdevmind03",
        "mastodon_url": "",
        "linkedin_url": "",
        "instagram_username": "luciasoy_yoo",
    },
    {
        "name": "Nazaret Miranda López",
        "title": "Software Developer",
        "img": "/theme/assets/images/org/nazaret.jpg",
        "community": "AdaLoveDev",
        "wg": ["Voluntariado"],
        "github_username": "",
        "twitter_username": "",
        "mastodon_url": "",
        "linkedin_url": "https://www.linkedin.com/in/zaretmir/",
        "instagram_username": "",
    },
    {
        "name": "Pablo Benavides",
        "title": "Python Lead",
        "img": "/theme/assets/images/org/pablo.jpeg",
        "community": "Python Granada",
        "wg": ["Programa", "Patrocinios"],
        "github_username": "PybloBenavides",
        "twitter_username": "",
        "mastodon_url": "",
        "linkedin_url": "",
        "instagram_username": "",
    },
    {
        "name": "Jose Alberto Torres Aguera",
        "title": "Technical Leader",
        "img": "/theme/assets/images/org/pepe.jpg",
        "community": "Python Málaga",
        "wg": ["Infraestructura", "Patrocinios", "Web"],
        "github_username": "jata84",
        "twitter_username": "Jata1984",
        "mastodon_url": "",
        "linkedin_url": "",
        "instagram_username": "",
    },
    {
        "name": "Samuel López Santamaría",
        "title": "Senior Data Scientist",
        "img": "/theme/assets/images/org/samuel.jpg",
        "community": "",
        "wg": ["Programa", "Infraestructura", "Patrocinios"],
        "github_username": "",
        "twitter_username": "",
        "mastodon_url": "",
        "linkedin_url": "https://www.linkedin.com/in/slopezsantamaria/",
        "instagram_username": "",
    },
    {
        "name": "Sergio Delgado Quintero",
        "title": "Ingeniero Informático y Profesor en FP",
        "img": "/theme/assets/images/org/sergio.jpg",
        "community": "Python Canarias",
        "wg": ["Infraestructura", "Redes Sociales", "Web"],
        "github_username": "sdelquin",
        "twitter_username": "sdelquin",
        "mastodon_url": "",
        "linkedin_url": "https://www.linkedin.com/in/sdelquin",
        "instagram_username": "",
    },
    {
        "name": "Silvia García Hernández",
        "title": "Estudiante",
        "img": "/theme/assets/images/org/silvia.jpg",
        "community": "Python Canarias",
        "wg": ["Diversidad", "Redes Sociales", "Voluntariado"],
        "github_username": "",
        "twitter_username": "",
        "mastodon_url": "",
        "linkedin_url": "",
        "instagram_username": "",
    },
    {
        "name": " Victor Vicente-Palacios",
        "title": "Clinical Data Scientist",
        "img": "/theme/assets/images/org/victor.jpg",
        "community": "",
        "wg": ["Programa", "Diversidad"],
        "github_username": "victorvicpal",
        "twitter_username": "victorvicpal",
        "mastodon_url": "https://dair-community.social/@victorvicpal",
        "linkedin_url": "https://www.linkedin.com/in/victorvicpal/",
        "instagram_username": "",
    },
    {
        "name": "Yodra López Herrera",
        "title": "Software Developer",
        "img": "/theme/assets/images/org/yodra.jpg",
        "community": "AdaLoveDev",
        "wg": ["Programa", "Diversidad", "Infraestructura", "Patrocinios", "Voluntariado"],
        "github_username": "",
        "twitter_username": "yodralopez",
        "mastodon_url": "",
        "linkedin_url": "https://www.linkedin.com/in/yodralopez",
        "instagram_username": "",
    },
]

# Shuffle team per deployment
random.shuffle(ORG)


CRONOGRAMA = [
    {"fecha": "Febrero", "desc": "¡Presentamos la PyConES en Canarias!"},
    # TODO: Agregar la fecha cuando se lance el sitio
    {"fecha": "Abril", "desc": "Apertura para el envío de ponencias y talleres 🗒️"},
    {"fecha": "Mayo", "desc": "Apertura para la venta de entradas 🎟️"},
    {"fecha": "Junio", "desc": "Apertura para la postulación de becas 🧞"},
    {"fecha": "23 de Junio", "desc": "Cierre del llamado a ponencias y talleres ✋"},
    {"fecha": "9 de Julio", "desc": "Anuncio de ponencias y talleres aceptados 🏆"},
    {"fecha": "6 de Octubre", "desc": "¡Empieza el espectáculo! 🐍"},
]

SPONSORS = {
    "teide": {
    },
    "tamadaba": {
        "Skydance Studios": {
            "logo": "/theme/assets/images/sponsors/logo_skydance.png",
            "url": "https://skydance.com/",
        },
        "Octopus Energy": {
            "logo": "/theme/assets/images/sponsors/logo_octopusenergy.png",
            "url": "https://octopus.energy/",
        },
    },
    "teneguia": {
    },
    "timanfaya": {
        "GISCE-TI, S.L.": {
            "logo": "/theme/assets/images/sponsors/logo_gisce.png",
            "url": "https://gisce.net",
        },
        "Kaleidos": {
            "logo": "/theme/assets/images/sponsors/logo_kaleidos.png",
            "url": "https://kaleidos.net",
        },
    },
}

KEYNOTERS=[
    {
        "name":"Gema Parreño",
        "description":{
            "es":"Gema Parreño es Data Scientist en IZERTIS con pasión y compromiso con el Open Source y el Machine Learning. Ha contribuido en proyectos para OpenNASA, PySC2, API desarrollada por DeepMind y Blizzard para StarCraft II y DVC, entre otros. Le gusta viajar, bucear y un buen reporte de errores.",
            "en":"Gema Parreño is a Data Scientist at IZERTIS with passion and commitment to Open Source and Machine Learning. She has contributed to projects for OpenNASA, PySC2, API developed by DeepMind and Blizzard for StarCraft II and DVC, among others. She likes traveling, snorkeling, and good bug reporting."
        },
        "image":"/theme/assets/images/ponentes/gema.jpg",
        "twitter":"https://twitter.com/SoyGema"
    },

]
