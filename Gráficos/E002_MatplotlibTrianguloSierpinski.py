'''
Triángulo de Sierpinski
Crea una función recursiva que genere el triángulo de Sierpinski de nivel n (por ejemplo, n=6) con turtle o matplotlib. Parte de un triángulo equilátero inicial y en cada iteración, divide cada lado en dos y conecta los puntos medios, eliminando el triángulo central. Colorea las áreas para resaltar la estructura fractal.
'''

# Ejercicio 2: Triángulo de Sierpinski con Matplotlib

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def dibujar_triangulo_sierpinski(ax, vertices, nivel):
    """
    Dibuja recursivamente triángulos de Sierpinski.
    ax: axes de matplotlib
    vertices: array 3x2 con vértices del triángulo actual
    nivel: nivel de recursión restante
    """
    if nivel == 0:
        triangulo = patches.Polygon(vertices, closed=True, facecolor='red', edgecolor='darkred', alpha=0.7)
        ax.add_patch(triangulo)
    else:
        # Puntos medios
        v0, v1, v2 = vertices
        m01 = (v0 + v1) / 2
        m12 = (v1 + v2) / 2
        m20 = (v2 + v0) / 2
        
        # Tres sub-triángulos
        dibujar_triangulo_sierpinski(ax, np.array([v0, m01, m20]), nivel - 1)
        dibujar_triangulo_sierpinski(ax, np.array([m01, v1, m12]), nivel - 1)
        dibujar_triangulo_sierpinski(ax, np.array([m20, m12, v2]), nivel - 1)

def programa_sierpinski(nivel):
    """Programa principal."""
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title(f'Triángulo de Sierpinski (nivel {nivel})')
    
    # Triángulo inicial
    lado = 400
    altura = lado * np.sqrt(3) / 2
    vertices = np.array([
        [-lado/2, -altura/3],
        [lado/2, -altura/3],
        [0, 2*altura/3]
    ])
    
    dibujar_triangulo_sierpinski(ax, vertices, nivel)
    plt.xlim(-lado/2 - 10, lado/2 + 10)
    plt.ylim(-altura/3 - 10, 2*altura/3 + 10)
    plt.show()

# Ejecutar con nivel 6
programa_sierpinski(6)
