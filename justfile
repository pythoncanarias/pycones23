dev: clean
    pelican -lrv

build: clean
    pelican content -s publishconf.py

clean:
    rm -fr output/*
