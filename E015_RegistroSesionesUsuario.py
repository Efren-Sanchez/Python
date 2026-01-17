"""
Registro de sesiones de usuario
Crea un programa que simule el inicio y cierre de sesión de usuarios.
Cada vez que un usuario inicie o cierre sesión, registra el evento en un fichero de texto con el formato usuario;accion;fecha_hora. Usa la librería datetime para obtener la marca temporal.
"""

# Programa 15: Registro de sesiones de usuario

from datetime import datetime  # Para obtener fecha y hora actual


def registrar_evento(usuario, accion, ruta_fichero="sesiones.log"):
    """
    Registra un evento de inicio o cierre de sesión en un fichero de texto.
    Formato: usuario;accion;fecha_hora
    """
    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linea = f"{usuario};{accion};{fecha_hora}"
    try:
        with open(ruta_fichero, "a", encoding="utf-8") as f:
            f.write(linea + "\n")
    except OSError as e:
        print("Error al escribir en el fichero de registro:", e)


def mostrar_menu():
    """
    Muestra el menú principal y devuelve la opción elegida.
    """
    print("\n===== REGISTRO DE SESIONES =====")
    print("1. Iniciar sesión")
    print("2. Cerrar sesión")
    print("3. Salir")
    opcion = input("Elige una opción (1-3): ")
    return opcion


def main():
    """
    Función principal del programa.
    """
    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            usuario = input("Introduce el nombre de usuario: ").strip()
            if usuario:
                registrar_evento(usuario, "INICIO")
                print("Inicio de sesión registrado.")
            else:
                print("El nombre de usuario no puede estar vacío.")

        elif opcion == "2":
            usuario = input("Introduce el nombre de usuario: ").strip()
            if usuario:
                registrar_evento(usuario, "CIERRE")
                print("Cierre de sesión registrado.")
            else:
                print("El nombre de usuario no puede estar vacío.")

        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    main()
