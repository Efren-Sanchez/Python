"""
Singleton para conexión a base de datos
Implementa el patrón Singleton para una clase ConexionBD que:
- Garantice que solo exista una instancia en toda la aplicación.
- Simule conexión/desconexión a base de datos.
- Incluya método get_instancia() estático para obtener la única instancia.
"""

# Programa 49: Patrón Singleton para ConexionBD

class ConexionBD:
    """
    Singleton que garantiza una única instancia de conexión BD.
    """
    _instancia = None
    _inicializada = False
    
    def __new__(cls):
        if cls._instancia is None:
            print("Creando ÚNICA instancia de ConexionBD")
            cls._instancia = super(ConexionBD, cls).__new__(cls)
        return cls._instancia
    
    def __init__(self):
        if self._inicializada:
            return
        
        self.host = "localhost"
        self.puerto = 5432
        self.conectado = False
        self._inicializada = True
    
    @classmethod
    def get_instancia(cls):
        """
        Método de clase para obtener la instancia singleton.
        """
        if cls._instancia is None:
            cls._instancia = cls()
        return cls._instancia
    
    def conectar(self):
        """
        Simula conexión a base de datos.
        """
        if not self.conectado:
            print(f"Conectando a {self.host}:{self.puerto}...")
            self.conectado = True
        else:
            print("Ya estaba conectado.")
    
    def desconectar(self):
        """
        Simula desconexión.
        """
        if self.conectado:
            print("Desconectando de base de datos...")
            self.conectado = False
        else:
            print("No estaba conectado.")
    
    def ejecutar_consulta(self, sql):
        """
        Simula ejecución de consulta SQL.
        """
        if not self.conectado:
            raise RuntimeError("Debe conectarse primero")
        print(f"Ejecutando: {sql}")


def main():
    """
    Función principal que demuestra el singleton.
    """
    print("=== PRUEBA SINGLETON CONEXION BD ===\n")
    
    # Primera instancia
    print("1. Obteniendo primera instancia:")
    bd1 = ConexionBD.get_instancia()
    print(f"ID bd1: {id(bd1)}")
    
    # Segunda "instancia" (misma)
    print("\n2. Obteniendo segunda instancia:")
    bd2 = ConexionBD()
    print(f"ID bd2: {id(bd2)}")
    print("¡Son la MISMA instancia!")
    
    # Uso
    bd1.conectar()
    bd2.ejecutar_consulta("SELECT * FROM usuarios")
    bd1.desconectar()


if __name__ == "__main__":
    main()
