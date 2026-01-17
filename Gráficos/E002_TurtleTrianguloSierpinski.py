'''
Triángulo de Sierpinski
Crea una función recursiva que genere el triángulo de Sierpinski de nivel n (por ejemplo, n=6) con turtle o matplotlib. Parte de un triángulo equilátero inicial y en cada iteración, divide cada lado en dos y conecta los puntos medios, eliminando el triángulo central. Colorea las áreas para resaltar la estructura fractal.
'''

# Ejercicio 2: Triángulo de Sierpinski con Turtle

import turtle
import math

def triangulo_sierpinski(t, x, y, lado, nivel):
    """
    Dibuja recursivamente el triángulo de Sierpinski usando coordenadas absolutas.
    t: objeto turtle
    x, y: posición inicial del vértice inferior izquierdo
    lado: longitud del lado
    nivel: nivel de recursión
    """
    if nivel == 0:
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.setheading(0)  # Apunta hacia la derecha
        for _ in range(3):
            t.forward(lado)
            t.left(120)
    else:
        lado_menor = lado / 2
        h_menor = lado_menor * math.sqrt(3) / 2
        
        # Sub-triángulo inferior izquierdo
        triangulo_sierpinski(t, x, y, lado_menor, nivel - 1)
        
        # Sub-triángulo inferior derecho
        triangulo_sierpinski(t, x + lado_menor, y, lado_menor, nivel - 1)
        
        # Sub-triángulo superior
        triangulo_sierpinski(t, x + lado_menor / 2, y + h_menor, lado_menor, nivel - 1)

def dibujar_sierpinski(nivel, lado):
    """Programa principal para el triángulo de Sierpinski."""
    ventana = turtle.Screen()
    ventana.title("Triángulo de Sierpinski corregido")
    t = turtle.Turtle()
    t.speed(0)
    t.color("red")
    t.pensize(1)
    
    # Posición inicial para vértice inferior izquierdo
    x_inicial = -lado / 2
    y_inicial = -lado / (2 * math.sqrt(3))
    
    triangulo_sierpinski(t, x_inicial, y_inicial, lado, nivel)
    ventana.exitonclick()

# Ejecutar con nivel 6 y lado 400
dibujar_sierpinski(6, 400)
