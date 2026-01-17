"""
Consumidor de colas con queue y threading
Simula un sistema de colas de tareas con 3 tipos de trabajadores en hilos:
text
- Productor: genera tareas aleatorias
- Procesador CPU: tareas de cálculo
- Procesador I/O: simula lecturas de ficheros
Muestra estadísticas de velocidad de procesamiento por tipo.
"""

# Programa 56: Sistema de colas con trabajadores threading

import queue
import threading
import time
import random
from collections import defaultdict


class Trabajador(threading.Thread):
    """
    Trabajador genérico que procesa tareas de una cola.
    """
    def __init__(self, nombre, cola_tareas, estadisticas, tiempo_proceso):
        super().__init__(name=nombre)
        self.cola_tareas = cola_tareas
        self.estadisticas = estadisticas
        self.tiempo_proceso = tiempo_proceso
        self.daemon = True
    
    def run(self):
        """
        Bucle principal del trabajador.
        """
        while True:
            try:
                # Esperar tarea (bloqueante)
                tarea = self.cola_tareas.get(timeout=1)
                if tarea is None:  # Señal de parada
                    break
                
                # Procesar tarea
                time.sleep(self.tiempo_proceso + random.uniform(0, 0.1))
                self.estadisticas[self.name] += 1
                
                if self.name.startswith("CPU"):
                    resultado = sum(range(tarea))  # Trabajo CPU
                else:
                    resultado = f"Archivo_{tarea}_leido"  # Trabajo I/O
                
                print(f"{self.name}: tarea {tarea} → {resultado[:20]}...")
                self.cola_tareas.task_done()
                
            except queue.Empty:
                continue


class Productor(threading.Thread):
    """
    Genera tareas para las colas.
    """
    def __init__(self, cola_tareas, num_tareas):
        super().__init__(name="Productor")
        self.cola_tareas = cola_tareas
        self.num_tareas = num_tareas
        self.daemon = True
    
    def run(self):
        for i in range(self.num_tareas):
            tipo_tarea = random.choice(["cpu", "io"])
            self.cola_tareas.put((i, tipo_tarea))
            time.sleep(0.01)  # Ritmo de producción
        print("Productor: Todas las tareas generadas")


def main():
    """
    Función principal del sistema de colas.
    """
    cola_tareas = queue.Queue()
    estadisticas = defaultdict(int)
    
    # Crear trabajadores
    trabajadores_cpu = [Trabajador(f"CPU-{i}", cola_tareas, estadisticas, 0.05) for i in range(2)]
    trabajadores_io = [Trabajador(f"I/O-{i}", cola_tareas, estadisticas, 0.1) for i in range(2)]
    
    # Ruta de distribución de tareas (simple)
    def ruta_tarea(tarea_id, tipo):
        return tipo == "cpu"
    
    productor = Productor(cola_tareas, 100)
    
    print("🚀 Iniciando sistema de colas...")
    productor.start()
    
    for w in trabajadores_cpu + trabajadores_io:
        w.start()
    
    productor.join()
    cola_tareas.join()  # Esperar que se procesen todas
    
    print("\n=== ESTADÍSTICAS FINALES ===")
    total_procesado = sum(estadisticas.values())
    print(f"Total tareas: {total_procesado}")
    for nombre, cantidad in sorted(estadisticas.items()):
        print(f"  {nombre}: {cantidad} tareas")


if __name__ == "__main__":
    main()
