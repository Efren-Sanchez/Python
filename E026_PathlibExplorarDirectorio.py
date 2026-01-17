"""
Uso de pathlib para explorar un directorio
Escribe un programa que use la librería pathlib para:
- Pedir al usuario una ruta de directorio.
- Listar todos los ficheros normales de ese directorio.
- Mostrar, para cada fichero, su tamaño en bytes y su extensión.
- Contar cuántos ficheros hay de cada extensión (por ejemplo: .txt, .py, etc.).
"""

# Programa 26: Explorar un directorio con pathlib

from pathlib import Path  # Módulo moderno para rutas de sistema de ficheros


def explorar_directorio(ruta_directorio):
    """
    Lista todos los ficheros normales de un directorio,
    mostrando su tamaño y extensión. Cuenta cuántos hay de cada extensión.
    """
    path = Path(ruta_directorio)

    if not path.exists() or not path.is_dir():
        print("La ruta indicada no es un directorio válido.")
        return

    conteo_extensiones = {}

    print("\n--- FICHEROS EN EL DIRECTORIO ---")
    for elemento in path.iterdir():
        if elemento.is_file():
            tamano = elemento.stat().st_size  # Tamaño en bytes
            extension = elemento.suffix.lower()  # Incluye el punto, por ejemplo ".txt"
            if extension == "":
                extension = "(sin extensión)"
            print(f"{elemento.name} - {tamano} bytes - {extension}")

            conteo_extensiones[extension] = conteo_extensiones.get(extension, 0) + 1

    print("\n--- RESUMEN POR EXTENSIÓN ---")
    if not conteo_extensiones:
        print("No se han encontrado ficheros en el directorio.")
    else:
        for ext, cantidad in conteo_extensiones.items():
            print(f"{ext}: {cantidad} fichero(s)")


def main():
    """
    Función principal del programa.
    """
    ruta = input("Introduce la ruta del directorio a explorar: ")
    explorar_directorio(ruta)


if __name__ == "__main__":
    main()
