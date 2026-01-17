'''
Curva del Dragón
Desarrolla un script que trace la curva del Dragón (o "Dragon Curve") de orden n usando recursión con turtle. Comienza con una línea recta, aplica giros alternos de 90° (derecha e izquierda) en cada iteración doblando la curva sobre sí misma, y visualiza el resultado para n=10. Experimenta con colores por nivel de recursión.
'''

# Ejercicio 3: Curva del Dragón con Turtle

import turtle

# Paleta de colores para niveles de recursión
COLORES = ["#ff0000", "#ff7f00", "#ffff00", "#00ff00", "#0000ff", "#4b0082", "#8b00ff"]

def curva_dragon(t, orden, direccion):
    """
    t: objeto turtle
    orden: nivel de recursión
    direccion: 1 (izq) o -1 (der) para el giro central
    """
    if orden == 0:
        t.forward(6)
    else:
        # Cambiar color según el nivel actual
        t.pencolor(COLORES[orden % len(COLORES)])
        
        # Lógica de plegado: la primera parte siempre usa dirección positiva (1)
        curva_dragon(t, orden - 1, 1)
        t.left(90 * direccion)
        # La segunda parte siempre usa dirección negativa (-1)
        curva_dragon(t, orden - 1, -1)

def dibujar_dragon(orden):
    ventana = turtle.Screen()
    ventana.setup(800, 800)
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    
    # Centrado manual para orden 10
    t.penup()
    t.goto(100, -50)
    t.pendown()
    
    curva_dragon(t, orden, 1)
    ventana.exitonclick()

dibujar_dragon(10)