"""
Clase GestorNotas con persistencia en JSON
Crea una clase GestorNotas que gestione un diccionario de alumnos y sus notas.
La clase debe:
- Cargar las notas desde un fichero JSON al iniciar (si existe).
- Permitir añadir o modificar la nota de un alumno.
- Permitir eliminar un alumno.
- Guardar los cambios en el fichero JSON al finalizar el programa.
Implementa un menú de texto para manejar el gestor.
"""

# Programa 28: Clase GestorNotas con fichero JSON

import json
import os


class GestorNotas:
    """
    Clase que gestiona un diccionario de alumnos y sus notas,
    con persistencia en un fichero JSON.
    """

    def __init__(self, ruta_fichero):
        self.ruta_fichero = ruta_fichero
        self.notas = {}
        self.cargar()

    def cargar(self):
        """
        Carga las notas desde el fichero JSON si existe.
        """
        if not os.path.exists(self.ruta_fichero):
            self.notas = {}
            return
        try:
            with open(self.ruta_fichero, "r", encoding="utf-8") as f:
                self.notas = json.load(f)
        except (json.JSONDecodeError, OSError):
            print("Error al cargar el fichero de notas. Se inicia vacío.")
            self.notas = {}

    def guardar(self):
        """
        Guarda las notas en el fichero JSON.
        """
        try:
            with open(self.ruta_fichero, "w", encoding="utf-8") as f:
                json.dump(self.notas, f, ensure_ascii=False, indent=4)
            print("Notas guardadas correctamente.")
        except OSError as e:
            print("Error al guardar el fichero de notas:", e)

    def anadir_o_modificar_nota(self, alumno, nota):
        """
        Añade o modifica la nota de un alumno.
        """
        self.notas[alumno] = nota
        print(f"Nota de '{alumno}' actualizada a {nota}.")

    def eliminar_alumno(self, alumno):
        """
        Elimina un alumno del registro de notas.
        """
        if alumno in self.notas:
            del self.notas[alumno]
            print(f"Alumno '{alumno}' eliminado.")
        else:
            print("El alumno no existe.")

    def mostrar_notas(self):
        """
        Muestra todas las notas.
        """
        if not self.notas:
            print("No hay notas registradas.")
            return
        print("\n--- LISTADO DE NOTAS ---")
        for alumno, nota in self.notas.items():
            print(f"{alumno}: {nota}")


def mostrar_menu():
    """
    Muestra el menú principal y devuelve la opción elegida.
    """
    print("\n===== GESTOR DE NOTAS =====")
    print("1. Mostrar notas")
    print("2. Añadir o modificar nota")
    print("3. Eliminar alumno")
    print("4. Guardar y salir")
    return input("Elige una opción (1-4): ")


def main():
    """
    Función principal del programa.
    """
    gestor = GestorNotas("notas.json")

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            gestor.mostrar_notas()
        elif opcion == "2":
            alumno = input("Nombre del alumno: ").strip()
            if alumno == "":
                print("El nombre no puede estar vacío.")
                continue
            try:
                nota = float(input("Nota del alumno: "))
            except ValueError:
                print("La nota debe ser numérica.")
                continue
            gestor.anadir_o_modificar_nota(alumno, nota)
        elif opcion == "3":
            alumno = input("Nombre del alumno a eliminar: ").strip()
            gestor.eliminar_alumno(alumno)
        elif opcion == "4":
            gestor.guardar()
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
