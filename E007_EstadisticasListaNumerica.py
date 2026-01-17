"""
Estadísticas de una lista numérica
Pide una lista de números y calcula:
-Media, mediana y desviación estándar.
Usa la librería statistics y muestra los resultados con 2 decimales.
"""

# Programa 7: Estadísticas de una lista numérica

import statistics  # Módulo estándar para cálculos estadísticos


def leer_numeros():
    """
    Lee una lista de números flotantes introducidos por el usuario
    en una sola línea, separados por espacios.
    """
    texto = input("Introduce números separados por espacios: ")
    partes = texto.split()
    numeros = []

    for parte in partes:
        try:
            numero = float(parte)
            numeros.append(numero)
        except ValueError:
            print(f"El valor '{parte}' no es un número válido. Se ignora.")

    return numeros


def calcular_estadisticas(numeros):
    """
    Calcula media, mediana y desviación estándar de una lista de números.
    Devuelve una tupla (media, mediana, desviacion).
    """
    media = statistics.mean(numeros)
    mediana = statistics.median(numeros)
    # Usamos stdev (desviación estándar muestral)
    desviacion = statistics.stdev(numeros) if len(numeros) > 1 else 0.0
    return media, mediana, desviacion


def main():
    """
    Función principal del programa.
    """
    numeros = leer_numeros()
    if len(numeros) == 0:
        print("No se han introducido números.")
        return

    media, mediana, desviacion = calcular_estadisticas(numeros)

    print(f"Media: {media:.2f}")
    print(f"Mediana: {mediana:.2f}")
    print(f"Desviación estándar: {desviacion:.2f}")


if __name__ == "__main__":
    main()
