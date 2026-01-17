"""
Generador de números primos infinitos
Implementa un generador infinito que produzca números primos consecutivos usando yield.
El programa debe:
- Permitir al usuario pedir los primeros N primos.
- Mostrar el tiempo que tarda en generar los primeros 1000 primos.
- Guardar los primos generados en una lista limitada para no consumir memoria.
"""

# Programa 42: Generador infinito de números primos

import time
from itertools import count


def es_primo(numero):
    """
    Comprueba si un número es primo.
    """
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True


def generador_primos():
    """
    Generador infinito que produce números primos consecutivos.
    """
    for numero in count(2):
        if es_primo(numero):
            yield numero


def main():
    """
    Función principal que prueba el generador.
    """
    print("Generador de primos en marcha...")
    
    # Obtener primeros 20 primos
    print("Primeros 20 números primos:")
    primos = []
    for i, primo in enumerate(generador_primos()):
        primos.append(primo)
        print(f"{i+1:2d}: {primo}", end=" ")
        if (i+1) % 10 == 0:
            print()
        if i >= 19:
            break
    print()
    
    # Tiempo para primeros 1000 primos
    inicio = time.time()
    cantidad = 1000
    lista_primos = list(generador_primos())
    lista_primos = lista_primos[:cantidad]
    fin = time.time()
    
    print(f"\nTiempo para generar {cantidad} primos: {fin-inicio:.3f} segundos")
    print(f"Último primo: {lista_primos[-1]}")
    print(f"Memoria usada: ~{len(lista_primos) * 28} bytes")


if __name__ == "__main__":
    main()
