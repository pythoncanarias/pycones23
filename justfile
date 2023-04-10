dev target="web": clean
    PYCONES_BUILD_TARGET={{target}} pelican -lrv

build target="web": clean
    PYCONES_BUILD_TARGET={{target}} pelican content -s publishconf.py

docker target="web":
    PYCONES_BUILD_TARGET={{target}} docker compose up

clean:
    rm -fr output/*
