"""
Estadísticas meteorológicas (librerías)
Usando la librería datetime y random, genera una lista de 30 registros simulando temperaturas diarias de un mes.
Cada elemento será una tupla (fecha, temperatura). Calcula la temperatura media, máxima y mínima, y guarda el resumen en un fichero CSV.
"""

# Programa 10: Estadísticas meteorológicas simuladas

import random      # Para generar temperaturas aleatorias
from datetime import date, timedelta  # Para manejar fechas
import csv         # Para guardar los resultados en CSV


def generar_registros_mensuales(dia_inicial, num_dias, temp_min, temp_max):
    """
    Genera una lista de tuplas (fecha, temperatura) simulando datos diarios.
    - dia_inicial: objeto date con el primer día del mes
    - num_dias: número de días que se van a generar
    - temp_min, temp_max: rango de temperaturas aleatorias
    """
    registros = []

    for i in range(num_dias):
        fecha_actual = dia_inicial + timedelta(days=i)
        temperatura = random.uniform(temp_min, temp_max)
        registros.append((fecha_actual, temperatura))

    return registros


def calcular_estadisticas_temperaturas(registros):
    """
    Recibe una lista de tuplas (fecha, temperatura) y calcula:
    - temperatura media
    - temperatura máxima
    - temperatura mínima
    Devuelve una tupla (media, maxima, minima).
    """
    if not registros:
        return None, None, None

    temperaturas = [t for _, t in registros]
    media = sum(temperaturas) / len(temperaturas)
    maxima = max(temperaturas)
    minima = min(temperaturas)
    return media, maxima, minima


def guardar_resumen_csv(ruta, media, maxima, minima):
    """
    Guarda en un fichero CSV un pequeño resumen de temperaturas.
    El CSV tendrá columnas: concepto, valor
    """
    try:
        with open(ruta, "w", encoding="utf-8", newline="") as f:
            escritor = csv.writer(f)
            escritor.writerow(["concepto", "valor"])
            escritor.writerow(["media", f"{media:.2f}"])
            escritor.writerow(["maxima", f"{maxima:.2f}"])
            escritor.writerow(["minima", f"{minima:.2f}"])
        print(f"Resumen guardado en '{ruta}'.")
    except OSError as e:
        print("Error al escribir el CSV:", e)


def main():
    """
    Función principal del programa.
    """
    # Configuración del mes simulado
    # Por ejemplo: mes de enero de 2025
    ano = 2025
    mes = 1
    num_dias = 30  # Para el ejercicio, usamos 30 días

    # Rango de temperaturas
    temp_min = -5.0
    temp_max = 20.0

    primer_dia = date(ano, mes, 1)

    registros = generar_registros_mensuales(primer_dia, num_dias, temp_min, temp_max)

    # Mostramos los registros generados
    print("Registros generados (fecha - temperatura):")
    for fecha, temperatura in registros:
        print(f"{fecha.isoformat()} - {temperatura:.2f} ºC")

    media, maxima, minima = calcular_estadisticas_temperaturas(registros)

    if media is None:
        print("No se han podido calcular estadísticas.")
        return

    print("\nEstadísticas del mes:")
    print(f"Temperatura media: {media:.2f} ºC")
    print(f"Temperatura máxima: {maxima:.2f} ºC")
    print(f"Temperatura mínima: {minima:.2f} ºC")

    guardar_resumen_csv("resumen_temperaturas.csv", media, maxima, minima)


if __name__ == "__main__":
    main()
