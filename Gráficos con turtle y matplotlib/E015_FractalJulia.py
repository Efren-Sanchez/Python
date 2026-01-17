'''
Fractal de Julia
    Con matplotlib genera el conjunto de Julia para c=-0.8+0.156i. Itera z_{n+1}=z_n²+c desde z_0=-0.5+0.5i en rejilla 800x800. Colorea por velocidad de escape con mapa 'plasma' y compara con Mandelbrot.
'''

# Ejercicio 15: Fractal de Julia con matplotlib

import matplotlib.pyplot as plt
import numpy as np

def julia(c, ancho, alto, max_iter):
    """
    Conjunto de Julia para constante c compleja.
    """
    x = np.linspace(-1.5, 1.5, ancho)
    y = np.linspace(-1.5, 1.5, alto)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y
    divergencia = np.zeros(Z.shape, dtype=int)
    
    for i in range(max_iter):
        mask = np.abs(Z) <= 2
        Z[mask] = Z[mask]**2 + c
        divergencia[np.abs(Z) > 2] = i
    
    return divergencia

def dibujar_julia():
    """Programa principal Julia c=-0.8+0.156i."""
    c = complex(-0.8, 0.156)
    julia_set = julia(c, 800, 800, 100)
    
    plt.figure(figsize=(12, 12))
    plt.imshow(julia_set, cmap='plasma', extent=[-1.5, 1.5, -1.5, 1.5])
    plt.title("Conjunto de Julia (c = -0.8 + 0.156i)")
    plt.colorbar(label="Iteraciones")
    plt.show()

# Ejecutar
dibujar_julia()
