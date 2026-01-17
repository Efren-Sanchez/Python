"""
Comprobador de estado de páginas web
Diseña un programa que lea desde un fichero de texto una lista de URLs (una por línea).
Para cada URL:
- Realiza una petición GET con requests.
- Muestra el código de estado (200, 404, etc.).
- Guarda en un fichero de salida las URLs que no respondan o devuelvan un código de error (400 o superior).
"""

# Programa 33: Comprobador de estado de páginas web

import requests  # Para peticiones HTTP


def cargar_urls(ruta_fichero):
    """
    Lee una lista de URLs desde un fichero de texto.
    """
    urls = []
    try:
        with open(ruta_fichero, "r", encoding="utf-8") as f:
            for linea in f:
                url = linea.strip()
                if url.startswith("http") and url not in urls:
                    urls.append(url)
    except FileNotFoundError:
        print(f"El fichero '{ruta_fichero}' no existe.")
    except OSError as e:
        print(f"Error al leer el fichero: {e}")
    return urls


def comprobar_estado(url):
    """
    Comprueba el estado HTTP de una URL y devuelve el código.
    """
    try:
        respuesta = requests.head(url, timeout=5, allow_redirects=True)
        return respuesta.status_code
    except requests.exceptions.RequestException:
        return None


def main():
    """
    Función principal del programa.
    """
    ruta_urls = input("Introduce el nombre del fichero con las URLs (una por línea): ")
    urls = cargar_urls(ruta_urls)

    if not urls:
        print("No se han leído URLs del fichero.")
        return

    print("\nComprobando estado de las páginas...")
    urls_fallidas = []

    for url in urls:
        codigo = comprobar_estado(url)
        estado = "OK" if codigo == 200 else f"ERROR ({codigo})" if codigo else "NO ACCESIBLE"
        print(f"{url}: {estado}")
        
        if codigo is None or codigo >= 400:
            urls_fallidas.append(url)

    # Guardar URLs fallidas en fichero de salida
    if urls_fallidas:
        try:
            with open("urls_fallidas.txt", "w", encoding="utf-8") as f:
                for url in urls_fallidas:
                    f.write(url + "\n")
            print(f"\nSe han guardado {len(urls_fallidas)} URLs fallidas en 'urls_fallidas.txt'.")
        except OSError as e:
            print(f"Error al escribir fichero de fallidas: {e}")
    else:
        print("\n¡Todas las URLs responden correctamente!")


if __name__ == "__main__":
    main()
