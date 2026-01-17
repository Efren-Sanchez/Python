'''
Implementa un formulario de login con validación: Entry para usuario/contraseña, Button que verifique credenciales y cambie a una ventana principal si son correctas.
'''

# Ejercicio 9: Formulario de login con validación

import tkinter as tk
from tkinter import messagebox

class AppLogin:
    def __init__(self):
        self.ventana_login = tk.Tk()
        self.ventana_login.title("Login")
        self.ventana_login.geometry("300x200")
        self.credenciales_correctas = False
        self.crear_ventana_login()
    
    def crear_ventana_login(self):
        tk.Label(self.ventana_login, text="Usuario:").pack(pady=10)
        self.entrada_usuario = tk.Entry(self.ventana_login)
        self.entrada_usuario.pack()
        
        tk.Label(self.ventana_login, text="Contraseña:").pack(pady=10)
        self.entrada_contrasena = tk.Entry(self.ventana_login, show="*")
        self.entrada_contrasena.pack()
        
        tk.Button(self.ventana_login, text="Iniciar Sesión", command=self.verificar_login).pack(pady=20)
    
    def verificar_login(self):
        usuario = self.entrada_usuario.get()
        contrasena = self.entrada_contrasena.get()
        if usuario == "admin" and contrasena == "1234":  # Credenciales fijas para demo
            self.credenciales_correctas = True
            self.ventana_login.destroy()
            self.crear_ventana_principal()
        else:
            messagebox.showerror("Error", "Credenciales incorrectas.")
    
    def crear_ventana_principal(self):
        self.ventana_principal = tk.Toplevel(self.ventana_login)
        self.ventana_principal.title("Ventana Principal")
        self.ventana_principal.geometry("400x300")
        tk.Label(self.ventana_principal, text="¡Bienvenido! Acceso concedido.", font=("Arial", 16)).pack(pady=50)
        tk.Button(self.ventana_principal, text="Salir", command=self.ventana_login.quit).pack()

app = AppLogin()
app.ventana_login.mainloop()
