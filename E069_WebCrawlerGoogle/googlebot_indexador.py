"""
Mini-GoogleBot: Indexador web estilo Google.
Instalación: pip install requests beautifulsoup4 mysql-connector-python urllib3 celery whoosh flask
Uso: python googlebot_indexador.py --semilla https://es.wikipedia.org/wiki/Python --limite 100
"""

import argparse
import time
import threading
import queue
from urllib.parse import urljoin, urlparse, urldefrag
from urllib.robotparser import RobotFileParser
import requests
from bs4 import BeautifulSoup
import mysql.connector
from mysql.connector import Error
from collections import Counter
import re
import json
import logging

# Configuración logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Configuración conexión MySQL
CONFIG_BD = {
    'host': 'localhost',
    'database': 'googlebot',
    'user': 'root',
    'password': 'root'
}

class MiniGoogleBot:
    def __init__(self, semilla_url, limite_paginas=1000, profundidad_max=4):
        self.semilla_url = semilla_url
        self.limite_paginas = limite_paginas
        self.profundidad_max = profundidad_max
        self.dominio_base = '{uri.netloc}'.format(uri=urlparse(semilla_url))
        self.colas_paginas = queue.Queue()
        self.paginas_visitadas = set()
        self.paginas_indexadas = 0
        self.contador_peticiones = 0  # Contador para rotación de User-Agent
        self.conexion_bd = self._conectar_bd()
        self.robot_parser = RobotFileParser()
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (DAM-GoogleBot/1.0)',
            'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
        ]
        self._robots_cache = {}
        self.bloqueo = threading.Lock()  # Para acceso seguro a variables compartidas
        
    def _conectar_bd(self):
        """Establece conexión persistente a MySQL."""
        try:
            conexion = mysql.connector.connect(**CONFIG_BD)
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM paginas")
            conexion.commit()
            logger.info("Base de datos preparada")
            return conexion
        except Error as e:
            logger.error(f"Error BD: {e}")
            return None
    
    def verificar_robots(self, url):
        """Verifica permisos en robots.txt."""
        parsed_url = urlparse(url)
        rp_url = f"https://{parsed_url.netloc}/robots.txt"
        
        if rp_url not in self._robots_cache:
            rp = RobotFileParser()
            try:
                rp.set_url(rp_url)
                rp.read()
                self._robots_cache[rp_url] = rp
            except Exception:  # ✅ Excepción específica
                self._robots_cache[rp_url] = None
        
        rp = self._robots_cache[rp_url]
        return rp.can_fetch('*', url) if rp else True
    
    def limpiar_texto(self, texto):
        """Extrae texto limpio eliminando HTML, scripts y ruido."""
        texto = re.sub(r'<script.*?</script>', '', texto, flags=re.DOTALL | re.IGNORECASE)
        texto = re.sub(r'<style.*?</style>', '', texto, flags=re.DOTALL | re.IGNORECASE)
        soup = BeautifulSoup(texto, 'html.parser')
        texto_limpio = soup.get_text()
        texto_limpio = re.sub(r'[^\w\s.,!?-]', ' ', texto_limpio.lower())
        palabras = re.findall(r'\b[a-záéíóúüñ]{3,}\b', texto_limpio)
        return ' '.join(palabras[:5000]), palabras
    
    def extraer_palabras_clave(self, palabras):
        """Calcula TOP 50 palabras más frecuentes."""
        contador = Counter(palabras)
        return [{'palabra': p, 'frecuencia': f} for p, f in contador.most_common(50)]
    
    def extraer_enlaces(self, soup, url_base):
        """Extrae enlaces internos del mismo dominio."""
        enlaces = []
        for a in soup.find_all('a', href=True):
            href = a['href']
            url_completa = urldefrag(urljoin(url_base, href))[0]
            if urlparse(url_completa).netloc == self.dominio_base:
                enlaces.append(url_completa)
        return list(set(enlaces))
    
    def indexar_pagina(self, url, profundidad):
        """Indexa una página individual."""
        with self.bloqueo:  # ✅ Protección con lock
            if self.paginas_indexadas >= self.limite_paginas:
                return False
            
            if url in self.paginas_visitadas:
                return True
            
            self.paginas_visitadas.add(url)
        
        headers = {'User-Agent': self.user_agents[self.contador_peticiones % len(self.user_agents)]}
        self.contador_peticiones += 1
        
        try:
            respuesta = requests.get(url, headers=headers, timeout=15)
            respuesta.raise_for_status()
            
            soup = BeautifulSoup(respuesta.text, 'html.parser')
            titulo = soup.title.string[:300] if soup.title else 'Sin titulo'
            
            contenido_limpio, palabras = self.limpiar_texto(respuesta.text)
            palabras_clave = self.extraer_palabras_clave(palabras)
            enlaces = self.extraer_enlaces(soup, url)
            
            cursor = self.conexion_bd.cursor()
            cursor.execute("""
                INSERT INTO paginas (url, titulo, contenido_texto, palabras_clave, enlaces, profundidad)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (url, titulo, contenido_limpio, json.dumps(palabras_clave), 
                  json.dumps(enlaces), profundidad))
            self.conexion_bd.commit()
            
            with self.bloqueo:
                self.paginas_indexadas += 1
                logger.info(f"[{self.paginas_indexadas}/{self.limite_paginas}] {titulo[:60]}...")
            
            if profundidad < self.profundidad_max:
                for enlace in enlaces[:10]:
                    self.colas_paginas.put((enlace, profundidad + 1))
            
            return True
            
        except Exception as e:
            logger.warning(f"Error {url}: {e}")
            return False
    
    def worker_indexacion(self):
        """Hilo worker para indexación paralela."""
        while True:
            with self.bloqueo:
                if self.paginas_indexadas >= self.limite_paginas:
                    break
            
            try:
                url, profundidad = self.colas_paginas.get(timeout=2)
                self.indexar_pagina(url, profundidad)
                self.colas_paginas.task_done()
            except queue.Empty:
                # Verificar si hay más trabajo o terminar
                with self.bloqueo:
                    if self.colas_paginas.empty():
                        break
            except Exception as e:
                logger.warning(f"Error en worker: {e}")
    
    def ejecutar_indexacion(self):
        """Ejecuta crawling completo con 5 workers."""
        logger.info(f"Iniciando indexacion: {self.semilla_url}")
        logger.info(f"Limite: {self.limite_paginas} paginas, profundidad max: {self.profundidad_max}")
        
        inicio_tiempo = time.time()
        
        if self.verificar_robots(self.semilla_url):
            self.indexar_pagina(self.semilla_url, 0)
        else:
            logger.error("Semilla bloqueada por robots.txt")
            return
        
        hilos = []
        for _ in range(5):
            hilo = threading.Thread(target=self.worker_indexacion, daemon=True)
            hilo.start()
            hilos.append(hilo)
        
        # Esperar que todos los hilos terminen
        for hilo in hilos:
            hilo.join()
        
        tiempo_total = time.time() - inicio_tiempo
        logger.info(f"Indexacion completada: {self.paginas_indexadas} paginas en {tiempo_total/60:.1f} min")
        self.conexion_bd.close()

def main():
    parser = argparse.ArgumentParser(description="Mini-GoogleBot Indexador")
    parser.add_argument('--semilla', required=True, help="URL semilla")
    parser.add_argument('--limite', type=int, default=1000, help="Max paginas")
    parser.add_argument('--profundidad', type=int, default=4, help="Max profundidad")
    
    args = parser.parse_args()
    
    bot = MiniGoogleBot(args.semilla, args.limite, args.profundidad)
    bot.ejecutar_indexacion()

if __name__ == "__main__":
    main()
