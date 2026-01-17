"""
Lector de RSS con feedparser (u otra librería similar)
Crea un programa que lea un feed RSS (por ejemplo, de noticias tecnológicas) usando una librería especializada como feedparser (si está instalada; si no, plantearlo como opcional).
El programa debe:
- Obtener la lista de entradas del feed.
- Mostrar por pantalla los títulos y URLs de las 5 últimas noticias.
- Guardar los títulos en un fichero de texto para leerlos más tarde sin conexión.
"""

# Programa 40: Lector de RSS con feedparser
# Para ejecutar: pip install feedparser
# Luego: python programa10.py

try:
    import feedparser  # Librería especializada en RSS/Atom
except ImportError:
    print("Instala feedparser: pip install feedparser")
    exit(1)

import os


def leer_rss(url_feed):
    """
    Lee un feed RSS y devuelve las últimas 5 entradas.
    """
    try:
        feed = feedparser.parse(url_feed)
        if feed.bozo:  # Error al parsear
            return None
        
        ultimas_entradas = []
        for entrada in feed.entries[:5]:
            titulo = entrada.title
            enlace = entrada.link
            ultimas_entradas.append((titulo, enlace))
        return ultimas_entradas
    except Exception as e:
        print(f"Error al leer el feed: {e}")
        return None


def guardar_titulos(entradas, ruta_fichero):
    """
    Guarda los títulos de las noticias en un fichero de texto.
    """
    try:
        with open(ruta_fichero, "w", encoding="utf-8") as f:
            f.write("=== ULTIMAS NOTICIAS ===\n\n")
            for i, (titulo, enlace) in enumerate(entradas, 1):
                f.write(f"{i}. {titulo}\n")
                f.write(f"   {enlace}\n\n")
        print(f"Titulos guardados en '{ruta_fichero}'.")
    except OSError as e:
        print(f"Error al guardar fichero: {e}")


def main():
    """
    Funcion principal del programa.
    """
    # Feed RSS de ejemplo (BBC Mundo) - usando HTTPS
    url_feed = "https://feeds.bbci.co.uk/mundo/rss.xml"
    
    print("Leyendo feed RSS...")
    entradas = leer_rss(url_feed)
    
    if entradas is None:
        print("No se pudo leer el feed RSS.")
        return
    
    print("\n=== 5 ULTIMAS NOTICIAS ===")
    for i, (titulo, enlace) in enumerate(entradas, 1):
        print(f"{i}. {titulo}")
        print(f"   {enlace}\n")
    
    # Guardar en fichero
    guardar_titulos(entradas, "ultimas_noticias.txt")


if __name__ == "__main__":
    main()
