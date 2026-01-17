"""
Sistema de logging configurable
Crea un programa que use el modulo logging para registrar eventos en diferentes niveles (DEBUG, INFO, WARNING, ERROR).
Debe permitir:
- Configurar el nivel de logging desde un fichero de configuracion (config.ini).
- Registrar mensajes en fichero y consola simultaneamente.
- Formatear las entradas con timestamp, nivel y nombre del modulo.
"""

# Programa 41: Sistema de logging configurable

import logging
import logging.config
import configparser
from pathlib import Path


def crear_configuracion_defecto():
    """
    Crea el archivo de configuracion si no existe.
    """
    config = configparser.ConfigParser()
    
    # Seccion DEFAULT con valores por defecto
    config["DEFAULT"] = {
        "level": "INFO"
    }
    
    # Seccion para el logger principal
    config["LOG_MAIN"] = {
        "level": "DEBUG",
        "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        "file": "aplicacion.log",
        "to_console": "true"
    }
    
    # Guardar configuracion
    with open("logging.conf", "w", encoding="utf-8") as f:
        config.write(f)
    
    return config


def configurar_logging():
    """
    Configura el sistema de logging desde un fichero de configuracion.
    """
    config = configparser.ConfigParser()
    
    # Crear archivo de configuracion si no existe
    if not Path("logging.conf").exists():
        config = crear_configuracion_defecto()
    
    # Leer configuracion
    config.read("logging.conf", encoding="utf-8")
    
    # Obtener configuracion del logger principal
    if "LOG_MAIN" in config:
        nivel = getattr(logging, config["LOG_MAIN"].get("level", "DEBUG").upper())
        formato = config["LOG_MAIN"].get("format", "%(asctime)s [%(levelname)s] %(name)s: %(message)s")
        archivo_log = config["LOG_MAIN"].get("file", "aplicacion.log")
        a_consola = config["LOG_MAIN"].getboolean("to_console", True)
    else:
        # Valores por defecto
        nivel = logging.DEBUG
        formato = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
        archivo_log = "aplicacion.log"
        a_consola = True
    
    # Crear handlers
    handlers = []
    
    if archivo_log:
        handlers.append(logging.FileHandler(archivo_log))
    
    if a_consola:
        handlers.append(logging.StreamHandler())
    
    # Configurar logging
    logging.basicConfig(
        level=nivel,
        format=formato,
        handlers=handlers
    )


def main():
    """
    Funcion principal que prueba diferentes niveles de logging.
    """
    configurar_logging()
    logger = logging.getLogger("MiAplicacion")
    
    logger.debug("Este es un mensaje DEBUG")
    logger.info("Este es un mensaje INFO")
    logger.warning("¡Advertencia!")
    logger.error("¡Error grave!")
    logger.critical("¡Error critico!")
    
    print("\nTambien se han guardado en 'aplicacion.log'")


if __name__ == "__main__":
    main()
