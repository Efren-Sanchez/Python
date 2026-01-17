'''
Crea una aplicación con dos LabelFrame: el primero con dos Label, dos Entry (para nombre y contraseña) 
y un Button de login; el segundo con tres botones (Aceptar, Cancelar, Salir).
'''

# Ejercicio 5: Aplicación con LabelFrame (login y botones)

import tkinter as tk
from tkinter import messagebox

def procesar_login():
    usuario = entrada_usuario.get()
    contrasena = entrada_contrasena.get()
    if usuario and contrasena:
        messagebox.showinfo("Login", f"Bienvenido, {usuario}")
    else:
        messagebox.showerror("Error", "Rellena todos los campos.")

def aceptar():
    messagebox.showinfo("Aceptar", "Operación aceptada.")

def cancelar():
    messagebox.showwarning("Cancelar", "Operación cancelada.")

def salir():
    ventana.quit()

ventana = tk.Tk()
ventana.title("Formulario con Marcos")
ventana.geometry("300x250")

marco_login = tk.LabelFrame(ventana, text="Login")
marco_login.pack(pady=10, padx=20, fill=tk.X)

tk.Label(marco_login, text="Usuario:").pack(pady=5)
entrada_usuario = tk.Entry(marco_login)
entrada_usuario.pack()

tk.Label(marco_login, text="Contraseña:").pack(pady=5)
entrada_contrasena = tk.Entry(marco_login, show="*")
entrada_contrasena.pack()

tk.Button(marco_login, text="Login", command=procesar_login).pack(pady=10)

marco_botones = tk.LabelFrame(ventana, text="Acciones")
marco_botones.pack(pady=10, padx=20, fill=tk.X)

tk.Button(marco_botones, text="Aceptar", command=aceptar).pack(side=tk.LEFT, padx=5)
tk.Button(marco_botones, text="Cancelar", command=cancelar).pack(side=tk.LEFT, padx=5)
tk.Button(marco_botones, text="Salir", command=salir).pack(side=tk.LEFT, padx=5)

ventana.mainloop()
