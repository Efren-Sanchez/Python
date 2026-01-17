"""
Sistema de menú para listar, actualizar y borrar artículos.
Tabla: CREATE TABLE articulos (id INT PRIMARY KEY, nombre VARCHAR(100), precio DECIMAL(10,2));
Inserta datos de prueba antes.
"""

# Programa 63: Actualización y borrado con menú

import mysql.connector
from mysql.connector import Error

CONFIGURACION_BD = {'host': 'localhost', 'database': 'ejercicios_dam', 'user': 'root', 'password': 'root'}

def conectar():
    """Conexión a BD."""
    try:
        return mysql.connector.connect(**CONFIGURACION_BD)
    except Error as e:
        print(f"Error: {e}")
        return None

def listar_articulos(conexion):
    """Muestra todos los artículos."""
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM articulos")
    for art in cursor.fetchall():
        print(f"ID: {art[0]}, {art[1]} - {art[2]}€")
    cursor.close()

def actualizar_precio(conexion):
    """Actualiza precio por ID."""
    id_art = int(input("ID artículo: "))
    nuevo_precio = float(input("Nuevo precio: "))
    cursor = conexion.cursor()
    try:
        cursor.execute("UPDATE articulos SET precio = %s WHERE id = %s", (nuevo_precio, id_art))
        conexion.commit()
        print("Precio actualizado." if cursor.rowcount > 0 else "Artículo no encontrado.")
    except Error as e:
        print(f"Error: {e}")
    cursor.close()

def borrar_articulo(conexion):
    """Borra artículo por ID."""
    id_art = int(input("ID a borrar: "))
    cursor = conexion.cursor()
    try:
        cursor.execute("DELETE FROM articulos WHERE id = %s", (id_art,))
        conexion.commit()
        print("Borrado." if cursor.rowcount > 0 else "No encontrado.")
    except Error as e:
        print(f"Error: {e}")
    cursor.close()

def mostrar_menu():
    """Muestra menú interactivo."""
    conexion = conectar()
    if not conexion:
        return
    while True:
        print("\n1. Listar\n2. Actualizar precio\n3. Borrar\n4. Salir")
        opcion = input("Opción: ")
        if opcion == '1':
            listar_articulos(conexion)
        elif opcion == '2':
            actualizar_precio(conexion)
        elif opcion == '3':
            borrar_articulo(conexion)
        elif opcion == '4':
            break
        else:
            print("Opción inválida.")
    conexion.close()

if __name__ == "__main__":
    mostrar_menu()
