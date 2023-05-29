dev: clean
   pelican -lrv

docker:
    docker compose up

build siteurl="http://localhost:8000": clean
    SITEURL={{siteurl}} pelican content -s publishconf.py

clean:
    rm -fr output/*
