"""
Gestor de configuración con configparser
Crea un programa que lea configuración desde config.ini con secciones [DATABASE], [LOGGING], [API].
Debe:
- Validar que existan todas las secciones y claves obligatorias.
- Permitir sobrescribir configuración desde variables de entorno.
- Mostrar la configuración final cargada.
"""

# Programa 47: Gestor de configuración con configparser

import configparser
import os


class GestorConfiguracion:
    """
    Gestor que lee configuración desde fichero y variables de entorno.
    """
    
    def __init__(self, ruta_fichero="config.ini"):
        self.config = configparser.ConfigParser()
        self.ruta_fichero = ruta_fichero
        self.cargar()
    
    def cargar(self):
        """
        Carga configuración validando secciones obligatorias.
        """
        secciones_obligatorias = ["DATABASE", "LOGGING", "API"]
        claves_obligatorias = {
            "DATABASE": ["host", "puerto", "usuario"],
            "LOGGING": ["nivel", "fichero"],
            "API": ["clave", "url_base"]
        }
        
        self.config.read(self.ruta_fichero, encoding="utf-8")
        
        # Validar secciones
        for seccion in secciones_obligatorias:
            if not self.config.has_section(seccion):
                raise ValueError(f"Sección '{seccion}' faltante en {self.ruta_fichero}")
        
        # Validar claves obligatorias
        for seccion, claves in claves_obligatorias.items():
            for clave in claves:
                if not self.config.has_option(seccion, clave):
                    raise ValueError(f"Clave '{clave}' faltante en sección '{seccion}'")
        
        # Sobrescribir con variables de entorno
        self._sobrescribir_entorno()
    
    def _sobrescribir_entorno(self):
        """
        Sobrescribe valores con variables de entorno.
        """
        for seccion in self.config.sections():
            for clave, valor in self.config.items(seccion):
                var_entorno = f"{seccion}_{clave}".upper()
                if var_entorno in os.environ:
                    self.config[seccion][clave] = os.environ[var_entorno]
    
    def obtener(self, seccion, clave, tipo=str):
        """
        Obtiene un valor configurado con tipo de conversión.
        """
        valor = self.config.get(seccion, clave)
        return tipo(valor)
    
    def mostrar_configuracion(self):
        """
        Muestra toda la configuración cargada.
        """
        print("=== CONFIGURACIÓN CARGADA ===")
        for seccion in self.config.sections():
            print(f"[{seccion}]")
            for clave, valor in self.config.items(seccion):
                print(f"  {clave} = {valor}")
            print()


def main():
    """
    Función principal del programa.
    """
    try:
        gestor = GestorConfiguracion("config.ini")
        gestor.mostrar_configuracion()
        
        # Ejemplo de uso
        print("\nEjemplos de obtención:")
        print(f"Host BD: {gestor.obtener('DATABASE', 'host')}")
        print(f"Nivel log: {gestor.obtener('LOGGING', 'nivel')}")
        print(f"Clave API: {gestor.obtener('API', 'clave')}")
        
    except (ValueError, configparser.Error) as e:
        print(f"Error de configuración: {e}")


if __name__ == "__main__":
    main()
