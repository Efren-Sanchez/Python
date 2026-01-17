'''
Curva de Koch
Implementa un programa en Python que dibuje la curva de Koch de orden n (por ejemplo, n=4) usando el módulo turtle. Divide cada segmento en tres partes iguales, sustituye el segmento central por los dos lados de un triángulo equilátero (rotando 60°), y repite recursivamente. Muestra el copo de nieve completo uniendo cuatro curvas.
'''

# Ejercicio 1: Curva de Koch (Copo de nieve) con Turtle

import turtle

def curva_koch(t, orden, longitud):
    if orden == 0:
        t.forward(longitud)
    else:
        ln = longitud / 3
        curva_koch(t, orden - 1, ln)
        t.left(60)
        curva_koch(t, orden - 1, ln)
        t.right(120)
        curva_koch(t, orden - 1, ln)
        t.left(60)
        curva_koch(t, orden - 1, ln)

def copo_nieve(orden, longitud):
    ventana = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)
    
    # Centrado: Calcular posición inicial
    # Se desplaza media longitud a la izquierda y un tercio de la altura hacia arriba
    altura_triangulo = (3**0.5 / 2) * longitud
    t.penup()
    t.goto(-longitud / 2, altura_triangulo / 3)
    t.pendown()
    
    # Error corregido: range(3) para cerrar el triángulo equilátero
    for _ in range(3):
        curva_koch(t, orden, longitud)
        t.right(120)
    
    ventana.exitonclick()

copo_nieve(4, 300)