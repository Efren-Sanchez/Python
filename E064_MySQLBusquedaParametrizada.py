"""
Programa de búsqueda con LIKE parametrizado en tabla 'empleados'.
Tabla ejemplo: CREATE TABLE empleados (id INT PRIMARY KEY, nombre VARCHAR(100), apellido VARCHAR(100), salario DECIMAL(10,2));
"""

# Programa 64: Búsqueda parametrizada y prevención de inyección

import mysql.connector
from mysql.connector import Error

CONFIGURACION_BD = {'host': 'localhost', 'database': 'ejercicios_dam', 'user': 'root', 'password': 'root'}

def conectar():
    """Establece conexión."""
    try:
        return mysql.connector.connect(**CONFIGURACION_BD)
    except Error:
        print("Error conexión.")
        return None

def buscar_empleados(conexion):
    """Búsqueda segura con parámetro."""
    texto_busqueda = input("Texto para buscar en apellidos: ").strip()
    cursor = conexion.cursor()
    try:
        cursor.execute("SELECT id, nombre, apellido, salario FROM empleados WHERE apellido LIKE %s", (f"%{texto_busqueda}%",))
        resultados = cursor.fetchall()
        if resultados:
            print("\nResultados:")
            for emp in resultados:
                print(f"ID: {emp[0]} - {emp[1]} {emp[2]} - {emp[3]}€")
        else:
            print("No hay coincidencias.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()

def main():
    """Ejecuta búsqueda."""
    conexion = conectar()
    if conexion:
        buscar_empleados(conexion)
        conexion.close()

if __name__ == "__main__":
    main()
