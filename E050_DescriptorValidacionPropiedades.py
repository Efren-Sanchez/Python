"""
Descriptor para validación de propiedades
Define un descriptor EnteroPositivo que:
- Solo permita asignar valores enteros positivos a una propiedad.
- Lance ValueError si se asigna un valor inválido.
- Se use en una clase Producto para validar stock y precio.
"""

# Programa 50: Descriptor para validación de propiedades

class EnteroPositivo:
    """
    Descriptor que valida que el valor sea entero positivo.
    """
    
    def __init__(self):
        self._valor_interno = None
        self._nombre = None
    
    def __set_name__(self, owner, name):
        self._nombre = name
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return self._valor_interno
    
    def __set__(self, obj, valor):
        if not isinstance(valor, int):
            raise ValueError(f"{self._nombre} debe ser entero")
        if valor < 0:
            raise ValueError(f"{self._nombre} debe ser positivo")
        self._valor_interno = valor


class Producto:
    """
    Clase que usa el descriptor para validar stock y precio.
    """
    stock = EnteroPositivo()
    precio = EnteroPositivo()
    
    def __init__(self, nombre):
        self.nombre = nombre
        self._stock = 0
        self._precio = 0
    
    @property
    def valor_total(self):
        """Valor total del stock (stock * precio)."""
        return self._stock * self._precio
    
    def __str__(self):
        return f"{self.nombre}: stock={self._stock}, precio={self._precio}, total={self.valor_total}"


def main():
    """
    Función principal que prueba el descriptor.
    """
    print("=== PRUEBA DESCRIPTOR EnteroPositivo ===\n")
    
    try:
        producto = Producto("Ordenador")
        producto.stock = 10
        producto.precio = 899
        
        print(producto)
        print(f"Valor total en stock: €{producto.valor_total:,}")
        
        # Pruebas de error
        print("\nProbando asignaciones inválidas:")
        producto.stock = -5  # Debe fallar
    except ValueError as e:
        print(f"✅ Error capturado: {e}")
    
    try:
        producto.precio = 3.14  # Debe fallar
    except ValueError as e:
        print(f"✅ Error capturado: {e}")


if __name__ == "__main__":
    main()
