'''
Desarrolla un catálogo de películas persistente usando Tkinter para añadir/eliminar items, guardando datos en un fichero con pickle.
'''

# Ejercicio 7: Catálogo de películas persistente con pickle

import tkinter as tk
from tkinter import messagebox, Listbox, Scrollbar
import pickle
import os

ARCHIVO = "peliculas.pkl"

def cargar_peliculas():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "rb") as f:
            return pickle.load(f)
    return []

def guardar_peliculas(peliculas):
    with open(ARCHIVO, "wb") as f:
        pickle.dump(peliculas, f)

def agregar_pelicula():
    nombre = entrada_nombre.get()
    if nombre:
        peliculas.append(nombre)
        lista_peliculas.delete(0, tk.END)
        for p in peliculas:
            lista_peliculas.insert(tk.END, p)
        entrada_nombre.delete(0, tk.END)
        guardar_peliculas(peliculas)
    else:
        messagebox.showerror("Error", "Introduce un nombre.")

def eliminar_pelicula():
    seleccion = lista_peliculas.curselection()
    if seleccion:
        del peliculas[seleccion[0]]
        lista_peliculas.delete(0, tk.END)
        for p in peliculas:
            lista_peliculas.insert(tk.END, p)
        guardar_peliculas(peliculas)

peliculas = cargar_peliculas()

ventana = tk.Tk()
ventana.title("Catálogo de Películas")
ventana.geometry("400x300")

tk.Label(ventana, text="Nombre Película:").pack(pady=5)
entrada_nombre = tk.Entry(ventana, width=30)
entrada_nombre.pack()

tk.Button(ventana, text="Agregar", command=agregar_pelicula).pack(pady=5)
tk.Button(ventana, text="Eliminar Seleccionada", command=eliminar_pelicula).pack(pady=5)

lista_frame = tk.Frame(ventana)
lista_frame.pack(pady=20, fill=tk.BOTH, expand=True)

scrollbar = Scrollbar(lista_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

lista_peliculas = Listbox(lista_frame, yscrollcommand=scrollbar.set, width=40)
lista_peliculas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=lista_peliculas.yview)

for p in peliculas:
    lista_peliculas.insert(tk.END, p)

ventana.mainloop()
