"""
Lectura de datos CSV en clase Alumno
Crea una clase Alumno con atributos nombre, edad y ciudad.
Escribe un programa que lea un fichero CSV con esos campos y cree una lista de objetos Alumno.
Después, implementa funciones para:
- Mostrar todos los alumnos.
- Mostrar solo los que viven en una ciudad dada.
- Calcular la edad media del grupo.
"""

# Programa 25: Clase Alumno y lectura desde CSV

import csv  # Para leer ficheros CSV


class Alumno:
    """
    Clase que representa un alumno con nombre, edad y ciudad.
    """

    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

    def __str__(self):
        return f"{self.nombre} ({self.edad} años) - {self.ciudad}"


def cargar_alumnos_desde_csv(ruta):
    """
    Carga alumnos desde un fichero CSV con formato:
    nombre,edad,ciudad
    Devuelve una lista de objetos Alumno.
    """
    alumnos = []
    try:
        with open(ruta, "r", encoding="utf-8", newline="") as f:
            lector = csv.reader(f)
            cabecera = next(lector, None)  # Ignoramos la cabecera si existe
            for fila in lector:
                if len(fila) < 3:
                    continue
                nombre = fila[0].strip()
                try:
                    edad = int(fila[1])
                except ValueError:
                    continue
                ciudad = fila[2].strip()
                alumnos.append(Alumno(nombre, edad, ciudad))
    except FileNotFoundError:
        print("El fichero CSV no existe.")
    except OSError as e:
        print("Error al leer el fichero CSV:", e)
    return alumnos


def mostrar_todos(alumnos):
    """
    Muestra todos los alumnos.
    """
    if not alumnos:
        print("No hay alumnos cargados.")
        return
    print("\n--- LISTA DE ALUMNOS ---")
    for alumno in alumnos:
        print(alumno)


def mostrar_por_ciudad(alumnos, ciudad_buscada):
    """
    Muestra los alumnos que viven en una ciudad dada.
    """
    ciudad_buscada = ciudad_buscada.lower()
    encontrados = [a for a in alumnos if a.ciudad.lower() == ciudad_buscada]

    if not encontrados:
        print(f"No hay alumnos de la ciudad '{ciudad_buscada}'.")
        return

    print(f"\nAlumnos de la ciudad '{ciudad_buscada}':")
    for a in encontrados:
        print(a)


def mostrar_edad_media(alumnos):
    """
    Calcula y muestra la edad media del grupo.
    """
    if not alumnos:
        print("No hay alumnos cargados.")
        return
    suma = sum(a.edad for a in alumnos)
    media = suma / len(alumnos)
    print(f"Edad media del grupo: {media:.2f} años")


def main():
    """
    Función principal del programa.
    """
    ruta = input("Introduce el nombre del fichero CSV de alumnos: ")
    alumnos = cargar_alumnos_desde_csv(ruta)

    if not alumnos:
        print("No se han cargado alumnos.")
        return

    mostrar_todos(alumnos)

    ciudad = input("\nIntroduce una ciudad para filtrar alumnos: ")
    mostrar_por_ciudad(alumnos, ciudad)

    mostrar_edad_media(alumnos)


if __name__ == "__main__":
    main()
