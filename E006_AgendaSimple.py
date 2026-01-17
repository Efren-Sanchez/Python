"""
Agenda simple
Crea un pequeño programa de agenda de contactos que guarde en un fichero JSON (json):
- Añadir contacto (nombre, teléfono, email).
- Buscar contacto por nombre.
- Listar todos los contactos.
"""

# Programa 6: Agenda simple de contactos usando JSON

import json  # Para leer/escribir ficheros JSON
import os    # Para comprobar si existe el fichero


RUTA_FICHERO = "agenda.json"


def cargar_agenda():
    """
    Carga la agenda desde un fichero JSON.
    Si el fichero no existe o hay error, devuelve una lista vacía.
    La agenda será una lista de diccionarios con claves:
    'nombre', 'telefono', 'email'
    """
    if not os.path.exists(RUTA_FICHERO):
        return []

    try:
        with open(RUTA_FICHERO, "r", encoding="utf-8") as f:
            agenda = json.load(f)
            # Nos aseguramos de que sea una lista
            if isinstance(agenda, list):
                return agenda
            else:
                return []
    except (json.JSONDecodeError, OSError):
        print("Error al leer el fichero de agenda.")
        return []


def guardar_agenda(agenda):
    """
    Guarda la agenda (lista de contactos) en un fichero JSON.
    """
    try:
        with open(RUTA_FICHERO, "w", encoding="utf-8") as f:
            json.dump(agenda, f, ensure_ascii=False, indent=4)
        print("Agenda guardada correctamente.")
    except OSError as e:
        print("Error al guardar la agenda:", e)


def mostrar_menu():
    """
    Muestra el menú principal y devuelve la opción elegida por el usuario.
    """
    print("\n===== AGENDA DE CONTACTOS =====")
    print("1. Añadir contacto")
    print("2. Buscar contacto por nombre")
    print("3. Listar todos los contactos")
    print("4. Salir")
    opcion = input("Elige una opción (1-4): ")
    return opcion


def anadir_contacto(agenda):
    """
    Pide por teclado los datos de un contacto y lo añade a la agenda.
    """
    print("\n--- Añadir contacto ---")
    nombre = input("Nombre: ").strip()
    telefono = input("Teléfono: ").strip()
    email = input("Email: ").strip()

    if nombre == "":
        print("El nombre no puede estar vacío.")
        return

    contacto = {
        "nombre": nombre,
        "telefono": telefono,
        "email": email
    }
    agenda.append(contacto)
    print("Contacto añadido correctamente.")


def buscar_contacto(agenda):
    """
    Pide un nombre y muestra los contactos cuyo nombre contenga
    el texto introducido (búsqueda simple).
    """
    print("\n--- Buscar contacto ---")
    termino = input("Introduce el nombre o parte del nombre: ").strip().lower()
    if termino == "":
        print("No se ha introducido ningún texto.")
        return

    encontrados = []
    for contacto in agenda:
        if termino in contacto["nombre"].lower():
            encontrados.append(contacto)

    if encontrados:
        print(f"Se han encontrado {len(encontrados)} contacto(s):")
        for c in encontrados:
            print(f"- {c['nombre']} | Tel: {c['telefono']} | Email: {c['email']}")
    else:
        print("No se han encontrado contactos con ese nombre.")


def listar_contactos(agenda):
    """
    Muestra todos los contactos de la agenda.
    """
    print("\n--- Listar todos los contactos ---")
    if not agenda:
        print("La agenda está vacía.")
        return

    for i, contacto in enumerate(agenda, start=1):
        print(f"{i}. {contacto['nombre']} | Tel: {contacto['telefono']} | Email: {contacto['email']}")


def main():
    """
    Función principal del programa.
    """
    agenda = cargar_agenda()

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            anadir_contacto(agenda)
            guardar_agenda(agenda)
        elif opcion == "2":
            buscar_contacto(agenda)
        elif opcion == "3":
            listar_contactos(agenda)
        elif opcion == "4":
            print("Saliendo de la agenda...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    main()
