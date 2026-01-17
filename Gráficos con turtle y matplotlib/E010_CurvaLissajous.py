'''
Curva de Lissajous
Genera con matplotlib figuras de Lissajous variando frecuencias f_x y f_y (ej: 3:4, 5:3). Usa ecuaciones x=sin(2πft+a), y=sin(2πft*b) para t∈. Prueba fases a=0°,90°,180° con colores distintos por fase.
'''

# Ejercicio 10: Curva de Lissajous con matplotlib

import matplotlib.pyplot as plt
import numpy as np

def lissajous(fx, fy, fase_grados):
    # Convertir fase a radianes
    fase_rad = np.radians(fase_grados)
    
    # t debe cubrir al menos un ciclo completo para cerrar la curva
    # Para frecuencias enteras, t de 0 a 1 es suficiente para un ciclo base
    t = np.linspace(0, 1, 1000)
    
    # Ecuaciones paramétricas corregidas
    x = np.sin(2 * np.pi * fx * t)
    y = np.sin(2 * np.pi * fy * t + fase_rad)
    return x, y

def dibujar_lissajous(ratio_x=3, ratio_y=4):
    fases = [0, 90, 180]
    colores = ['royalblue', 'crimson', 'forestgreen']
    
    fig, axs = plt.subplots(1, 3, figsize=(15, 5))
    
    for i, fase in enumerate(fases):
        x, y = lissajous(ratio_x, ratio_y, fase)
        
        axs[i].plot(x, y, color=colores[i], linewidth=2)
        axs[i].set_title(f'Fase = {fase}°', fontsize=12)
        axs[i].set_aspect('equal')
        axs[i].grid(True, linestyle='--', alpha=0.5)
        # Mantener ejes para referencia de amplitud [-1, 1]
        axs[i].set_xlim(-1.1, 1.1)
        axs[i].set_ylim(-1.1, 1.1)
    
    plt.suptitle(f"Curvas de Lissajous (Ratio {ratio_x}:{ratio_y})", fontsize=16)
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

dibujar_lissajous(3, 4)