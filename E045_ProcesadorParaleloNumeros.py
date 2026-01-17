"""
Procesador paralelo de números con multiprocessing
Crea un programa que divida una lista de 1.000.000 números aleatorios entre 4 procesos paralelos.
Cada proceso debe:
- Calcular la suma parcial de su sublista.
- Usar multiprocessing.Queue para enviar su resultado al proceso principal.
- Mostrar el tiempo total y compararlo con la versión secuencial.
"""

# Programa 45: Procesamiento paralelo con multiprocessing

import multiprocessing
import time
import random


def calcular_suma_parcial(sub_lista):
    """
    Función que calcula la suma de una sublista.
    Se ejecuta en proceso separado.
    """
    return sum(sub_lista)


def version_secuencial(datos):
    """
    Versión secuencial para comparar tiempos.
    """
    inicio = time.time()
    total = sum(datos)
    fin = time.time()
    return total, fin - inicio


def version_paralela(datos, num_procesos):
    """
    Versión paralela usando multiprocessing.
    """
    tamano_sub = len(datos) // num_procesos
    sub_listas = [datos[i:i+tamano_sub] for i in range(0, len(datos), tamano_sub)]
    
    inicio = time.time()
    
    with multiprocessing.Pool(processes=num_procesos) as pool:
        resultados = pool.map(calcular_suma_parcial, sub_listas)
    
    total = sum(resultados)
    fin = time.time()
    
    return total, fin - inicio


def main():
    """
    Función principal que compara secuencial vs paralelo.
    """
    # Generar datos grandes
    tamano = 1_000_000
    datos = [random.randint(1, 100) for _ in range(tamano)]
    
    print(f"Datos generados: {tamano} números")
    
    # Secuencial
    total_sec, tiempo_sec = version_secuencial(datos)
    print(f"Secuencial: {total_sec} en {tiempo_sec:.3f}s")
    
    # Paralelo (4 procesos)
    total_par, tiempo_par = version_paralela(datos, 4)
    print(f"Paralelo (4): {total_par} en {tiempo_par:.3f}s")
    
    aceleracion = tiempo_sec / tiempo_par
    print(f"Aceleración: {aceleracion:.2f}x")


if __name__ == "__main__":
    multiprocessing.set_start_method('spawn')  # Para compatibilidad
    main()
