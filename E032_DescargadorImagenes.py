"""
Descargador simple de imágenes
Escribe un programa que reciba por teclado una URL de imagen y un nombre de fichero local.
El programa debe:
- Descargar la imagen usando requests.
- Guardarla en disco en un fichero con el nombre indicado.
- Comprobar el tamaño de la respuesta y mostrarlo por pantalla.
"""

# Programa 32: Descargador de imágenes

import requests  # Para peticiones HTTP


def descargar_imagen(url, nombre_fichero):
    """
    Descarga una imagen desde una URL y la guarda localmente.
    """
    try:
        respuesta = requests.get(url, timeout=10, stream=True)
        respuesta.raise_for_status()

        tamano_respuesta = len(respuesta.content)
        print(f"Tamaño de la imagen descargada: {tamano_respuesta} bytes")

        with open(nombre_fichero, "wb") as f:
            f.write(respuesta.content)
        print(f"Imagen guardada como '{nombre_fichero}'.")
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error al descargar la imagen: {e}")
        return False
    except OSError as e:
        print(f"Error al guardar el fichero: {e}")
        return False


def main():
    """
    Función principal del programa.
    """
    url = input("Introduce la URL de la imagen: ").strip()
    if url == "":
        print("La URL no puede estar vacía.")
        return

    nombre_fichero = input("Introduce el nombre del fichero de destino (incluyendo extensión): ").strip()
    if nombre_fichero == "":
        nombre_fichero = "imagen_descargada.jpg"

    print("Descargando imagen...")
    if descargar_imagen(url, nombre_fichero):
        print("¡Descarga completada con éxito!")
    else:
        print("La descarga ha fallado.")


if __name__ == "__main__":
    main()
