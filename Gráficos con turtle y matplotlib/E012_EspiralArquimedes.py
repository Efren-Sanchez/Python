'''
Espiral de Arquímedes
Con turtle, dibuja una espiral de Arquímedes r=aθ donde θ va de 0 a 10π. Incrementa el radio linealmente con el ángulo. Usa circle con radio variable y colorea por sectores (rojo,verde,azul repitiendo cada 120°).
​'''

# Ejercicio 12: Espiral de Arquímedes con turtle

import turtle
import math

def espiral_arquimedes():
    ventana = turtle.Screen()
    ventana.title("Espiral de Arquímedes")
    t = turtle.Turtle()
    t.speed(0)
    t.pensize(2)
    
    a = 5  # Factor de crecimiento (píxeles por radián)
    t.penup()
    theta = 0
    paso = 0.05 # Incremento de theta en cada paso
    colores = ["red", "green", "blue"]
    
    while theta < 10 * math.pi:
        # Ecuación de Arquímedes: r = a * theta
        r = a * theta
        
        # Selección de color por sectores de 120° (2*pi/3 radianes)
        sector = int(theta / (2 * math.pi / 3))
        t.color(colores[sector % 3])
        
        # Convertir coordenadas polares (r, theta) a cartesianas (x, y)
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        
        t.goto(x, y)
        theta += paso
    
    ventana.exitonclick()

espiral_arquimedes()