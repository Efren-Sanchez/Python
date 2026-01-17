'''
Diseña una interfaz que pida un número entero N en un Entry y calcule su factorial con un Button, mostrando el resultado en un Label.
'''

# Ejercicio 3: Calculadora de factorial

import tkinter as tk
from math import factorial

def calcular_factorial():
    try:
        n = int(entrada_numero.get())
        resultado = factorial(n)
        etiqueta_resultado.config(text=f"Factorial: {resultado}")
    except ValueError:
        etiqueta_resultado.config(text="Número inválido")

ventana = tk.Tk()
ventana.title("Calculadora Factorial")
ventana.geometry("250x150")

tk.Label(ventana, text="Número (N):").pack(pady=10)
entrada_numero = tk.Entry(ventana)
entrada_numero.pack()

boton_calcular = tk.Button(ventana, text="Calcular", command=calcular_factorial)
boton_calcular.pack(pady=10)

etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack()

ventana.mainloop()
