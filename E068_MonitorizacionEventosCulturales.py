"""
Crawler multi-sitio para eventos culturales con export iCal.
pip install requests beautifulsoup4 icalendar
"""

# Programa 68: Monitorizador de eventos culturales

import requests
from bs4 import BeautifulSoup
from icalendar import Calendar, Event
from datetime import datetime, timedelta
from urllib.parse import urljoin
import heapq
import time

SITIOS_EVENTOS = [
    'https://madridcultura.es/agenda',  # Adaptar
    'https://www.barcelona.cat/es/que-pasa-barcelona'
]

def extraer_evento(soup, url_base, ciudad):
    """Extrae eventos de una página."""
    eventos = []
    items = soup.find_all('div', class_='evento-item')  # Selector genérico
    for item in items:
        titulo = item.find('h3').get_text(strip=True) if item.find('h3') else ''
        fecha_str = item.find('span', class_='fecha').get_text() if item.find('span', class_='fecha') else ''
        lugar = item.find('.lugar').get_text(strip=True) if item.find('.lugar') else 'TBD'
        precio = item.find('.precio').get_text(strip=True) if item.find('.precio') else 'Gratis'
        
        if ciudad.lower() in titulo.lower() + lugar.lower():
            try:
                fecha_evento = datetime.strptime(fecha_str, '%d/%m/%Y')  # Adaptar formato
                eventos.append((fecha_evento, {
                    'titulo': titulo,
                    'fecha': fecha_evento.isoformat(),
                    'lugar': lugar,
                    'precio': precio,
                    'url': urljoin(url_base, item.find('a')['href'])
                }))
            except ValueError:
                pass
    return eventos

def reintento_request(url, max_reintentos=3):
    """Request con reintentos."""
    for intento in range(max_reintentos):
        try:
            headers = {'User-Agent': f'DAM-Crawler v{intento+1}'}
            resp = requests.get(url, headers=headers, timeout=10)
            resp.raise_for_status()
            return resp
        except requests.RequestException as e:
            print(f"Reintento {intento+1}: {e}")
            time.sleep(2 ** intento)
    return None

def exportar_ical(eventos, archivo_salida):
    """Genera archivo .ics."""
    cal = Calendar()
    cal.add('prodid', '-//DAM Crawler//mxm.dk//')
    cal.add('version', '2.0')
    
    for _, evento in eventos:
        ev = Event()
        ev.add('summary', evento['titulo'])
        ev.add('dtstart', datetime.fromisoformat(evento['fecha']))
        ev.add('dtend', datetime.fromisoformat(evento['fecha']) + timedelta(hours=2))
        ev.add('location', evento['lugar'])
        ev.add('description', f"Precio: {evento['precio']} | {evento['url']}")
        cal.add_component(ev)
    
    with open(archivo_salida, 'wb') as f:
        f.write(cal.to_ical())
    print(f"📅 {len(eventos)} eventos en {archivo_salida}")

def main():
    """Crawler principal con cola de prioridades."""
    ciudad = input("Ciudad (ej: Madrid): ").strip()
    cola_eventos = []
    
    for sitio in SITIOS_EVENTOS:
        resp = reintento_request(sitio)
        if resp:
            soup = BeautifulSoup(resp.text, 'html.parser')
            eventos = extraer_evento(soup, sitio, ciudad)
            cola_eventos.extend(eventos)
    
    cola_eventos.sort()  # Ordena por fecha (heapq no necesario para <200)
    eventos_ordenados = cola_eventos[:200]
    
    archivo = f"eventos_{ciudad.lower()}_{datetime.now().strftime('%Y%m%d')}.ics"
    exportar_ical(eventos_ordenados, archivo)

if __name__ == "__main__":
    main()
