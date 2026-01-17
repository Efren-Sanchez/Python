"""
Clase Cronometro usando time
Implementa una clase Cronometro que permita medir el tiempo transcurrido entre un inicio y un fin.
Debe tener métodos:
- iniciar(): guarda el tiempo de inicio.
- detener(): guarda el tiempo de fin.
- tiempo_transcurrido(): devuelve el tiempo en segundos entre inicio y fin.
Crea un pequeño programa que lo use para medir cuánto tarda el usuario en escribir una frase.
"""

# Programa 27: Clase Cronometro usando time

import time  # Para medir tiempos


class Cronometro:
    """
    Clase que permite medir tiempo transcurrido entre iniciar y detener.
    """

    def __init__(self):
        self.inicio = None
        self.fin = None

    def iniciar(self):
        """
        Guarda el instante de inicio.
        """
        self.inicio = time.time()
        self.fin = None

    def detener(self):
        """
        Guarda el instante de fin.
        """
        if self.inicio is None:
            print("El cronómetro no se ha iniciado.")
            return
        self.fin = time.time()

    def tiempo_transcurrido(self):
        """
        Devuelve el tiempo transcurrido en segundos.
        """
        if self.inicio is None or self.fin is None:
            print("El cronómetro no se ha iniciado o detenido correctamente.")
            return None
        return self.fin - self.inicio


def main():
    """
    Función principal del programa.
    """
    cronometro = Cronometro()
    print("Cuando pulses ENTER comenzará el cronómetro.")
    input("Pulsa ENTER para empezar a escribir una frase...")
    cronometro.iniciar()

    frase = input("Escribe una frase y pulsa ENTER: ")

    cronometro.detener()
    tiempo = cronometro.tiempo_transcurrido()
    if tiempo is not None:
        print(f"\nHas tardado {tiempo:.2f} segundos en escribir:")
        print(frase)


if __name__ == "__main__":
    main()
