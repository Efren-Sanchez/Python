'''
Helecho de Barnsley
Escribe un programa que simule el helecho de Barnsley aplicando cuatro transformaciones afines probabilísticas (probabilidades: 0.85, 0.07, 0.07, 0.01) a un punto inicial (0,0) durante 50,000 iteraciones con matplotlib. Usa random para seleccionar cada regla y plotea los puntos resultantes en verde para simular hojas.
'''

# Ejercicio 4: Helecho de Barnsley (con turtle aproximado) con Turtle

import turtle
import random

def transformar_punto(x, y):
    r = random.random()
    if r < 0.01:
        return 0, 0.16 * y, "brown"
    elif r < 0.86:
        return 0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6, "darkgreen"
    elif r < 0.93:
        return 0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6, "green"
    else:
        return -0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44, "lightgreen"

def dibujar_helecho(iteraciones):
    ventana = turtle.Screen()
    ventana.tracer(0)  # Desactiva la animación (crítico para rendimiento)
    
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    
    x, y = 0.0, 0.0
    escala = 45 
    desplazamiento_y = -200

    for i in range(iteraciones):
        x, y, color = transformar_punto(x, y)
        t.goto(x * escala, y * escala + desplazamiento_y)
        t.dot(2, color)
        
        # Actualizar pantalla cada 1000 puntos para ver progreso
        if i % 1000 == 0:
            ventana.update()
            
    ventana.update() # Refresco final
    ventana.exitonclick()

dibujar_helecho(50000)