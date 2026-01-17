"""
Gestión de alumnos con tuplas inmutables
Crea una lista de tuplas inmutables que representen alumnos: (dni, nombre, apellidos, nota_media).
Implementa un menú que permita:
- Mostrar todos los alumnos ordenados por nota media.
- Buscar un alumno por DNI.
- Mostrar la nota media del grupo.
"""

# Programa 19: Gestión de alumnos con tuplas inmutables

def mostrar_menu():
    """
    Muestra el menú principal y devuelve la opción elegida.
    """
    print("\n===== GESTIÓN DE ALUMNOS =====")
    print("1. Mostrar alumnos ordenados por nota media")
    print("2. Buscar alumno por DNI")
    print("3. Mostrar nota media del grupo")
    print("4. Salir")
    opcion = input("Elige una opción (1-4): ")
    return opcion


def mostrar_alumnos_ordenados(alumnos):
    """
    Muestra todos los alumnos ordenados por nota media descendente.
    Cada alumno es una tupla (dni, nombre, apellidos, nota_media).
    """
    if not alumnos:
        print("No hay alumnos.")
        return

    alumnos_ordenados = sorted(alumnos, key=lambda a: a[3], reverse=True)
    print("\n--- ALUMNOS ORDENADOS POR NOTA MEDIA ---")
    for dni, nombre, apellidos, nota in alumnos_ordenados:
        print(f"{dni} - {nombre} {apellidos} - {nota:.2f}")


def buscar_alumno_por_dni(alumnos, dni_buscado):
    """
    Busca y muestra un alumno por su DNI.
    """
    for alumno in alumnos:
        dni, nombre, apellidos, nota = alumno
        if dni == dni_buscado:
            print(f"Alumno encontrado: {dni} - {nombre} {apellidos} - {nota:.2f}")
            return
    print("No se ha encontrado ningún alumno con ese DNI.")


def mostrar_nota_media_grupo(alumnos):
    """
    Calcula y muestra la nota media del grupo.
    """
    if not alumnos:
        print("No hay alumnos.")
        return
    suma = 0.0
    for alumno in alumnos:
        suma += alumno[3]
    media = suma / len(alumnos)
    print(f"Nota media del grupo: {media:.2f}")


def main():
    """
    Función principal del programa.
    """
    # Lista inicial de alumnos de ejemplo (se podría leer de fichero)
    alumnos = [
        ("11111111A", "Ana", "García López", 7.5),
        ("22222222B", "Luis", "Martínez Pérez", 8.3),
        ("33333333C", "María", "Rodríguez Sánchez", 6.9),
        ("44444444D", "Juan", "López Díaz", 9.1),
    ]

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            mostrar_alumnos_ordenados(alumnos)
        elif opcion == "2":
            dni = input("Introduce el DNI del alumno: ").strip()
            buscar_alumno_por_dni(alumnos, dni)
        elif opcion == "3":
            mostrar_nota_media_grupo(alumnos)
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    main()
