"""
Generador de documentacion automatica con inspect
Crea un sistema que genere documentacion HTML automaticamente:
- Inspecciona modulos/clases/funciones con inspect
- Extrae docstrings y firmas
- Genera plantillas HTML con estilos
- Incluye ejemplos de uso ejecutables
Procesa un directorio completo de .py.
"""

# Programa 60: Generador de documentacion automatica

import inspect
import os
import sys
from pathlib import Path
from importlib.util import spec_from_file_location, module_from_spec


def generar_html_doc(modulo_obj, nombre_modulo="modulo"):
    """
    Genera HTML para un modulo/objeto desde inspect.
    """
    html = """
<!DOCTYPE html>
<html>
<head>
    <title>Documentacion Automatica</title>
    <style>
        body { font-family: Arial; margin: 40px; }
        .modulo { background: #e3f2fd; padding: 20px; border-radius: 8px; }
        .funcion { background: #f3e5f5; margin: 10px 0; padding: 15px; }
        .clase { background: #e8f5e9; margin: 10px 0; padding: 15px; }
        pre { background: #f5f5f5; padding: 10px; border-radius: 4px; overflow-x: auto; }
    </style>
</head>
<body>
"""
    
    # Info del modulo
    html += f'<div class="modulo"><h1>{nombre_modulo}</h1>'
    if hasattr(modulo_obj, '__file__'):
        html += f'<p><strong>Archivo:</strong> {modulo_obj.__file__}</p>'
    
    # Funciones y clases
    for nombre, obj in inspect.getmembers(modulo_obj):
        if inspect.isfunction(obj) or inspect.isclass(obj):
            firma = inspect.signature(obj)
            docstring = inspect.getdoc(obj) or "Sin documentacion"
            
            tipo_clase = "funcion" if inspect.isfunction(obj) else "clase"
            html += f'<div class="{tipo_clase}">'
            html += f'<h3>{nombre}{firma}</h3>'
            html += f'<pre>{docstring.strip()}</pre>'
            
            # Si es una clase, documentar sus metodos
            if inspect.isclass(obj):
                for nombre_metodo, metodo in inspect.getmembers(obj):
                    if inspect.isfunction(metodo) and not nombre_metodo.startswith('_'):
                        firma_metodo = inspect.signature(metodo)
                        docstring_metodo = inspect.getdoc(metodo) or "Sin documentacion"
                        html += f'<div style="margin-left: 20px;">'
                        html += f'<h4>{nombre_metodo}{firma_metodo}</h4>'
                        html += f'<pre>{docstring_metodo.strip()}</pre>'
                        html += '</div>'
            
            html += "</div>"
    
    html += "</body></html>"
    return html


def cargar_modulo_desde_archivo(ruta_archivo):
    """
    Carga un modulo Python desde un archivo .py
    """
    nombre_modulo = Path(ruta_archivo).stem
    spec = spec_from_file_location(nombre_modulo, ruta_archivo)
    if spec and spec.loader:
        modulo = module_from_spec(spec)
        sys.modules[nombre_modulo] = modulo
        spec.loader.exec_module(modulo)
        return modulo
    return None


def procesar_directorio_doc(raiz_directorio, salida_html):
    """
    Procesa directorio completo generando documentacion unificada.
    """
    html_total = """
<!DOCTYPE html>
<html><head><title>Documentacion Proyecto</title>
<style>
    body{font-family:Arial;margin:40px;}
    h2{margin-top:40px;border-bottom:2px solid #333;}
    .modulo{background:#e3f2fd;padding:15px;border-radius:8px;margin:10px 0;}
</style></head>
<body><h1>Documentacion Automatica del Proyecto</h1>
<h2>Directorio: {raiz}</h2>
""".format(raiz=raiz_directorio)
    
    archivos_procesados = 0
    errores = []
    
    for py_archivo in Path(raiz_directorio).glob("**/*.py"):
        if py_archivo.is_file() and py_archivo.name != "__init__.py":
            try:
                modulo = cargar_modulo_desde_archivo(str(py_archivo))
                if modulo:
                    nombre_modulo = py_archivo.stem
                    doc_modulo = generar_html_doc(modulo, nombre_modulo)
                    html_total += f'<div class="modulo"><h2>{py_archivo.name}</h2>{doc_modulo}</div>'
                    archivos_procesados += 1
                else:
                    errores.append(f"No se pudo cargar: {py_archivo.name}")
            except Exception as e:
                errores.append(f"Error en {py_archivo.name}: {e}")
    
    if errores:
        html_total += "<h2>Errores</h2><ul>"
        for error in errores:
            html_total += f"<li>{error}</li>"
        html_total += "</ul>"
    
    html_total += "</body></html>"
    
    with open(salida_html, "w", encoding="utf-8") as f:
        f.write(html_total)
    
    print(f"Documentacion generada: {salida_html}")
    print(f"Archivos procesados: {archivos_procesados}")
    if errores:
        print(f"Errores: {len(errores)}")


# Modulo de ejemplo para documentar
def suma(a: int, b: int) -> int:
    """
    Suma dos numeros enteros.
    
    Args:
        a: Primer numero
        b: Segundo numero
    
    Returns:
        Suma de ambos numeros.
    """
    return a + b


def multiplicar(a: float, b: float) -> float:
    """
    Multiplica dos numeros.
    
    Args:
        a: Primer factor
        b: Segundo factor
    
    Returns:
        Producto de ambos factores.
    """
    return a * b


class Calculadora:
    """
    Calculadora basica con operaciones fundamentales.
    Soporta suma, resta, multiplicacion y division.
    """
    
    @staticmethod
    def resta(a, b):
        """Resta dos numeros."""
        return a - b
    
    @staticmethod
    def division(a, b):
        """Divide dos numeros. Lanza ZeroDivisionError si b es 0."""
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a / b
    
    def __init__(self, precision=2):
        """Inicializa calculadora con precision decimal."""
        self.precision = precision
    
    def get_precision(self):
        """Devuelve la precision actual."""
        return self.precision


def main():
    """
    Funcion principal de demostracion.
    """
    # Documentar modulo actual
    doc_actual = generar_html_doc(__name__, "Documentacion del Modulo Actual")
    with open("docs_modulo_actual.html", "w", encoding="utf-8") as f:
        f.write(doc_actual)
    print("Documentacion del modulo actual: docs_modulo_actual.html")
    
    # Procesar directorio (ejemplo con directorio actual)
    directorio = input("Directorio a documentar [.] : ").strip() or "."
    if os.path.isdir(directorio):
        procesar_directorio_doc(directorio, "documentacion_completa.html")
    else:
        print(f"El directorio '{directorio}' no existe.")


if __name__ == "__main__":
    main()
