"""
Monitor de latencia de servidores
Disena un programa que reciba una lista de URLs y mida el tiempo de respuesta de cada una.
Debe:
- Usar time para medir el tiempo antes y despues de la peticion HTTP.
- Repetir varias veces la peticion y calcular la media de tiempo de respuesta.
- Mostrar un pequeno "ranking" de servidores ordenados de menor a mayor latencia media.
"""

# Programa 39: Monitor de latencia de servidores

import requests  # Para peticiones HTTP
import time     # Para medir tiempos
import statistics  # Para calcular media


def medir_latencia(url, repeticiones=3):
    """
    Mide el tiempo de respuesta de una URL varias veces y devuelve la media.
    """
    tiempos = []
    for i in range(repeticiones):
        try:
            inicio = time.time()
            respuesta = requests.head(url, timeout=10)
            fin = time.time()
            latencia = (fin - inicio) * 1000  # Convertir a milisegundos
            tiempos.append(latencia)
        except requests.exceptions.RequestException:
            tiempos.append(float('inf'))
    
    # Filtrar valores infinitos para calcular la media
    tiempos_validos = [t for t in tiempos if t != float('inf')]
    
    if not tiempos_validos:
        return float('inf')
    
    return statistics.mean(tiempos_validos)


def main():
    """
    Funcion principal del programa.
    """
    print("Introduce URLs (una por linea, vacio para terminar):")
    urls = []
    while True:
        url = input().strip()
        if url == "":
            break
        if url.startswith("http"):
            urls.append(url)
    
    if not urls:
        print("No se han introducido URLs.")
        return
    
    print("\nMidiendo latencia (3 repeticiones por URL)...")
    resultados = []
    
    for url in urls:
        latencia_media = medir_latencia(url)
        resultados.append((url, latencia_media))
        estado = "OK" if latencia_media != float('inf') else "FALLA"
        tiempo_txt = f"{latencia_media:.2f} ms" if latencia_media != float('inf') else "SIN RESPUESTA"
        print(f"{url}: {estado} ({tiempo_txt})")
    
    # Ranking: separar servidores que responden de los que no
    print("\n--- RANKING DE LATENCIA ---")
    
    # Filtrar solo los que respondieron para el ranking
    ranking_validos = [(url, lat) for url, lat in resultados if lat != float('inf')]
    ranking_fallidos = [(url, lat) for url, lat in resultados if lat == float('inf')]
    
    # Ordenar por latencia ascendente (menor latencia = mejor)
    ranking_ordenado = sorted(ranking_validos, key=lambda x: x[1])
    
    # Mostrar ranking de servidores que respondieron
    for posicion, (url, latencia) in enumerate(ranking_ordenado, 1):
        print(f"{posicion}. {url}: {latencia:.2f} ms")
    
    # Mostrar servidores que fallaron al final
    if ranking_fallidos:
        print("\n--- SERVIDORES SIN RESPUESTA ---")
        for url, _ in ranking_fallidos:
            print(f"  - {url}: SIN RESPUESTA")


if __name__ == "__main__":
    main()
