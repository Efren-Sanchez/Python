'''
Helecho de Barnsley
Escribe un programa que simule el helecho de Barnsley aplicando cuatro transformaciones afines probabilísticas (probabilidades: 0.85, 0.07, 0.07, 0.01) a un punto inicial (0,0) durante 50,000 iteraciones con matplotlib. Usa random para seleccionar cada regla y plotea los puntos resultantes en verde para simular hojas.
'''

# Ejercicio 4: Helecho de Barnsley con Matplotlib

import matplotlib.pyplot as plt
import numpy as np

def generar_helecho(iteraciones):
    x = np.zeros(iteraciones)
    y = np.zeros(iteraciones)
    
    for i in range(1, iteraciones):
        r = np.random.random()
        xi, yi = x[i-1], y[i-1]
        
        if r < 0.01:
            # Tallo
            x[i] = 0
            y[i] = 0.16 * yi
        elif r < 0.86:
            # Hojas pequeñas
            x[i] = 0.85 * xi + 0.04 * yi
            y[i] = -0.04 * xi + 0.85 * yi + 1.6
        elif r < 0.93:
            # Rama izquierda
            x[i] = 0.2 * xi - 0.26 * yi
            y[i] = 0.23 * xi + 0.22 * yi + 1.6
        else:
            # Rama derecha
            x[i] = -0.15 * xi + 0.28 * yi
            y[i] = 0.26 * xi + 0.24 * yi + 0.44
            
    return x, y

def dibujar_helecho(iteraciones):
    x, y = generar_helecho(iteraciones)
    
    plt.figure(figsize=(7, 10), facecolor='black')
    # Uso de 'g,' para pintar píxeles individuales (mucho más rápido que scatter)
    plt.plot(x, y, 'g,', markersize=0.1)
    plt.title(f'Helecho de Barnsley - {iteraciones:,} it.', color='white')
    plt.axis('off')
    plt.show()

dibujar_helecho(50000)