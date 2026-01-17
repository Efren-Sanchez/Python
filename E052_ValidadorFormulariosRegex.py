"""
Validador de formularios con expresiones regulares
Implementa una clase ValidadorFormulario que valide todos los campos de un formulario web:
text
- Nombre completo (solo letras + espacios)
- Email (formato estándar)
- Teléfono español (9 dígitos)
- DNI (8 dígitos + letra)
- Código postal (5 dígitos)
- Fecha dd/mm/aaaa válida
Muestra errores específicos por campo.
"""

# Programa 52: Validador de formularios completo

import re
from datetime import datetime


class ValidadorFormulario:
    """
    Valida todos los campos típicos de un formulario web.
    """
    
    PATRONES = {
        "nombre": r"^[A-Za-zÁÉÍÓÚÜÑáéíóúüñ\s]+$",
        "email": r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
        "telefono": r"^\d{9}$",
        "dni": r"^\d{8}[TRWAGMYFPDXBNJZSQVHLCKE]$",
        "codigo_postal": r"^\d{5}$",
        "fecha": r"^(0[1-9]|[12]\d|3[01])/(0[1-9]|1[0-2])/(19|20)\d{2}$"
    }
    
    @staticmethod
    def validar_nombre(nombre):
        """Nombre completo: solo letras y espacios."""
        return bool(re.match(ValidadorFormulario.PATRONES["nombre"], nombre.strip()))
    
    @staticmethod
    def validar_email(email):
        """Email formato estándar."""
        return bool(re.match(ValidadorFormulario.PATRONES["email"], email.strip()))
    
    @staticmethod
    def validar_telefono(telefono):
        """Teléfono español: 9 dígitos."""
        return bool(re.match(ValidadorFormulario.PATRONES["telefono"], telefono.strip()))
    
    @staticmethod
    def validar_dni(dni):
        """DNI: 8 dígitos + letra válida."""
        if not re.match(ValidadorFormulario.PATRONES["dni"], dni.strip().upper()):
            return False
        # Validar letra de control
        numeros = int(dni[:8])
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        return letras[numeros % 23] == dni[8].upper()
    
    @staticmethod
    def validar_codigo_postal(cp):
        """Código postal español: 5 dígitos."""
        return bool(re.match(ValidadorFormulario.PATRONES["codigo_postal"], cp.strip()))
    
    @staticmethod
    def validar_fecha(fecha_str):
        """Fecha dd/mm/aaaa válida."""
        if not re.match(ValidadorFormulario.PATRONES["fecha"], fecha_str.strip()):
            return False
        try:
            datetime.strptime(fecha_str, "%d/%m/%Y")
            return True
        except ValueError:
            return False
    
    @staticmethod
    def validar_formulario(datos):
        """
        Valida formulario completo y devuelve errores por campo.
        """
        errores = {}
        
        if not ValidadorFormulario.validar_nombre(datos.get("nombre", "")):
            errores["nombre"] = "Solo letras y espacios permitidos"
        if not ValidadorFormulario.validar_email(datos.get("email", "")):
            errores["email"] = "Formato de email inválido"
        if not ValidadorFormulario.validar_telefono(datos.get("telefono", "")):
            errores["telefono"] = "9 dígitos numéricos"
        if not ValidadorFormulario.validar_dni(datos.get("dni", "")):
            errores["dni"] = "DNI inválido (8 dígitos + letra control)"
        if not ValidadorFormulario.validar_codigo_postal(datos.get("codigo_postal", "")):
            errores["codigo_postal"] = "5 dígitos"
        if not ValidadorFormulario.validar_fecha(datos.get("fecha_nacimiento", "")):
            errores["fecha_nacimiento"] = "Formato dd/mm/aaaa inválido"
        
        return errores


def main():
    """
    Función principal interactiva.
    """
    print("=== VALIDADOR DE FORMULARIO ===")
    
    formulario = {}
    
    formulario["nombre"] = input("Nombre completo: ")
    formulario["email"] = input("Email: ")
    formulario["telefono"] = input("Teléfono: ")
    formulario["dni"] = input("DNI: ")
    formulario["codigo_postal"] = input("Código postal: ")
    formulario["fecha_nacimiento"] = input("Fecha nacimiento (dd/mm/aaaa): ")
    
    errores = ValidadorFormulario.validar_formulario(formulario)
    
    if not errores:
        print("\n✅ ¡TODOS LOS CAMPOS SON VÁLIDOS!")
        print("Formulario aceptado.")
    else:
        print("\n❌ ERRORES ENCONTRADOS:")
        for campo, error in errores.items():
            print(f"  {campo}: {error}")


if __name__ == "__main__":
    main()
