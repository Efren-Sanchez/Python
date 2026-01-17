'''
Estrella de David
Dibuja con turtle dos triángulos equiláteros superpuestos rotados 180° formando la estrella de David. Rellena uno en azul y otro en amarillo con contornos negros. Añade animación rotando lentamente toda la figura 360°.
'''

# Ejercicio 9: Estrella de David con turtle

import turtle
import math

def dibujar_triangulo(t, radio, color_relleno):
    """Dibuja un triángulo equilátero dado el radio de su círculo circunscrito."""
    t.color("black", color_relleno)
    t.begin_fill()
    for i in range(3):
        # Calculamos la posición de los vértices usando coordenadas polares
        angulo_rad = math.radians(t.heading() + i * 120)
        x = radio * math.cos(angulo_rad)
        y = radio * math.sin(angulo_rad)
        if i == 0:
            t.penup()
            t.goto(x, y)
            t.pendown()
        else:
            t.goto(x, y)
    # Volver al primer punto para cerrar y rellenar
    angulo_ini = math.radians(t.heading())
    t.goto(radio * math.cos(angulo_ini), radio * math.sin(angulo_ini))
    t.end_fill()

def estrella_david_animada():
    ventana = turtle.Screen()
    ventana.tracer(0)
    t = turtle.Turtle()
    t.hideturtle()
    
    radio = 100 # Distancia del centro a los vértices
    
    for rotacion in range(0, 361, 2):
        t.clear()
        
        # Triángulo 1: Punta hacia arriba (90°)
        t.setheading(90 + rotacion)
        dibujar_triangulo(t, radio, "blue")
        
        # Triángulo 2: Punta hacia abajo (270°)
        t.setheading(270 + rotacion)
        dibujar_triangulo(t, radio, "yellow")
        
        ventana.update()
        turtle.time.sleep(0.01)

    ventana.exitonclick()

estrella_david_animada()