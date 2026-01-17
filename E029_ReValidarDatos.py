"""
Uso de re para validar datos con clases
Define una clase Validador que agrupe métodos estáticos para validar:
- Un correo electrónico.
- Un número de teléfono español sencillo (por ejemplo, 9 dígitos).
- Un DNI con formato básico (8 dígitos y una letra).
Usa la librería re (expresiones regulares).
Crea un programa que pida esos datos al usuario y muestre si cada uno es válido o no.
"""

# Programa 29: Clase Validador con expresiones regulares

import re  # Para trabajar con expresiones regulares


class Validador:
    """
    Clase que agrupa métodos estáticos para validar distintos datos.
    """

    @staticmethod
    def es_email_valido(email):
        """
        Valida un correo electrónico de forma sencilla.
        """
        patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return re.match(patron, email) is not None

    @staticmethod
    def es_telefono_valido(telefono):
        """
        Valida un número de teléfono español simple: 9 dígitos.
        """
        patron = r"^\d{9}$"
        return re.match(patron, telefono) is not None

    @staticmethod
    def es_dni_valido(dni):
        """
        Valida un DNI básico: 8 dígitos y una letra final.
        (No se comprueba la letra correcta, solo el formato.)
        """
        patron = r"^\d{8}[A-Za-z]$"
        return re.match(patron, dni) is not None


def main():
    """
    Función principal del programa.
    """
    email = input("Introduce un correo electrónico: ")
    telefono = input("Introduce un teléfono (9 dígitos): ")
    dni = input("Introduce un DNI (8 dígitos y una letra): ")

    print("\nRESULTADOS DE LA VALIDACIÓN:")

    print("Email válido:" if Validador.es_email_valido(email) else "Email NO válido.")
    print("Teléfono válido:" if Validador.es_telefono_valido(telefono) else "Teléfono NO válido.")
    print("DNI válido:" if Validador.es_dni_valido(dni) else "DNI NO válido.")


if __name__ == "__main__":
    main()
