"""
Watcher de ficheros con watchdog
Implementa un monitor de ficheros que:
- Vigile un directorio por creaciones/modificaciones/eliminaciones.
- Reaccione automáticamente (ej: comprimir nuevos .txt).
- Pause/reanude vigilancia con señales del sistema.
- Genere reporte de actividad.
"""

# Programa 58: Monitor de ficheros con watchdog
# Instalar: pip install watchdog

import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import gzip
import shutil


class ManejadorEventos(FileSystemEventHandler):
    """
    Reacciona a eventos del sistema de ficheros.
    """
    def __init__(self, directorio_vigilado):
        self.directorio_vigilado = directorio_vigilado
        self.reporte_actividad = []
    
    def on_created(self, event):
        """Nuevo fichero/directorios creado."""
        if not event.is_directory and event.src_path.endswith('.txt'):
            print(f"📄 NUEVO: {os.path.basename(event.src_path)}")
            self.comprimir_txt(event.src_path)
        self.reporte_actividad.append(f"CREADO: {event.src_path}")
    
    def on_modified(self, event):
        """Fichero modificado."""
        print(f"✏️  MODIF: {os.path.basename(event.src_path)}")
        self.reporte_actividad.append(f"MODIF: {event.src_path}")
    
    def on_deleted(self, event):
        """Fichero eliminado."""
        print(f"🗑️  BORRADO: {os.path.basename(event.src_path)}")
        self.reporte_actividad.append(f"BORRADO: {event.src_path}")
    
    def on_moved(self, event):
        """Fichero movido."""
        print(f"🔄 MOVIDO: {event.dest_path}")
        self.reporte_actividad.append(f"MOVIDO: {event.dest_path}")
    
    def comprimir_txt(self, ruta_txt):
        """Comprimen nuevos .txt automáticamente."""
        try:
            ruta_gz = ruta_txt + ".gz"
            with open(ruta_txt, 'rb') as f_in:
                with gzip.open(ruta_gz, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
            print(f"📦 Comprimido: {os.path.basename(ruta_gz)}")
        except Exception as e:
            print(f"❌ Error comprimiendo: {e}")
    
    def generar_reporte(self, ruta_reporte):
        """Genera reporte de actividad."""
        with open(ruta_reporte, "w", encoding="utf-8") as f:
            f.write("=== REPORTE DE ACTIVIDAD ===\n")
            f.write(f"Vigilado: {self.directorio_vigilado}\n")
            f.write(f"Eventos: {len(self.reporte_actividad)}\n\n")
            for evento in self.reporte_actividad[-50:]:  # Últimos 50
                f.write(event + "\n")
        print(f"📋 Reporte guardado: {ruta_reporte}")


def monitor_directorio(directorio, segundos=0):
    """
    Monitor principal del directorio.
    """
    if not os.path.isdir(directorio):
        print(f"❌ '{directorio}' no es un directorio válido")
        return
    
    event_handler = ManejadorEventos(directorio)
    observer = Observer()
    observer.schedule(event_handler, directorio, recursive=False)
    
    print(f"👀 Vigilando '{directorio}' (Ctrl+C para parar)")
    print("Acciones automáticas: nuevos .txt → comprimidos .gz")
    
    observer.start()
    try:
        if segundos > 0:
            time.sleep(segundos)
        else:
            while True:
                time.sleep(1)
    except KeyboardInterrupt:
        print("\n⏹️  Parando monitor...")
    
    observer.stop()
    observer.join()
    
    # Generar reporte final
    event_handler.generar_reporte("actividad_monitor.txt")


def main():
    """
    Función principal interactiva.
    """
    directorio = input("📁 Directorio a vigilar [/tmp]: ").strip() or "/tmp"
    
    if input("🚀 ¿Iniciar monitor? [s/N]: ").lower().startswith('s'):
        duracion = input("Duración en segundos [infinita]: ").strip()
        duracion = int(duracion) if duracion.isdigit() else 0
        monitor_directorio(directorio, duracion)


if __name__ == "__main__":
    main()
