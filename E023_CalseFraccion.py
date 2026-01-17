"""
Clase Fraccion con operaciones básicas
Crea una clase Fraccion que represente una fracción con numerador y denominador.
Debe permitir:
- Sumar y restar fracciones (métodos que devuelvan nuevas fracciones).
- Simplificar la fracción a su forma irreducible.
- Mostrar la fracción en formato a/b.
Usa, si quieres, math.gcd para simplificar.
"""

# Programa 23: Clase Fraccion con operaciones básicas

import math  # Para calcular el máximo común divisor


class Fraccion:
    """
    Clase que representa una fracción numerador/denominador.
    """

    def __init__(self, numerador, denominador):
        if denominador == 0:
            raise ValueError("El denominador no puede ser cero.")
        self.numerador = numerador
        self.denominador = denominador
        self.simplificar()

    def simplificar(self):
        """
        Simplifica la fracción dividiendo numerador y denominador
        por su máximo común divisor.
        """
        mcd = math.gcd(self.numerador, self.denominador)
        self.numerador //= mcd
        self.denominador //= mcd

    def sumar(self, otra):
        """
        Suma la fracción actual con otra fracción y devuelve una nueva fracción.
        """
        nuevo_num = self.numerador * otra.denominador + otra.numerador * self.denominador
        nuevo_den = self.denominador * otra.denominador
        return Fraccion(nuevo_num, nuevo_den)

    def restar(self, otra):
        """
        Resta otra fracción a la fracción actual y devuelve una nueva fracción.
        """
        nuevo_num = self.numerador * otra.denominador - otra.numerador * self.denominador
        nuevo_den = self.denominador * otra.denominador
        return Fraccion(nuevo_num, nuevo_den)

    def __str__(self):
        """
        Devuelve una representación en texto de la fracción.
        """
        return f"{self.numerador}/{self.denominador}"


def main():
    """
    Función principal del programa.
    """
    print("Creando fracciones 1/2 y 3/4...")
    f1 = Fraccion(1, 2)
    f2 = Fraccion(3, 4)

    print("Fracción 1:", f1)
    print("Fracción 2:", f2)

    suma = f1.sumar(f2)
    resta = f1.restar(f2)

    print("Suma:", suma)
    print("Resta:", resta)


if __name__ == "__main__":
    main()
