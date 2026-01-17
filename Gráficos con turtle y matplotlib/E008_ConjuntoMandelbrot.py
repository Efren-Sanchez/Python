'''
Conjunto de Mandelbrot
Desarrolla con matplotlib el conjunto de Mandelbrot usando 500x500 píxeles. Colorea píxeles según iteraciones hasta |z|>2 para c en -2.5..1 (real) y -1.5..1.5 (imaginario). Usa mapa de colores 'hot' con zoom interactivo opcional.
'''

# Ejercicio 8: Conjunto de Mandelbrot con matplotlib

import matplotlib.pyplot as plt
import numpy as np

def mandelbrot(ancho, alto, max_iter):
    # Crear el plano complejo directamente
    x = np.linspace(-2.5, 1.0, ancho)
    y = np.linspace(-1.5, 1.5, alto)
    X, Y = np.meshgrid(x, y)
    C = X + 1j * Y
    
    Z = np.zeros(C.shape, dtype=complex)
    # Matriz para almacenar en qué iteración escapa cada punto
    escape_iter = np.full(C.shape, max_iter, dtype=int)
    # Máscara de puntos que aún no han escapado
    puntos_en_vuelo = np.full(C.shape, True, dtype=bool)

    for i in range(max_iter):
        # Solo calculamos sobre los puntos que no han escapado (|z| <= 2)
        Z[puntos_en_vuelo] = Z[puntos_en_vuelo]**2 + C[puntos_en_vuelo]
        
        # Identificar puntos que acaban de escapar
        escaparon_ahora = (np.abs(Z) > 2) & puntos_en_vuelo
        escape_iter[escaparon_ahora] = i
        
        # Actualizar los que siguen bajo control
        puntos_en_vuelo &= ~escaparon_ahora
        
        # Optimización: si todos han escapado, salir
        if not np.any(puntos_en_vuelo):
            break
            
    return escape_iter

def dibujar_mandelbrot():
    # Aumentamos max_iter para mayor detalle en los bordes
    m_set = mandelbrot(500, 500, 100)
    
    plt.figure(figsize=(10, 8))
    # 'hot' es el mapa de colores solicitado
    img = plt.imshow(m_set, extent=[-2.5, 1, -1.5, 1.5], cmap='hot')
    plt.colorbar(img, label="Velocidad de escape (iteración)")
    plt.title("Conjunto de Mandelbrot (Vectorizado)")
    plt.xlabel("Re(c)")
    plt.ylabel("Im(c)")
    plt.show()

dibujar_mandelbrot()