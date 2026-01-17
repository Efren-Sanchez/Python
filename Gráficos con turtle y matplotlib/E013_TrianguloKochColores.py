'''
Triángulo de Koch con Colores
Implementa con turtle la curva de Koch pero colorea cada nivel recursivo diferente (nivel 0: negro, 1: rojo, 2: azul, etc.). Dibuja el copo completo rotando 60° entre lados y usa pencolor en la función recursiva.
​'''

# Ejercicio 13: Triángulo de Koch con Colores con turtle

import turtle
import math

def koch_color(t, orden, longitud, nivel_actual):
    """
    Curva de Koch con color dinámico por profundidad.
    """
    colores = ["black", "red", "blue", "green", "orange", "purple"]
    # Seleccionar color según el nivel de recursión
    t.pencolor(colores[nivel_actual % len(colores)])
    
    if orden == 0:
        t.forward(longitud)
    else:
        # La longitud se divide entre 3 en cada nivel
        nueva_longitud = longitud / 3
        
        koch_color(t, orden - 1, nueva_longitud, nivel_actual + 1)
        t.left(60)
        koch_color(t, orden - 1, nueva_longitud, nivel_actual + 1)
        t.right(120)
        koch_color(t, orden - 1, nueva_longitud, nivel_actual + 1)
        t.left(60)
        koch_color(t, orden - 1, nueva_longitud, nivel_actual + 1)

def dibujar_copo(orden, longitud):
    ventana = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)
    t.pensize(2)
    
    # Centrar el dibujo correctamente
    altura = longitud * math.sqrt(3) / 2
    t.penup()
    t.goto(-longitud / 2, -altura / 3)
    t.pendown()
    
    # El copo de nieve (triangular) requiere 3 lados de 120 grados
    for _ in range(3):
        koch_color(t, orden, longitud, 0)
        t.right(120)
    
    ventana.exitonclick()

dibujar_copo(4, 300)
