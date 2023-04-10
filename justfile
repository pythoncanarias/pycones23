dev target="web": clean
    PYCONES_BUILD_TARGET={{target}} pelican -lrv

docker target="web":
    PYCONES_BUILD_TARGET={{target}} docker compose up

build target="web" siteurl="http://localhost:8000": clean
    PYCONES_BUILD_TARGET={{target}} SITEURL={{siteurl}} pelican content -s publishconf.py

clean:
    rm -fr output/*
