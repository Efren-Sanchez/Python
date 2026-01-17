"""
Servidor TCP concurrente con threading
Crea un servidor TCP en puerto 8888 que acepte multiples clientes simultaneos usando threading.
Cada cliente puede:
- Enviar mensajes que se broadcast a todos los conectados.
- Comando /salir para desconectarse.
- Mostrar lista de clientes conectados con /lista.
"""

# Programa 53: Servidor TCP concurrente
# Ejecutar: python programa3.py

import socket
import threading
import time


class ClienteHandler(threading.Thread):
    """
    Maneja un cliente individual en hilo separado.
    """
    def __init__(self, socket_cliente, clientes_conectados):
        super().__init__()
        self.socket_cliente = socket_cliente
        self.clientes_conectados = clientes_conectados
        self.nombre_cliente = None
    
    def run(self):
        """
        Bucle principal del cliente.
        """
        try:
            # Pedir nombre
            self.socket_cliente.send(b"Introduce tu nombre: ")
            self.nombre_cliente = self.socket_cliente.recv(1024).decode().strip()
            self.clientes_conectados[self.nombre_cliente] = self.socket_cliente
            
            mensaje_bienvenida = f"¡Hola {self.nombre_cliente}! Escribe /salir o /lista\n"
            self.socket_cliente.send(mensaje_bienvenida.encode())
            
            # Broadcast de conexion
            self.broadcast(f"{self.nombre_cliente} se ha conectado ({len(self.clientes_conectados)} conectados)")
            
            while True:
                datos = self.socket_cliente.recv(1024).decode().strip()
                if not datos:
                    break
                
                if datos == "/salir":
                    self.socket_cliente.send("¡Hasta luego!\n")
                    break
                elif datos == "/lista":
                    lista = "Conectados: " + ", ".join(self.clientes_conectados.keys())
                    self.socket_cliente.send((lista + "\n").encode())
                else:
                    self.broadcast(f"{self.nombre_cliente}: {datos}")
        
        except ConnectionResetError:
            pass
        except Exception:
            pass  # Manejo de errores de comunicacion
        finally:
            self.desconectar()
    
    def broadcast(self, mensaje):
        """
        Envia mensaje a todos los clientes.
        """
        # Crear lista de nombres a eliminar para evitar modificar durante iteracion
        nombres_a_eliminar = []
        
        for nombre, sock in list(self.clientes_conectados.items()):
            try:
                sock.send((mensaje + "\n").encode())
            except (BrokenPipeError, ConnectionResetError, OSError):
                # Cliente desconectado, marcar para eliminar
                nombres_a_eliminar.append(nombre)
        
        # Eliminar clientes que fallaron
        for nombre in nombres_a_eliminar:
            if nombre in self.clientes_conectados:
                del self.clientes_conectados[nombre]
    
    def desconectar(self):
        """
        Limpia conexion del cliente.
        """
        if self.nombre_cliente and self.nombre_cliente in self.clientes_conectados:
            del self.clientes_conectados[self.nombre_cliente]
            self.broadcast(f"{self.nombre_cliente} se ha desconectado")
        self.socket_cliente.close()


def servidor_tcp(puerto=8888):
    """
    Servidor TCP principal.
    """
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    servidor.bind(("localhost", puerto))
    servidor.listen(5)
    
    print(f"Servidor TCP escuchando en localhost:{puerto}")
    print("Conecta con: telnet localhost 8888")
    
    clientes_conectados = {}
    
    try:
        while True:
            socket_cliente, addr = servidor.accept()
            print(f"Nueva conexion desde {addr}")
            handler = ClienteHandler(socket_cliente, clientes_conectados)
            handler.start()
    except KeyboardInterrupt:
        print("\nCerrando servidor...")
    finally:
        servidor.close()


if __name__ == "__main__":
    servidor_tcp()
