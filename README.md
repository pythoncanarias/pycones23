# pycones23

Conferencia Nacional de Python 2023 · La Laguna · Tenerife · Islas Canarias

## Como empezar

### Utilizando Docker

#### Dev containers

- Se ha configurado el devcontainers para usar en vscode y en github, para usarlo sólo deberíamos abrir el proyecto dentro del contenedor

#### Docker-compose

- Para trabajar con docker-compose deberemos tener instalado docker y docker-compose, https://docs.docker.com/compose/install/
- Ejecutar el siguiente comando dentro de la carpeta del proyecto `bash docker-compose up` para ver la web consulta http://localhost:8000
- Nota: El puerto que usa el contenedor es el 8000, para trabajar con el proyecto, asegurate que no tienes ningún contenedor con ese puerto en uso.

### Utilizando Python

Crea un nuevo entorno virtual (opcional) e instala las dependencias:

```bash
python -m venv env
source env/bin/activate   # macOS y Linux
env\Scripts\activate      # windows cmd
env\Scripts\Activate.ps1  # windows Powershell

pip install -r requirements.txt
```

Genera el contenido, y comienza el servidor en localhost

```bash
PYCONES_BUILD_TARGET=WEB pelican -l content -s pelicanconf.py -r --bind 0.0.0.0
```

visita `http://0.0.0.0:8000` para visualizar el sitio web.


#### v1.0 12/04/2023
