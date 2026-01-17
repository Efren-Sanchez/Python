'''
Curva de Koch
Implementa un programa en Python que dibuje la curva de Koch de orden n (por ejemplo, n=4) usando el módulo turtle. Divide cada segmento en tres partes iguales, sustituye el segmento central por los dos lados de un triángulo equilátero (rotando 60°), y repite recursivamente. Muestra el copo de nieve completo uniendo cuatro curvas.
'''

# Ejercicio 1: Curva de Koch (Copo de nieve) con Matplotlib

import numpy as np
import matplotlib.pyplot as plt

def koch_recursive(p1, p2, orden):
    if orden == 0:
        return [p1, p2]
    
    p1, p2 = np.array(p1), np.array(p2)
    v = (p2 - p1) / 3
    
    # Puntos de división
    a = p1 + v
    b = p1 + 2 * v
    
    # Rotación de 60° (pico exterior)
    # Matriz de rotación: [[cos, -sin], [sin, cos]]
    angle = np.pi / 3
    rot = np.array([[np.cos(angle), -np.sin(angle)], 
                    [np.sin(angle),  np.cos(angle)]])
    pico = a + rot @ v
    
    # Unir segmentos recursivamente
    return (koch_recursive(p1, a, orden - 1) + 
            koch_recursive(a, pico, orden - 1)[1:] + 
            koch_recursive(pico, b, orden - 1)[1:] + 
            koch_recursive(b, p2, orden - 1)[1:])

def dibujar_copo(orden):
    # Vértices del triángulo base (Sentido horario para picos exteriores con rot +60°)
    p0 = [0, 0]
    p1 = [0.5, np.sqrt(3)/2]
    p2 = [1, 0]
    
    # Generar los 3 lados del copo
    lados = [
        koch_recursive(p0, p1, orden),
        koch_recursive(p1, p2, orden),
        koch_recursive(p2, p0, orden)
    ]
    
    plt.figure(figsize=(8, 8))
    for l in lados:
        x, y = zip(*l)
        plt.plot(x, y, 'b-')
    
    plt.axis('equal')
    plt.axis('off')
    plt.show()

dibujar_copo(4)