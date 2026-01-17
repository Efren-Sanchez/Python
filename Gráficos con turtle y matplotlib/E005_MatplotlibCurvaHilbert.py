'''
Curva de Hilbert
Implementa la curva de Hilbert de orden n (por ejemplo, n=5) con una función recursiva en turtle. Esta curva rellena un cuadrado dividiendo recursivamente en cuatro subcuadrados, girando 90° y conectando con pasos hacia adelante. Asegúrate de que sea continua y sin autointersecciones, ideal para mostrar espacio-filling.
'''

# Ejercicio 5: Curva de Hilbert con Turtle con Matplotlib

import matplotlib.pyplot as plt
import numpy as np

def hilbert_recursivo(x0, y0, xi, xj, yi, yj, orden):
    """
    x0, y0: coordenadas base
    xi, xj: vector dirección x
    yi, yj: vector dirección y
    """
    if orden <= 0:
        # Retorna el centro del cuadrado actual
        return [x0 + (xi + yi) / 2], [y0 + (xj + yj) / 2]
    
    # Dividir en 4 subcuadrantes y rotar según la regla de Hilbert
    # Cuadrante 1: inferior izquierdo (rotado)
    x1, y1 = hilbert_recursivo(x0, y0, yi/2, yj/2, xi/2, xj/2, orden-1)
    # Cuadrante 2: superior izquierdo
    x2, y2 = hilbert_recursivo(x0 + xi/2, y0 + xj/2, xi/2, xj/2, yi/2, yj/2, orden-1)
    # Cuadrante 3: superior derecho
    x3, y3 = hilbert_recursivo(x0 + xi/2 + yi/2, y0 + xj/2 + yj/2, xi/2, xj/2, yi/2, yj/2, orden-1)
    # Cuadrante 4: inferior derecho (rotado y reflejado)
    x4, y4 = hilbert_recursivo(x0 + xi/2 + yi, y0 + xj/2 + yj, -yi/2, -yj/2, -xi/2, -xj/2, orden-1)
    
    return x1 + x2 + x3 + x4, y1 + y2 + y3 + y4

def dibujar_hilbert_matplotlib(orden):
    # Definición de vectores base unitarios
    x, y = hilbert_recursivo(0, 0, 1, 0, 0, 1, orden)
    
    plt.figure(figsize=(10, 10))
    plt.plot(x, y, color='purple', linewidth=1.5)
    plt.title(f'Curva de Hilbert - Orden {orden} (Matplotlib)')
    plt.axis('equal')
    plt.axis('off')
    plt.tight_layout()
    plt.show()

dibujar_hilbert_matplotlib(5)