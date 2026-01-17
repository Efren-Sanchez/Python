"""
Sistema CRUD completo para tabla 'alumnos'.
Tabla: CREATE TABLE alumnos (id INT PRIMARY KEY, nombre VARCHAR(100), edad INT, nota_media DECIMAL(4,2));
"""

# Programa 65: Mini CRUD completo sobre una tabla

import mysql.connector
from mysql.connector import Error

CONFIGURACION_BD = {'host': 'localhost', 'database': 'ejercicios_dam', 'user': 'root', 'password': 'root'}

def conectar():
    """Conexión reutilizable."""
    try:
        return mysql.connector.connect(**CONFIGURACION_BD)
    except Error as e:
        print(f"Error: {e}")
        return None

def crear_alumno(conexion):
    """Inserta nuevo alumno."""
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    nota = float(input("Nota media: "))
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO alumnos (nombre, edad, nota_media) VALUES (%s, %s, %s)", (nombre, edad, nota))
    conexion.commit()
    print(f"ID creado: {cursor.lastrowid}")

def listar_alumnos(conexion):
    """Lista todos."""
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM alumnos")
    for alu in cursor.fetchall():
        print(f"ID: {alu[0]}, {alu[1]}, {alu[2]} años, nota: {alu[3]}")
    cursor.close()

def actualizar_nota(conexion):
    """Actualiza nota por ID."""
    id_al = int(input("ID: "))
    nota = float(input("Nueva nota: "))
    cursor = conexion.cursor()
    cursor.execute("UPDATE alumnos SET nota_media = %s WHERE id = %s", (nota, id_al))
    conexion.commit()
    print("Actualizado." if cursor.rowcount else "No encontrado.")

def borrar_alumno(conexion):
    """Borra por ID."""
    id_al = int(input("ID a borrar: "))
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM alumnos WHERE id = %s", (id_al,))
    conexion.commit()
    print("Borrado." if cursor.rowcount else "No encontrado.")

def menu_crud():
    """Menú principal CRUD."""
    conexion = conectar()
    if not conexion: return
    while True:
        print("\n1.Crear 2.Listar 3.Actualizar 4.Borrar 5.Salir")
        op = input("Opción: ")
        if op == '1': crear_alumno(conexion)
        elif op == '2': listar_alumnos(conexion)
        elif op == '3': actualizar_nota(conexion)
        elif op == '4': borrar_alumno(conexion)
        elif op == '5': break
    conexion.close()

if __name__ == "__main__":
    menu_crud()
