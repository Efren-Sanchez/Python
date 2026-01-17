'''
Espiral Logarítmica
Implementa con turtle una espiral logarítmica (espiral de oro) donde cada segmento crece un factor φ=(1+√5)/2 respecto al anterior. Dibuja 100 vueltas alternando colores azul/rojo y grosor creciente. Marca el centro con un círculo.
'''

# Ejercicio 7: Espiral Logarítmica con turtle

import turtle
import math

def espiral_logaritmica():
    ventana = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)
    
    # Constantes
    phi = (1 + math.sqrt(5)) / 2
    # El factor de crecimiento 'b' para una espiral logarítmica de oro:
    # radio = a * e^(b * theta). Para la de oro, b = ln(phi) / (pi/2)
    b = math.log(phi) / (math.pi / 2)
    
    # Marcar el centro
    t.dot(10, "yellow")
    
    t.penup()
    # Empezamos con un radio pequeño inicial
    a = 2 
    colores = ["blue", "red"]
    
    # Para dibujar 100 segmentos (no 100 vueltas, que sería infinito en pantalla)
    for i in range(100):
        t.color(colores[i % 2])
        t.pensize(i / 10 + 1)
        
        # theta en radianes para el cálculo
        theta_rad = math.radians(i * 10) 
        radio = a * math.exp(b * theta_rad)
        
        # Calcular posición (x, y)
        x = radio * math.cos(theta_rad)
        y = radio * math.sin(theta_rad)
        
        t.goto(x, y)
        t.pendown()
        
    ventana.exitonclick()

espiral_logaritmica()