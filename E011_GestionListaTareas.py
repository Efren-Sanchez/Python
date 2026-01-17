"""
Gestión de una lista de tareas
Crea un programa que mantenga una lista de tareas pendientes en memoria.
Debe permitir: añadir tarea, marcar tarea como realizada, eliminar tarea y mostrar todas las tareas (pendientes y realizadas). Usa una lista de tuplas (descripcion, realizada) y un menú simple.
"""

# Programa 11: Gestión de una lista de tareas

def mostrar_menu():
    """
    Muestra el menú principal y devuelve la opción elegida.
    """
    print("\n===== GESTIÓN DE TAREAS =====")
    print("1. Añadir tarea")
    print("2. Marcar tarea como realizada")
    print("3. Eliminar tarea")
    print("4. Mostrar todas las tareas")
    print("5. Salir")
    opcion = input("Elige una opción (1-5): ")
    return opcion


def mostrar_tareas(lista_tareas):
    """
    Muestra todas las tareas de la lista con su estado.
    Cada tarea es una tupla: (descripcion, realizada)
    """
    if not lista_tareas:
        print("No hay tareas en la lista.")
        return

    print("\n--- LISTA DE TAREAS ---")
    for indice, tarea in enumerate(lista_tareas, start=1):
        descripcion, realizada = tarea
        estado = "✔" if realizada else "✘"
        print(f"{indice}. [{estado}] {descripcion}")


def anadir_tarea(lista_tareas):
    """
    Pide una descripción al usuario y añade una nueva tarea
    como no realizada.
    """
    descripcion = input("Introduce la descripción de la nueva tarea: ").strip()
    if descripcion == "":
        print("La descripción no puede estar vacía.")
        return
    nueva_tarea = (descripcion, False)
    lista_tareas.append(nueva_tarea)
    print("Tarea añadida correctamente.")


def marcar_tarea_realizada(lista_tareas):
    """
    Pide al usuario el número de tarea y la marca como realizada.
    """
    mostrar_tareas(lista_tareas)
    if not lista_tareas:
        return

    try:
        numero = int(input("Introduce el número de tarea a marcar como realizada: "))
        if numero < 1 or numero > len(lista_tareas):
            print("Número de tarea no válido.")
            return
    except ValueError:
        print("Debes introducir un número entero.")
        return

    descripcion, _ = lista_tareas[numero - 1]
    lista_tareas[numero - 1] = (descripcion, True)
    print("Tarea marcada como realizada.")


def eliminar_tarea(lista_tareas):
    """
    Pide al usuario el número de tarea y la elimina de la lista.
    """
    mostrar_tareas(lista_tareas)
    if not lista_tareas:
        return

    try:
        numero = int(input("Introduce el número de tarea a eliminar: "))
        if numero < 1 or numero > len(lista_tareas):
            print("Número de tarea no válido.")
            return
    except ValueError:
        print("Debes introducir un número entero.")
        return

    tarea_eliminada = lista_tareas.pop(numero - 1)
    print(f"Tarea '{tarea_eliminada[0]}' eliminada correctamente.")


def main():
    """
    Función principal del programa.
    """
    lista_tareas = []

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            anadir_tarea(lista_tareas)
        elif opcion == "2":
            marcar_tarea_realizada(lista_tareas)
        elif opcion == "3":
            eliminar_tarea(lista_tareas)
        elif opcion == "4":
            mostrar_tareas(lista_tareas)
        elif opcion == "5":
            print("Saliendo del gestor de tareas...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    main()
