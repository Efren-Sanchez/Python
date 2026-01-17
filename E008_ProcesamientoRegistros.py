"""
Procesamiento de registros
Dado un fichero CSV con columnas nombre,edad,ciudad, crea un programa que:
- Lea el fichero y almacene los datos en una lista de tuplas.
- Pida una ciudad y muestre los nombres de las personas que viven en ella.
Usa el módulo csv.
"""

# Programa 8: Leer un CSV y filtrar por ciudad

import csv  # Módulo para trabajar con ficheros CSV


def leer_csv(ruta):
    """
    Lee un fichero CSV con columnas: nombre, edad, ciudad.
    Devuelve una lista de tuplas (nombre, edad, ciudad).
    """
    registros = []
    try:
        with open(ruta, "r", encoding="utf-8", newline="") as f:
            lector = csv.reader(f)
            # Suponemos primera fila como cabecera
            cabecera = next(lector, None)

            for fila in lector:
                if len(fila) < 3:
                    continue
                nombre = fila[0]
                try:
                    edad = int(fila[1])
                except ValueError:
                    edad = None
                ciudad = fila[2]
                registros.append((nombre, edad, ciudad))
    except FileNotFoundError:
        print("Error: el fichero CSV no existe.")
    except OSError as e:
        print("Error al leer el fichero CSV:", e)

    return registros


def mostrar_personas_por_ciudad(registros, ciudad_buscada):
    """
    Muestra los nombres de las personas que viven en una ciudad concreta.
    """
    ciudad_buscada = ciudad_buscada.lower()
    encontrados = []

    for nombre, edad, ciudad in registros:
        if ciudad.lower() == ciudad_buscada:
            encontrados.append((nombre, edad))

    if encontrados:
        print(f"Personas que viven en {ciudad_buscada}:")
        for nombre, edad in encontrados:
            if edad is not None:
                print(f"- {nombre} (edad: {edad})")
            else:
                print(f"- {nombre} (edad no disponible)")
    else:
        print(f"No se han encontrado personas que vivan en {ciudad_buscada}.")


def main():
    """
    Función principal del programa.
    """
    ruta = input("Introduce el nombre del fichero CSV: ")
    registros = leer_csv(ruta)

    if not registros:
        print("No se han leído registros.")
        return

    ciudad = input("Introduce la ciudad a buscar: ")
    mostrar_personas_por_ciudad(registros, ciudad)


if __name__ == "__main__":
    main()
