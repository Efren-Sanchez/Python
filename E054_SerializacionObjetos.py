"""
Serialización de objetos complejos con pickle
Crea clases Pedido y Cliente con relaciones anidadas.
Implementa funciones para:
- Serializar objetos complejos a pedidos.pkl.
- Deserializar y validar integridad.
- Migrar de pickle v1 a v2 cambiando estructura.
- Comparar objetos original vs deserializado.
"""

# Programa 54: Serialización compleja con pickle

import pickle
import os


class Cliente:
    """
    Clase Cliente serializable.
    """
    def __init__(self, nombre, email, pedidos_ids=None):
        self.nombre = nombre
        self.email = email
        self.pedidos_ids = pedidos_ids or []
    
    def __repr__(self):
        return f"Cliente({self.nombre}, {self.email}, pedidos={self.pedidos_ids})"


class Pedido:
    """
    Clase Pedido serializable.
    """
    def __init__(self, id_pedido, productos, total):
        self.id_pedido = id_pedido
        self.productos = productos
        self.total = total
    
    def __repr__(self):
        return f"Pedido(id={self.id_pedido}, total=€{self.total:.2f})"


def serializar_objetos(cliente, pedidos, ruta_fichero):
    """
    Serializa cliente y pedidos relacionados.
    """
    datos = {
        "cliente": cliente,
        "pedidos": pedidos,
        "version": 1
    }
    with open(ruta_fichero, "wb") as f:
        pickle.dump(datos, f)
    print(f"✅ Serializado en '{ruta_fichero}'")


def deserializar_validar(ruta_fichero):
    """
    Deserializa y valida integridad.
    """
    if not os.path.exists(ruta_fichero):
        raise FileNotFoundError(f"No existe {ruta_fichero}")
    
    with open(ruta_fichero, "rb") as f:
        datos = pickle.load(f)
    
    # Validar estructura
    if "cliente" not in datos or "pedidos" not in datos:
        raise ValueError("Estructura inválida")
    
    cliente = datos["cliente"]
    pedidos = datos["pedidos"]
    
    # Validar referencias
    for pedido in pedidos:
        if pedido.id_pedido not in cliente.pedidos_ids:
            print("⚠️  Referencia rota detectada")
    
    return cliente, pedidos


def migrar_pickle_v1_v2(ruta_origen, ruta_destino):
    """
    Migra de versión 1 a 2 añadiendo campo fecha.
    """
    cliente, pedidos = deserializar_validar(ruta_origen)
    
    # Añadir campo fecha a v2
    cliente.fecha_registro = "2026-01-01"
    for pedido in pedidos:
        pedido.fecha = "2026-01-09"
    
    datos_v2 = {
        "cliente": cliente,
        "pedidos": pedidos,
        "version": 2
    }
    
    with open(ruta_destino, "wb") as f:
        pickle.dump(datos_v2, f)
    print(f"✅ Migrado a v2: '{ruta_destino}'")


def main():
    """
    Función principal de demostración.
    """
    # Crear datos de ejemplo
    cliente = Cliente("Ana García", "ana@email.com", ["P001", "P002"])
    pedido1 = Pedido("P001", ["Portátil", "Ratón"], 1299.99)
    pedido2 = Pedido("P002", ["Teclado"], 89.99)
    
    # Serializar
    serializar_objetos(cliente, [pedido1, pedido2], "pedidos_v1.pkl")
    
    # Deserializar y validar
    cliente_recuperado, pedidos_recuperados = deserializar_validar("pedidos_v1.pkl")
    print("Cliente recuperado:", cliente_recuperado)
    print("Pedidos recuperados:", pedidos_recuperados)
    
    # Comparar
    print(f"¿Cliente igual? {cliente == cliente_recuperado}")
    
    # Migrar
    migrar_pickle_v1_v2("pedidos_v1.pkl", "pedidos_v2.pkl")


if __name__ == "__main__":
    main()
