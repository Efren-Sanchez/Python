"""
Crawler de ofertas e-commerce con paginación y pausas.
Ejemplo sitios: amazon.es/ofertas (adaptar selectores).
pip install requests beautifulsoup4
"""

# Programa 67: Rastreador de ofertas e-commerce

import json
import time
import random
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from urllib.parse import urljoin

def pausa_aleatoria():
    """Pausa 2-5 segundos entre requests."""
    tiempo = random.uniform(2, 5)
    print(f"⏳ Pausa {tiempo:.1f}s...")
    time.sleep(tiempo)

def extraer_ofertas(soup, url_base):
    """Extrae datos de productos de una página."""
    ofertas = []
    productos = soup.find_all('div', class_='product-link')  # Adaptar selector
    for prod in productos:
        nombre_elem = prod.find('h2') or prod.find('span', class_='product-title')
        precio_elem = prod.find('span', class_='price-current')
        rebaja_elem = prod.find('span', class_='price-discount')
        
        nombre = nombre_elem.get_text(strip=True) if nombre_elem else 'N/A'
        precio = float(precio_elem.get_text().replace('€', '').replace(',', '.') if precio_elem else 0)
        rebaja = float(rebaja_elem.get_text().replace('%', '')) if rebaja_elem else 0
        
        if rebaja > 50:
            print(f"🔥 Oferta >50%: {nombre} ({rebaja}%)")
        
        ofertas.append({
            'nombre': nombre[:80],
            'precio': precio,
            'rebaja_pct': rebaja,
            'url': urljoin(url_base, prod.find('a')['href'] if prod.find('a') else ''),
            'timestamp': datetime.now().isoformat()
        })
    return ofertas

def crawler_paginas(url_base, max_paginas=10):
    """Navega paginación."""
    todas_ofertas = []
    for pagina in range(1, max_paginas + 1):
        url_pagina = f"{url_base}?page={pagina}"
        print(f"📄 Procesando página {pagina}")
        
        headers = {'User-Agent': 'Mozilla/5.0 (DAM Student Crawler)'}
        resp = requests.get(url_pagina, headers=headers, timeout=10)
        if resp.status_code != 200:
            break
        
        soup = BeautifulSoup(resp.text, 'html.parser')
        ofertas = extraer_ofertas(soup, url_base)
        todas_ofertas.extend(ofertas)
        
        pausa_aleatoria()
    
    return todas_ofertas

def main():
    """Ejecuta crawler."""
    url_base = input("URL base de ofertas: ").strip()
    ofertas = crawler_paginas(url_base)
    
    archivo = f"ofertas_{datetime.now().strftime('%Y%m%d')}.json"
    with open(archivo, 'w', encoding='utf-8') as f:
        json.dump(ofertas, f, indent=2, ensure_ascii=False)
    print(f"💾 {len(ofertas)} ofertas en {archivo}")

if __name__ == "__main__":
    main()
