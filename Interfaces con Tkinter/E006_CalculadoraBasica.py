'''
Construye una calculadora gráfica básica con botones numéricos (0-9), operaciones (+, -, *, /) y un área de texto para mostrar resultados.
'''

# Ejercicio 6: Calculadora gráfica básica

import tkinter as tk

class Calculadora:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Calculadora")
        self.ventana.geometry("300x400")
        
        self.ecuacion = ""
        self.resultado = tk.StringVar(value="0")
        
        # Pantalla
        display = tk.Entry(ventana, textvariable=self.resultado, font=("Arial", 24), 
                          justify="right", state="readonly", bd=10, bg="#eee")
        display.pack(fill=tk.BOTH, padx=10, pady=20)
        
        # Contenedor de botones
        marco = tk.Frame(ventana)
        marco.pack(expand=True, fill=tk.BOTH)

        botones = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        fila, col = 0, 0
        for boton in botones:
            # Uso de default value en lambda para capturar el valor actual de la iteración
            comando = lambda x=boton: self.al_pulsar(x)
            tk.Button(marco, text=boton, width=5, height=2, font=("Arial", 14),
                      command=comando).grid(row=fila, column=col, sticky="nsew", padx=2, pady=2)
            col += 1
            if col > 3:
                col = 0
                fila += 1
        
        # Configurar peso de columnas/filas para que sean elásticas
        for i in range(4):
            marco.grid_columnconfigure(i, weight=1)
            marco.grid_rowconfigure(i, weight=1)

    def al_pulsar(self, tecla):
        if tecla == "=":
            self.resolver()
        elif tecla == "C":
            self.limpiar()
        else:
            if self.ecuacion == "0": self.ecuacion = ""
            self.ecuacion += str(tecla)
            self.resultado.set(self.ecuacion)

    def limpiar(self):
        self.ecuacion = ""
        self.resultado.set("0")

    def resolver(self):
        try:
            # eval() es aceptable en este contexto educativo controlado
            total = str(eval(self.ecuacion))
            self.resultado.set(total)
            self.ecuacion = total
        except Exception:
            self.resultado.set("Error")
            self.ecuacion = ""

if __name__ == "__main__":
    ventana = tk.Tk()
    app = Calculadora(ventana)
    ventana.mainloop()