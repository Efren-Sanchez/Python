"""
Diccionario de frecuencias de caracteres
Lee un fichero de texto y muestra la frecuencia de cada letra (ignorando mayúsculas, tildes y signos de puntuación). Usa un diccionario y ordena por frecuencia descendente.
"""

# Programa 5: Frecuencia de letras en un fichero de texto

import unicodedata  # Para normalizar tildes


def normalizar_texto(texto):
    """
    Recibe un texto y devuelve una versión:
    - En minúsculas
    - Sin tildes
    - Sin signos de puntuación
    Solo se conservan letras y espacios.
    """
    # Pasar a minúsculas
    texto = texto.lower()

    # Eliminar tildes usando normalización Unicode
    texto = unicodedata.normalize("NFD", texto)
    texto_sin_tildes = "".join(
        c for c in texto
        if unicodedata.category(c) != "Mn"
    )

    # Eliminar signos de puntuación, quedando solo letras y espacios
    resultado = []
    for c in texto_sin_tildes:
        if c.isalpha() or c.isspace():
            resultado.append(c)
    return "".join(resultado)


def contar_letras(texto):
    """
    Cuenta la frecuencia de cada letra en el texto
    y devuelve un diccionario {letra: frecuencia}.
    """
    frecuencias = {}
    for c in texto:
        if c.isalpha():
            frecuencias[c] = frecuencias.get(c, 0) + 1
    return frecuencias


def leer_fichero(ruta):
    """
    Lee el contenido de un fichero de texto y lo devuelve como cadena.
    """
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print("Error: el fichero no existe.")
    except OSError as e:
        print("Error al leer el fichero:", e)
    return None


def main():
    """
    Función principal del programa.
    """
    ruta = input("Introduce el nombre del fichero: ")
    contenido = leer_fichero(ruta)
    if contenido is None:
        return

    texto_normalizado = normalizar_texto(contenido)
    frecuencias = contar_letras(texto_normalizado)

    # Ordenamos por frecuencia descendente
    letras_ordenadas = sorted(
        frecuencias.items(),
        key=lambda par: par[1],
        reverse=True
    )

    print("Frecuencia de letras (de mayor a menor):")
    for letra, freq in letras_ordenadas:
        print(f"'{letra}': {freq}")


if __name__ == "__main__":
    main()
