"""
Programa completo para conectarse a MySQL y mostrar registros de tabla 'clientes'.
Requiere: pip install mysql-connector-python
Crear BD 'ejercicios_dam' con tabla clientes(id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(100), email VARCHAR(100))
Ejemplo INSERT: INSERT INTO clientes (nombre, email) VALUES ('Juan Pérez', 'juan@email.com'), ('Ana García', 'ana@email.com');
"""

# Programa 61: Conexión básica y consulta simple a MySQL


import mysql.connector
from mysql.connector import Error

# Configuración de la conexión (ajustar a tu servidor local)
CONFIGURACION_BD = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',      # Cambiar por tu usuario
    'password': 'root',  # Cambiar por tu contraseña
    'database': 'ejercicios_dam'
}

def conectar_base_datos():
    """Establece conexión a MySQL y devuelve el objeto conexión."""
    conexion = None
    try:
        conexion = mysql.connector.connect(**CONFIGURACION_BD)
        if conexion.is_connected():
            print("¡Conexión exitosa a MySQL!")
            return conexion
    except Error as error:
        print(f"Error al conectar: {error}")
    return conexion

def mostrar_clientes(conexion):
    """Ejecuta consulta SELECT y muestra todos los clientes."""
    cursor = conexion.cursor()
    try:
        cursor.execute("SELECT id, nombre, email FROM clientes")
        clientes = cursor.fetchall()
        if clientes:
            print("\nLista de clientes:")
            for cliente in clientes:
                print(f"ID: {cliente[0]}, Nombre: {cliente[1]}, Email: {cliente[2]}")
        else:
            print("No hay clientes en la tabla.")
    except Error as error:
        print(f"Error en consulta: {error}")
    finally:
        cursor.close()

def main():
    """Función principal del programa."""
    conexion = conectar_base_datos()
    if conexion:
        mostrar_clientes(conexion)
        conexion.close()
        print("Conexión cerrada.")
    else:
        print("No se pudo conectar a la BD.")

if __name__ == "__main__":
    main()
