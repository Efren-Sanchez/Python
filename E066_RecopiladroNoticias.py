"""
Crawler básico para extraer titulares de noticias.
Instalación: pip install requests beautifulsoup4 urllib3
Uso: python crawler_noticias.py https://ejemplo.com/noticias
Respeta robots.txt y limita a 50 artículos.
"""

# Programa 66: Recopilador de noticias

import sys
import csv
import time
import urllib.robotparser
from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def verificar_robots_txt(url_base):
    """Comprueba si robots.txt permite crawling."""
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(urljoin(url_base, '/robots.txt'))
    try:
        rp.read()
        return rp.can_fetch('*', url_base)
    except:
        return True  # Si no hay robots.txt, permite

def extraer_titulares(soup, url_base):
    """Extrae titulares h2/h3 con enlaces."""
    titulares = []
    for h in soup.find_all(['h2', 'h3']):
        enlace = h.find('a')
        if enlace:
            titulo = enlace.get_text(strip=True)
            href = enlace.get('href')
            url_completa = urljoin(url_base, href)
            fecha = h.find('time') or datetime.now().strftime('%Y-%m-%d')
            if titulo and url_completa:
                titulares.append({
                    'titulo': titulo[:100],
                    'url': url_completa,
                    'fecha': fecha.get_text(strip=True) if fecha.name else fecha.strftime('%Y-%m-%d')
                })
    return titulares

def guardar_csv(titulares, archivo_salida):
    """Guarda lista en CSV."""
    with open(archivo_salida, 'w', newline='', encoding='utf-8') as csvfile:
        campos = ['titulo', 'url', 'fecha']
        escritor = csv.DictWriter(csvfile, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(titulares)

def main(url_inicio):
    """Función principal del crawler."""
    if not verificar_robots_txt(url_inicio):
        print("❌ Bloqueado por robots.txt")
        return
    
    titulares = []
    try:
        headers = {'User-Agent': 'DAM-Crawler-Estudiante/1.0'}
        respuesta = requests.get(url_inicio, headers=headers, timeout=10)
        respuesta.raise_for_status()
        
        soup = BeautifulSoup(respuesta.text, 'html.parser')
        nuevos_titulares = extraer_titulares(soup, url_inicio)
        titulares.extend(nuevos_titulares[:50 - len(titulares)])
        
        inicio_tiempo = time.time()
        print(f"📊 Extraídos {len(titulares)} titulares en {time.time() - inicio_tiempo:.1f}s")
        
        archivo_salida = f"noticias_{datetime.now().strftime('%Y%m%d_%H%M')}.csv"
        guardar_csv(titulares, archivo_salida)
        print(f"💾 Guardado en {archivo_salida}")
        
    except requests.RequestException as error:
        print(f"Error HTTP: {error}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python crawler_noticias.py <URL>")
        sys.exit(1)
    main(sys.argv[1])
