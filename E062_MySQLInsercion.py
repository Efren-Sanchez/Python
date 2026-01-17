"""
Programa para insertar un producto desde teclado en tabla 'productos'.
Tabla ejemplo: CREATE TABLE productos (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(100), precio DECIMAL(10,2), stock INT);
"""

# Programa 62: Inserción de datos desde teclado

import mysql.connector
from mysql.connector import Error

CONFIGURACION_BD = {
    'host': 'localhost',
    'database': 'ejercicios_dam',
    'user': 'root',
    'password': 'root'
}

def conectar_base_datos():
    """Conecta a la base de datos MySQL."""
    try:
        conexion = mysql.connector.connect(**CONFIGURACION_BD)
        return conexion
    except Error as error:
        print(f"Error conexión: {error}")
        return None

def insertar_producto(conexion):
    """Lee datos del usuario e inserta nuevo producto."""
    nombre = input("Nombre del producto: ").strip()
    precio = float(input("Precio (ej: 19.99): "))
    stock = int(input("Stock inicial: "))
    
    cursor = conexion.cursor()
    try:
        consulta = "INSERT INTO productos (nombre, precio, stock) VALUES (%s, %s, %s)"
        cursor.execute(consulta, (nombre, precio, stock))
        conexion.commit()
        print(f"Producto '{nombre}' insertado con ID: {cursor.lastrowid}")
    except Error as error:
        print(f"Error inserción: {error}")
        conexion.rollback()
    finally:
        cursor.close()

def main():
    """Ejecuta inserción de producto."""
    conexion = conectar_base_datos()
    if conexion:
        insertar_producto(conexion)
        conexion.close()
    input("\nPresiona Enter para salir...")

if __name__ == "__main__":
    main()
