'''
Curva del Dragón
Desarrolla un script que trace la curva del Dragón (o "Dragon Curve") de orden n usando recursión con turtle. Comienza con una línea recta, aplica giros alternos de 90° (derecha e izquierda) en cada iteración doblando la curva sobre sí misma, y visualiza el resultado para n=10. Experimenta con colores por nivel de recursión.
'''

# Ejercicio 3: Curva del Dragón con Matplotlib

import matplotlib.pyplot as plt
import numpy as np

def secuencia_dragon(n):
    """
    Genera la secuencia de giros de la curva del Dragón:
    +1 = giro a la derecha, -1 = giro a la izquierda.
    """
    giros = [1]  # orden 1
    for _ in range(1, n):
        # Nuevo = giros + [1] + invertido y cambiado de signo
        giros = giros + [1] + [-g for g in giros[::-1]]
    return giros

def puntos_curva_dragon(orden):
    """
    Genera puntos de la curva del Dragón de orden 'orden'.
    Devuelve array (N, 2).
    """
    if orden == 0:
        return np.array([[0.0, 0.0], [1.0, 0.0]])

    giros = secuencia_dragon(orden)
    # Punto inicial y dirección inicial (eje X positivo)
    x, y = 0.0, 0.0
    dx, dy = 1.0, 0.0

    puntos = [(x, y)]
    for g in giros:
        # Avanza un segmento
        x += dx
        y += dy
        puntos.append((x, y))

        # Gira 90°: derecha (+1) o izquierda (-1)
        if g == 1:      # derecha
            dx, dy = dy, -dx
        else:           # izquierda
            dx, dy = -dy, dx

    return np.array(puntos)

def dibujar_dragon(orden):
    """Programa principal."""
    puntos = puntos_curva_dragon(orden)

    plt.figure(figsize=(8, 8))
    plt.plot(puntos[:, 0], puntos[:, 1], color='green', linewidth=1)
    plt.title(f'Curva del Dragón (orden {orden})')
    plt.axis('equal')
    plt.axis('off')
    plt.show()

# Ejecutar con orden 10
dibujar_dragon(10)

def dibujar_dragon_coloreado(orden):
    """Dibuja la curva del dragón con gradiente de color por segmento."""
    puntos = puntos_curva_dragon(orden)
    N = len(puntos) - 1
    colores = np.linspace(0, 1, N)

    plt.figure(figsize=(8, 8))
    for i in range(N):
        plt.plot(puntos[i:i+2, 0], puntos[i:i+2, 1],
                 color=plt.cm.plasma(colores[i]), linewidth=1)
    plt.title(f'Curva del Dragón coloreada (orden {orden})')
    plt.axis('equal')
    plt.axis('off')
    plt.show()

# Ejemplo de curva coloreada:
dibujar_dragon_coloreado(10)
