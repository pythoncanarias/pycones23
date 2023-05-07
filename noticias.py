import glob
from datetime import date as Date
from dataclasses import dataclass

import markdown


@dataclass
class Noticia:
    titulo: str
    fecha: Date
    contenido: str


def _iter_noticias():
    news_parser = markdown.Markdown(extensions=['extra', 'meta'])
    for filename in glob.glob('noticias/*.md'):
        news_parser.reset()
        with open(filename, 'r', encoding='utf-8') as f:
            contenido = news_parser.convert(f.read())
            yield Noticia(
                titulo=news_parser.Meta['titulo'][0],
                fecha=Date.fromisoformat(news_parser.Meta['fecha'][0]),
                contenido=contenido,
                )


def ultimas_noticias(max_noticias=5):
    news = sorted(_iter_noticias(), reverse=True, key=lambda d: d.fecha)
    return news[0:max_noticias]


def main():
    for noticia in ultimas_noticias():
        print(noticia.fecha, noticia.titulo)


if __name__ == "__main__":
    main()
