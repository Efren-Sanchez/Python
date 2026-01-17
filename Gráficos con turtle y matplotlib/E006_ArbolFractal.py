'''
Árbol Fractal
Crea un programa con turtle que dibuje un árbol fractal recursivo. Comienza con un tronco vertical y en cada rama aplica un ángulo aleatorio entre 25°-35° con longitud reducida al 70%. Añade hojas verdes en las ramas finales usando círculos pequeños.
'''

# Ejercicio 6: Árbol Fractal con turtle

import turtle
import random

def rama(tortuga, longitud, angulo_min, angulo_max, nivel):
    """
    Dibuja una rama recursiva del árbol.
    tortuga: objeto turtle
    longitud: longitud actual de la rama
    angulo_min/max: rango de ángulo aleatorio
    nivel: profundidad máxima
    """
    if longitud < 5 or nivel == 0:
        # Hoja: círculo verde pequeño
        tortuga.color("green")
        tortuga.circle(2)
        return
    
    tortuga.forward(longitud)
    angulo = random.uniform(angulo_min, angulo_max)
    tortuga.left(angulo)
    rama(tortuga, longitud * 0.7, angulo_min, angulo_max, nivel - 1)
    tortuga.right(angulo * 2)
    rama(tortuga, longitud * 0.7, angulo_min, angulo_max, nivel - 1)
    tortuga.left(angulo)
    tortuga.backward(longitud)

def dibujar_arbol():
    """Programa principal del árbol fractal."""
    ventana = turtle.Screen()
    ventana.title("Árbol Fractal")
    ventana.bgcolor("black")
    tortuga = turtle.Turtle()
    tortuga.speed(0)
    tortuga.color("brown")
    tortuga.left(90)
    tortuga.backward(200)  # Posicionar
    
    rama(tortuga, 100, 25, 35, 8)
    ventana.exitonclick()

# Ejecutar
dibujar_arbol()
