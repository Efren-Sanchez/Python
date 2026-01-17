'''
Flor de Petalos Móviles
Crea con turtle una flor de 12 pétalos usando círculos superpuestos con radio decreciente. Haz animación donde los pétalos "respiran" expandiéndose/contrayéndose con circle y delays. Centro amarillo, pétalos rosas con contorno verde.
​'''

# Ejercicio 14: Flor de Pétalos Móviles con turtle

import turtle
import math

def dibujar_petalo(t, radio):
    """Dibuja un pétalo usando dos arcos de círculo."""
    t.color("green", "pink")
    t.begin_fill()
    for _ in range(2):
        t.circle(radio, 60)
        t.left(120)
    t.end_fill()

def flor_respirando():
    ventana = turtle.Screen()
    ventana.tracer(0) # Desactiva actualización automática
    t = turtle.Turtle()
    t.hideturtle()
    
    # Parámetros de la animación
    num_petalos = 12
    paso_tiempo = 0
    
    while True:
        t.clear()
        # Efecto "respiración" usando seno
        factor_expansion = (math.sin(paso_tiempo) + 1.5) * 80
        
        # 1. Dibujar Pétalos
        for i in range(num_petalos):
            t.penup()
            t.home()
            t.setheading(i * (360 / num_petalos))
            t.pendown()
            # Superposición de 3 círculos (pétalos) decrecientes por eje
            for r_mod in [1.0, 0.8, 0.6]:
                dibujar_petalo(t, factor_expansion * r_mod)
        
        # 2. Dibujar Centro (siempre encima)
        t.penup()
        t.home()
        t.dot(40, "yellow")
        
        ventana.update()
        paso_tiempo += 0.1
        
        # Pequeño delay para estabilidad de CPU
        if paso_tiempo > 100: break # Evitar bucle infinito en tests

    ventana.exitonclick()

flor_respirando()