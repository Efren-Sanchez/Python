"""
Context Manager personalizado para archivos temporales
Define un context manager ArchivoTemporal usando @contextmanager que:
- Cree un fichero temporal al entrar en el bloque with.
- Permita escribir/leer datos durante su uso.
- Elimine automáticamente el fichero al salir del bloque, incluso si hay errores.
"""

# Programa 44: Context Manager para archivos temporales

from contextlib import contextmanager
import tempfile
import os


@contextmanager
def archivo_temporal(suffix=""):
    """
    Context manager que crea un fichero temporal que se elimina automáticamente.
    """
    # Crear fichero temporal
    descriptor, ruta = tempfile.mkstemp(suffix=suffix)
    
    try:
        # Abrir fichero para escritura/lectura
        with os.fdopen(descriptor, "w+", encoding="utf-8") as f:
            yield f, ruta
            # El fichero sigue abierto aquí
    finally:
        # Cerrar y eliminar automáticamente
        try:
            os.unlink(ruta)
            print(f"Fichero temporal '{ruta}' eliminado.")
        except OSError as e:
            print(f"Error al eliminar fichero temporal: {e}")


def main():
    """
    Función principal que prueba el context manager.
    """
    print("Probando context manager de fichero temporal...")
    
    with archivo_temporal(".txt") as (fichero, ruta):
        print(f"Fichero temporal creado: {ruta}")
        
        # Escribir datos
        fichero.write("¡Hola desde el fichero temporal!\n")
        fichero.write("Línea 2: Probando context manager.\n")
        fichero.flush()
        
        # Leer datos
        fichero.seek(0)
        contenido = fichero.read()
        print("Contenido escrito:")
        print(contenido)
    
    print("Bloque 'with' terminado (fichero ya eliminado).")


if __name__ == "__main__":
    main()
