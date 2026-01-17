'''
Copo de Nieve Variante
Modifica la curva de Koch con matplotlib para crear un copo de nieve con picos alternos hacia arriba/abajo. Usa 6 lados en lugar de 3 y ángulos variables (60°,120°). Experimenta con orden 5 y colores degradé por profundidad recursiva.
​'''

# Ejercicio 11: Copo de Nieve Variante con matplotlib

import matplotlib.pyplot as plt
import numpy as np
import random

def dibujar_brazo(ax, x, y, angulo, longitud, orden, color):
    if orden == 0:
        return
    
    # Calcular destino del segmento principal
    x_dest = x + longitud * np.cos(angulo)
    y_dest = y + longitud * np.sin(angulo)
    
    # Dibujar el segmento
    ax.plot([x, x_dest], [y, y_dest], color=color, lw=orden*0.5, alpha=0.8)
    
    # Generar ramificaciones laterales (simetría del brazo)
    # Se ramifica en puntos intermedios del segmento actual
    num_ramas = 3
    for i in range(1, num_ramas + 1):
        # Punto de ramificación
        px = x + (x_dest - x) * (i / (num_ramas + 1))
        py = y + (y_dest - y) * (i / (num_ramas + 1))
        
        # Ángulo y longitud de las ramas (aleatoriedad controlada)
        ang_rama = np.radians(random.uniform(30, 45))
        nueva_long = longitud * random.uniform(0.4, 0.6)
        
        # Rama izquierda
        dibujar_brazo(ax, px, py, angulo + ang_rama, nueva_long, orden - 1, color)
        # Rama derecha
        dibujar_brazo(ax, px, py, angulo - ang_rama, nueva_long, orden - 1, color)

def generar_copo_dendritico():
    fig, ax = plt.subplots(figsize=(8, 8), facecolor='#00050a')
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Parámetros globales del copo
    color_hielo = random.choice(['#E0F7FA', '#B2EBF2', '#FFFFFF', '#81D4FA'])
    orden_recursivo = 4
    longitud_base = 100
    
    # Un copo real siempre tiene 6 ejes principales
    # Semilla aleatoria fija para reproducibilidad (comentar para asimetría natural)
    random.seed(42)
    for i in range(6):
        angulo_eje = np.radians(i * 60)
        dibujar_brazo(ax, 0, 0, angulo_eje, longitud_base, orden_recursivo, color_hielo)
    
    plt.show()

# Ejecución
generar_copo_dendritico()
