"""
Clase Rectangulo con métodos geométricos
Define una clase Rectangulo con atributos ancho y alto.
La clase debe incluir:
- Método para calcular área y perímetro.
- Método que indique si es un cuadrado.
- Método que permita escalar el rectángulo por un factor (multiplicar ancho y alto).
Crea varios objetos y muestra sus datos por pantalla.
"""

# Programa 21: Clase Rectangulo con métodos geométricos

class Rectangulo:
    """
    Clase que representa un rectángulo mediante su ancho y alto.
    """

    def __init__(self, ancho, alto):
        """
        Constructor de la clase.
        """
        self.ancho = ancho
        self.alto = alto

    def area(self):
        """
        Calcula y devuelve el área del rectángulo.
        """
        return self.ancho * self.alto

    def perimetro(self):
        """
        Calcula y devuelve el perímetro del rectángulo.
        """
        return 2 * (self.ancho + self.alto)

    def es_cuadrado(self):
        """
        Devuelve True si el rectángulo es un cuadrado.
        """
        return self.ancho == self.alto

    def escalar(self, factor):
        """
        Escala el rectángulo multiplicando ancho y alto por un factor.
        """
        self.ancho *= factor
        self.alto *= factor

    def __str__(self):
        """
        Devuelve una representación en texto del rectángulo.
        """
        return f"Rectángulo(ancho={self.ancho}, alto={self.alto})"


def main():
    """
    Función principal para probar la clase Rectangulo.
    """
    # Creamos algunos rectángulos de ejemplo
    r1 = Rectangulo(4, 5)
    r2 = Rectangulo(3, 3)

    print("Datos del rectángulo 1:")
    print(r1)
    print("Área:", r1.area())
    print("Perímetro:", r1.perimetro())
    print("¿Es cuadrado?:", r1.es_cuadrado())

    print("\nDatos del rectángulo 2:")
    print(r2)
    print("Área:", r2.area())
    print("Perímetro:", r2.perimetro())
    print("¿Es cuadrado?:", r2.es_cuadrado())

    print("\nEscalando el rectángulo 1 por factor 2...")
    r1.escalar(2)
    print(r1)
    print("Nueva área:", r1.area())


if __name__ == "__main__":
    main()
