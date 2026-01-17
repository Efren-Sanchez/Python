'''
Crea una ventana con Tkinter que muestre un botón; al pulsarlo, cambie el color de fondo de la ventana entre rojo, verde y azul.
'''

# Ejercicio 1: Ventana con botón que cambia color de fondo

import tkinter as tk

def cambiar_color():
    colores = ["red", "green", "blue"]
    color_actual = ventana.cget("bg")
    # Encontrar el siguiente color en la lista cíclicamente
    try:
        indice_actual = colores.index(color_actual)
        nuevo_color = colores[(indice_actual + 1) % len(colores)]
    except ValueError:
        # Si el color actual no está en la lista, usar el primero
        nuevo_color = colores[0]
    ventana.configure(bg=nuevo_color)

ventana = tk.Tk()
ventana.title("Cambio de Color")
ventana.geometry("300x200")
ventana.configure(bg="white")

boton_color = tk.Button(ventana, text="Cambiar Color", command=cambiar_color)
boton_color.pack(pady=50)

ventana.mainloop()
