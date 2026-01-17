'''
Implementa un editor de texto simple con un área Text grande, un menú con opciones "Nuevo", "Abrir" y "Guardar" para manejar ficheros .txt.
'''

# Ejercicio 4: Editor de texto simple

import tkinter as tk
from tkinter import filedialog, messagebox

def nuevo_archivo():
    area_texto.delete(1.0, tk.END)

def abrir_archivo():
    ruta = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
    if ruta:
        with open(ruta, "r", encoding="utf-8") as f:
            area_texto.delete(1.0, tk.END)
            area_texto.insert(1.0, f.read())

def guardar_archivo():
    ruta = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])
    if ruta:
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(area_texto.get(1.0, tk.END))
        messagebox.showinfo("Guardado", "Archivo guardado correctamente.")

ventana = tk.Tk()
ventana.title("Editor de Texto Simple")
ventana.geometry("500x400")

menu_barra = tk.Menu(ventana)
ventana.config(menu=menu_barra)

menu_archivo = tk.Menu(menu_barra, tearoff=0)
menu_barra.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Nuevo", command=nuevo_archivo)
menu_archivo.add_command(label="Abrir", command=abrir_archivo)
menu_archivo.add_command(label="Guardar", command=guardar_archivo)

area_texto = tk.Text(ventana, wrap=tk.WORD)
area_texto.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

ventana.mainloop()
