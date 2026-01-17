"""
Buscador del Mini-GoogleBot.
Uso: python buscador.py "programacion web"
"""

import sys
import mysql.connector
from mysql.connector import Error
import re

CONFIG_BD = {
    'host': 'localhost',
    'database': 'googlebot',
    'user': 'root',
    'password': 'root'
}

def preparar_consulta(consulta):
    """
    Prepara la consulta para búsqueda BOOLEAN MODE.
    Convierte "programacion web" a +programacion +web
    """
    palabras = consulta.strip().split()
    if len(palabras) == 1:
        return f'+{palabras[0]}*'  # Búsqueda con prefijo
    else:
        return ' '.join(f'+{p}' for p in palabras)  # Todas las palabras requeridas

def buscar_documentos(consulta):
    """Busca documentos por relevancia."""
    conexion = None
    try:
        conexion = mysql.connector.connect(**CONFIG_BD)
        cursor = conexion.cursor(dictionary=True)
        
        consulta_boolean = preparar_consulta(consulta)
        
        # Consulta FULLTEXT con ponderación por título
        cursor.execute("""
            SELECT url, titulo, 
                   (MATCH(titulo) AGAINST (%s IN BOOLEAN MODE) * 3 +
                    MATCH(contenido_texto) AGAINST (%s IN NATURAL LANGUAGE MODE)) as relevancia
            FROM paginas 
            WHERE MATCH(titulo, contenido_texto) AGAINST (%s IN BOOLEAN MODE)
            ORDER BY relevancia DESC 
            LIMIT 10
        """, (consulta_boolean, consulta, consulta_boolean))
        
        resultados = cursor.fetchall()
        return resultados
        
    except Error as e:
        print(f"Error BD: {e}")
        return []
    finally:
        if conexion:
            conexion.close()

def mostrar_resultados(resultados):
    """Muestra resultados formateados."""
    if not resultados:
        print("No se encontraron resultados")
        return
    
    print(f"\n{len(resultados)} resultados encontrados:\n")
    for i, doc in enumerate(resultados, 1):
        titulo = doc['titulo'][:80] if doc['titulo'] else 'Sin titulo'
        print(f"{i}. {titulo}...")
        print(f"   {doc['url']}")
        print(f"   Relevancia: {doc['relevancia']:.1f}\n")

def main():
    if len(sys.argv) != 2:
        print("Uso: python buscador.py 'consulta'")
        return
    
    consulta = sys.argv[1].strip()
    if not consulta:
        print("Consulta vacia")
        return
    
    resultados = buscar_documentos(consulta)
    mostrar_resultados(resultados)

if __name__ == "__main__":
    main()
