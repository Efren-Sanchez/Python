'''
Crea un gestor de menú de restaurante con Listbox para categorías y platos, conectado a una base de datos SQLite para listar y añadir elementos.
'''

# Ejercicio 8: Gestor de menú restaurante con SQLite

import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# Crear base de datos
conn = sqlite3.connect("restaurante.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS menu (id INTEGER PRIMARY KEY, categoria TEXT, plato TEXT)")

def agregar_plato():
    categoria = combo_categoria.get()
    plato = entrada_plato.get()
    if categoria and plato:
        cursor.execute("INSERT INTO menu (categoria, plato) VALUES (?, ?)", (categoria, plato))
        conn.commit()
        actualizar_lista()
        entrada_plato.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Rellena todos los campos.")

def actualizar_lista():
    for item in tree.get_children():
        tree.delete(item)
    cursor.execute("SELECT categoria, plato FROM menu")
    for cat, plato in cursor.fetchall():
        tree.insert("", tk.END, values=(cat, plato))

def eliminar_plato():
    seleccion = tree.selection()
    if seleccion:
        item = tree.item(seleccion)
        # Eliminar por categoría y plato (pk logic simplified for demo)
        cursor.execute("DELETE FROM menu WHERE categoria=? AND plato=?", item["values"])
        conn.commit()
        actualizar_lista()

ventana = tk.Tk()
ventana.title("Gestor de Menú Restaurante")
ventana.geometry("500x400")

tk.Label(ventana, text="Categoría:").pack(pady=5)
combo_categoria = ttk.Combobox(ventana, values=["Entrantes", "Platos Principales", "Postres", "Bebidas"])
combo_categoria.pack()

tk.Label(ventana, text="Plato:").pack(pady=5)
entrada_plato = tk.Entry(ventana, width=40)
entrada_plato.pack()

tk.Button(ventana, text="Agregar Plato", command=agregar_plato).pack(pady=10)
tk.Button(ventana, text="Eliminar Seleccionado", command=eliminar_plato).pack()

# Treeview para lista
columnas = ("Categoría", "Plato")
tree = ttk.Treeview(ventana, columns=columnas, show="headings")
tree.heading("Categoría", text="Categoría")
tree.heading("Plato", text="Plato")
tree.pack(pady=20, fill=tk.BOTH, expand=True)

actualizar_lista()

ventana.mainloop()
conn.close()
