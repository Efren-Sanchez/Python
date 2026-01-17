"""
Estadísticas de palabras con stopwords
Pide al usuario el nombre de un fichero de texto.
Cuenta las palabras más usadas, pero ignorando un conjunto de palabras vacías (por ejemplo: "y", "de", "la", "el", "en", "a"). Muestra las 10 palabras más frecuentes y su frecuencia. Usa un conjunto (set) para las stopwords.
"""

# Programa 14: Estadísticas de palabras ignorando stopwords

from collections import Counter  # Para contar palabras


STOPWORDS = {
    "y", "de", "la", "el", "en", "a", "los", "las", "un", "una", "que",
    "por", "con", "se", "su", "es", "al"
}


def leer_fichero(ruta):
    """
    Lee el contenido de un fichero de texto y lo devuelve como cadena.
    """
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print("El fichero no existe.")
    except OSError as e:
        print("Error al leer el fichero:", e)
    return ""


def limpiar_y_separar_palabras(texto):
    """
    Convierte el texto en minúsculas, elimina signos de puntuación básicos
    y lo separa en palabras.
    """
    texto = texto.lower()
    caracteres_a_reemplazar = ",.;:¡!¿?()[]\"'"
    for c in caracteres_a_reemplazar:
        texto = texto.replace(c, " ")
    palabras = texto.split()
    return palabras


def contar_palabras_sin_stopwords(palabras):
    """
    Cuenta las palabras ignorando las stopwords.
    Devuelve un Counter con la frecuencia de cada palabra.
    """
    palabras_validas = [p for p in palabras if p not in STOPWORDS]
    contador = Counter(palabras_validas)
    return contador


def main():
    """
    Función principal del programa.
    """
    ruta = input("Introduce el nombre del fichero de texto: ")
    texto = leer_fichero(ruta)
    if texto == "":
        print("No se ha leído contenido del fichero.")
        return

    palabras = limpiar_y_separar_palabras(texto)
    contador = contar_palabras_sin_stopwords(palabras)

    top_10 = contador.most_common(10)

    print("\nLas 10 palabras más frecuentes (sin stopwords) son:")
    for palabra, frecuencia in top_10:
        print(f"'{palabra}': {frecuencia} veces")


if __name__ == "__main__":
    main()
