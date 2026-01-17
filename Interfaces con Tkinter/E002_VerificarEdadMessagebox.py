'''
Desarrolla un programa que solicite al usuario su nombre y edad mediante Entry y Entry, 
y muestre un mensaje con messagebox: "¡Hola [nombre]! Eres mayor de edad" si la edad >=18, 
o "¡Eres menor!" en caso contrario.
'''

# Ejercicio 2: Verificador de edad con messagebox

import tkinter as tk
from tkinter import messagebox

def verificar_edad():
    try:
        nombre = entrada_nombre.get()
        edad = int(entrada_edad.get())
        if edad >= 18:
            messagebox.showinfo("Saludo", f"¡Hola {nombre}! Eres mayor de edad.")
        else:
            messagebox.showwarning("Saludo", "¡Eres menor de edad!")
    except ValueError:
        messagebox.showerror("Error", "Introduce una edad válida.")

ventana = tk.Tk()
ventana.title("Verificador de Edad")
ventana.geometry("300x150")

tk.Label(ventana, text="Nombre:").pack(pady=5)
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()

tk.Label(ventana, text="Edad:").pack(pady=5)
entrada_edad = tk.Entry(ventana)
entrada_edad.pack()

boton_verificar = tk.Button(ventana, text="Verificar", command=verificar_edad)
boton_verificar.pack(pady=10)

ventana.mainloop()
