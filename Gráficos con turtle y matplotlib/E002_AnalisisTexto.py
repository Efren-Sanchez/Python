"""
Análisis de texto
Solicita al usuario el nombre de un fichero de texto y muestra:
- Número total de líneas.
- Número total de palabras.
- Las 5 palabras más frecuentes.
Usa el módulo collections (por ejemplo, Counter).
"""

# Programa 2: Análisis de texto en un fichero

from collections import Counter  # Para contar palabras


def leer_fichero(ruta):
    """
    Intenta leer el contenido de un fichero de texto y lo devuelve como cadena.
    Si hay un error (por ejemplo, el fichero no existe), devuelve None.
    """
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            contenido = f.read()
        return contenido
    except FileNotFoundError:
        print("Error: el fichero no existe.")
    except OSError as e:
        print("Error al leer el fichero:", e)
    return None


def analizar_texto(texto):
    """
    Recibe una cadena de texto y devuelve:
    - número de líneas
    - número de palabras
    - lista de tuplas con las 5 palabras más frecuentes
    """
    lineas = texto.splitlines()
    num_lineas = len(lineas)

    # Separa por espacios simples; para algo más robusto se podría usar regex
    palabras = texto.split()
    num_palabras = len(palabras)

    contador = Counter(palabras)
    top_5 = contador.most_common(5)

    return num_lineas, num_palabras, top_5


def main():
    """
    Función principal del programa.
    """
    ruta = input("Introduce el nombre del fichero de texto: ")
    contenido = leer_fichero(ruta)

    if contenido is None:
        return

    num_lineas, num_palabras, top_5 = analizar_texto(contenido)

    print(f"Número de líneas: {num_lineas}")
    print(f"Número de palabras: {num_palabras}")
    print("Las 5 palabras más frecuentes son:")
    for palabra, frecuencia in top_5:
        print(f"  '{palabra}': {frecuencia} veces")


if __name__ == "__main__":
    main()
