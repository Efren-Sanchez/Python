"""
Buscador de líneas en un log
Dado un fichero de log (por ejemplo, aplicacion.log), pide al usuario una palabra clave.
El programa debe mostrar todas las líneas que contengan esa palabra, indicando también el número de línea. Usa lectura línea a línea y enumeración.
"""

# Programa 18: Buscador de líneas en un fichero de log

def buscar_en_log(ruta, palabra_clave):
    """
    Busca líneas que contengan la palabra clave en un fichero de texto.
    Muestra el número de línea y el contenido correspondiente.
    """
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            print(f"\nLíneas que contienen '{palabra_clave}':")
            encontrada_alguna = False
            for numero_linea, linea in enumerate(f, start=1):
                if palabra_clave in linea:
                    encontrada_alguna = True
                    print(f"{numero_linea}: {linea.rstrip()}")
            if not encontrada_alguna:
                print("No se han encontrado coincidencias.")
    except FileNotFoundError:
        print("El fichero de log no existe.")
    except OSError as e:
        print("Error al leer el fichero de log:", e)


def main():
    """
    Función principal del programa.
    """
    ruta = input("Introduce el nombre del fichero de log: ")
    palabra = input("Introduce la palabra clave a buscar: ")

    if palabra == "":
        print("La palabra clave no puede estar vacía.")
        return

    buscar_en_log(ruta, palabra)


if __name__ == "__main__":
    main()
