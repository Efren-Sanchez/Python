'''
Curva de Hilbert
Implementa la curva de Hilbert de orden n (por ejemplo, n=5) con una función recursiva en turtle. Esta curva rellena un cuadrado dividiendo recursivamente en cuatro subcuadrados, girando 90° y conectando con pasos hacia adelante. Asegúrate de que sea continua y sin autointersecciones, ideal para mostrar espacio-filling.
'''

# Ejercicio 5: Curva de Hilbert con Turtle

import turtle

def hilbert(t, orden, angulo, longitud):
    if orden == 0:
        return

    # Giro inicial para orientar el subcuadrado
    t.left(angulo)
    hilbert(t, orden - 1, -angulo, longitud)
    
    t.forward(longitud)
    t.right(angulo)
    hilbert(t, orden - 1, angulo, longitud)
    
    t.forward(longitud)
    hilbert(t, orden - 1, angulo, longitud)
    
    t.right(angulo)
    t.forward(longitud)
    hilbert(t, orden - 1, -angulo, longitud)
    t.left(angulo)

def dibujar_hilbert(orden, tamano_total):
    ventana = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    
    # Cálculo de la longitud de cada segmento
    # Un cuadrado de orden n tiene (2^n - 1) segmentos de lado
    longitud = tamano_total / (2**orden - 1)
    
    # Centrado inicial
    t.penup()
    t.goto(-tamano_total/2, -tamano_total/2)
    t.pendown()
    
    hilbert(t, orden, 90, longitud)
    
    ventana.exitonclick()

# Ejecutar orden 5
dibujar_hilbert(5, 400)