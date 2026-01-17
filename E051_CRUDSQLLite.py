"""
CRUD completo con sqlite3
Crea un programa que gestione una base de datos SQLite tienda.db con tabla productos (id, nombre, precio, stock).
Implementa un menú completo con:
- CREATE: Insertar nuevo producto.
- READ: Listar todos o buscar por nombre.
- UPDATE: Modificar precio/stock.
- DELETE: Eliminar producto.
- Backup de la BD completa a backup.db.
"""

# Programa 51: CRUD completo con SQLite3

import sqlite3
import os
from datetime import datetime


class GestorTienda:
    """
    Gestor completo de base de datos SQLite para productos.
    """
    
    def __init__(self, ruta_bd="tienda.db"):
        self.ruta_bd = ruta_bd
        self.conexion = None
        self.crear_tabla()
    
    def conectar(self):
        """Establece conexión con la BD."""
        self.conexion = sqlite3.connect(self.ruta_bd)
        self.conexion.row_factory = sqlite3.Row  # Para acceso por nombre
    
    def desconectar(self):
        """Cierra conexión."""
        if self.conexion:
            self.conexion.close()
    
    def crear_tabla(self):
        """Crea tabla productos si no existe."""
        self.conectar()
        cursor = self.conexion.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL UNIQUE,
                precio REAL NOT NULL CHECK(precio > 0),
                stock INTEGER NOT NULL DEFAULT 0 CHECK(stock >= 0),
                fecha_creacion TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.conexion.commit()
        self.desconectar()
    
    def crear(self, nombre, precio, stock=0):
        """Inserta nuevo producto."""
        try:
            self.conectar()
            cursor = self.conexion.cursor()
            cursor.execute(
                "INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)",
                (nombre, precio, stock)
            )
            self.conexion.commit()
            print(f"✅ Producto '{nombre}' creado con ID {cursor.lastrowid}")
            return cursor.lastrowid
        except sqlite3.IntegrityError:
            print(f"❌ Producto '{nombre}' ya existe.")
        except sqlite3.Error as e:
            print(f"❌ Error BD: {e}")
        finally:
            self.desconectar()
    
    def leer_todos(self):
        """Lista todos los productos."""
        self.conectar()
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM productos ORDER BY nombre")
        productos = cursor.fetchall()
        self.desconectar()
        return productos
    
    def buscar_por_nombre(self, texto):
        """Busca productos por nombre."""
        self.conectar()
        cursor = self.conexion.cursor()
        cursor.execute(
            "SELECT * FROM productos WHERE nombre LIKE ? ORDER BY nombre",
            (f"%{texto}%",)
        )
        productos = cursor.fetchall()
        self.desconectar()
        return productos
    
    def actualizar(self, id_producto, precio=None, stock=None):
        """Actualiza precio o stock de un producto."""
        self.conectar()
        cursor = self.conexion.cursor()
        cambios = []
        params = []
        
        if precio is not None:
            cambios.append("precio = ?")
            params.append(precio)
        if stock is not None:
            cambios.append("stock = ?")
            params.append(stock)
        
        if not cambios:
            print("❌ No se especificaron campos a actualizar.")
            self.desconectar()
            return
        
        params.append(id_producto)
        sql = f"UPDATE productos SET {', '.join(cambios)} WHERE id = ?"
        
        resultado = cursor.execute(sql, params)
        self.conexion.commit()
        self.desconectar()
        
        if resultado.rowcount > 0:
            print(f"✅ Producto ID {id_producto} actualizado.")
        else:
            print(f"❌ Producto ID {id_producto} no encontrado.")
    
    def eliminar(self, id_producto):
        """Elimina producto por ID."""
        self.conectar()
        cursor = self.conexion.cursor()
        resultado = cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
        self.conexion.commit()
        self.desconectar()
        
        if resultado.rowcount > 0:
            print(f"✅ Producto ID {id_producto} eliminado.")
        else:
            print(f"❌ Producto ID {id_producto} no encontrado.")
    
    def hacer_backup(self, ruta_backup="backup.db"):
        """Crea backup completo de la BD."""
        try:
            self.conectar()
            self.conexion.backup(sqlite3.connect(ruta_backup))
            self.desconectar()
            print(f"✅ Backup creado: {ruta_backup}")
        except sqlite3.Error as e:
            print(f"❌ Error en backup: {e}")


def mostrar_menu():
    """Muestra menú principal."""
    print("\n=== GESTOR DE TIENDA ===")
    print("1. Listar todos")
    print("2. Buscar por nombre")
    print("3. Crear producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Backup BD")
    print("0. Salir")
    return input("Opción: ")


def main():
    """Función principal."""
    gestor = GestorTienda()
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            productos = gestor.leer_todos()
            if productos:
                print("\nPRODUCTOS:")
                for p in productos:
                    print(f"ID:{p['id']:2d} {p['nombre']:15s} €{p['precio']:6.2f} stock:{p['stock']:3d}")
            else:
                print("No hay productos.")
        
        elif opcion == "2":
            texto = input("Texto a buscar: ")
            productos = gestor.buscar_por_nombre(texto)
            if productos:
                print(f"\n{len(productos)} producto(s) encontrado(s):")
                for p in productos:
                    print(f"  ID:{p['id']} {p['nombre']} - €{p['precio']}")
            else:
                print("No se encontraron productos.")
        
        elif opcion == "3":
            nombre = input("Nombre: ")
            precio = float(input("Precio: "))
            stock = int(input("Stock [0]: ") or 0)
            gestor.crear(nombre, precio, stock)
        
        elif opcion == "4":
            try:
                id_prod = int(input("ID producto: "))
                precio = input("Nuevo precio [actual]: ")
                precio = float(precio) if precio else None
                stock = input("Nuevo stock [actual]: ")
                stock = int(stock) if stock else None
                gestor.actualizar(id_prod, precio, stock)
            except ValueError:
                print("ID, precio o stock inválido.")
        
        elif opcion == "5":
            try:
                id_prod = int(input("ID a eliminar: "))
                gestor.eliminar(id_prod)
            except ValueError:
                print("ID inválido.")
        
        elif opcion == "6":
            gestor.hacer_backup()
        
        elif opcion == "0":
            print("¡Adiós!")
            break
        
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
