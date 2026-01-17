"""
Parser de logs estructurados con json y re
Analiza un ficheo de logs con formato JSON por linea:
{"timestamp": "...", "nivel": "ERROR", "mensaje": "...", "usuario": "..."}
El programa debe:
- Filtrar por nivel de error y usuario.
- Generar reporte estadistico por hora/dia.
- Exportar errores criticos a CSV.
"""

# Programa 57: Parser de logs JSON estructurados (VERSION FINAL)

import json
import re
from collections import defaultdict, Counter
from datetime import datetime
import csv
import random  # Para generar logs de ejemplo
import os


def parsear_linea_log(linea):
    """
    Parsea una linea de log JSON con validacion regex.
    """
    # Verificar formato JSON basico
    patron_log = r'^\s*\{.*\}\s*$'
    if not re.match(patron_log, linea.strip()):
        return None
    
    try:
        log = json.loads(linea.strip())
        # Validar campos minimos
        if "timestamp" not in log or "nivel" not in log:
            return None
        return log
    except json.JSONDecodeError:
        return None


def generar_logs_ejemplo(ruta_salida, num_lineas=500):
    """
    Genera ficheo de logs JSON de ejemplo para pruebas.
    """
    niveles = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    usuarios = [f"usuario{i}" for i in range(1, 11)]
    
    with open(ruta_salida, "w", encoding="utf-8") as f:
        for i in range(num_lineas):
            nivel = random.choice(niveles)
            usuario = random.choice(usuarios)
            timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
            
            log = {
                "timestamp": timestamp,
                "nivel": nivel,
                "mensaje": f"Evento log {i+1}",
                "usuario": usuario,
                "modulo": random.choice(["web", "db", "api", "cache"])
            }
            f.write(json.dumps(log) + "\n")
    
    print(f"Generados {num_lineas} logs en '{ruta_salida}'")


def analizar_logs(ruta_fichero, nivel_minimo="ERROR", usuario_filtro=None):
    """
    Analisis completo de logs con estadisticas temporales.
    """
    estadisticas = {
        "por_hora": Counter(),
        "por_usuario": Counter(),
        "por_nivel": Counter(),
        "por_modulo": Counter(),
        "total_analizados": 0,
        "total_ignorados": 0
    }
    
    with open(ruta_fichero, "r", encoding="utf-8") as f:
        for linea_num, linea in enumerate(f, 1):
            log = parsear_linea_log(linea)
            if not log:
                estadisticas["total_ignorados"] += 1
                continue
            
            # Filtros
            nivel = log["nivel"].upper()
            if nivel < nivel_minimo:
                continue
            
            usuario = log.get("usuario", "anonimo")
            if usuario_filtro and usuario != usuario_filtro:
                continue
            
            # Extraer hora del timestamp ISO
            try:
                timestamp = log["timestamp"]
                fecha_hora = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
                hora = fecha_hora.hour
            except (ValueError, KeyError, AttributeError):  # ✅ Excepciones especificas
                hora = -1
            
            # Estadisticas
            estadisticas["por_hora"][hora] += 1
            estadisticas["por_usuario"][usuario] += 1
            estadisticas["por_nivel"][nivel] += 1
            estadisticas["por_modulo"][log.get("modulo", "desconocido")] += 1
            estadisticas["total_analizados"] += 1
    
    return estadisticas


def exportar_errores_csv(ruta_logs, ruta_csv):
    """
    Exporta errores CRITICAL a CSV con toda la info.
    """
    errores = []
    with open(ruta_logs, "r", encoding="utf-8") as f:
        for linea_num, linea in enumerate(f, 1):
            log = parsear_linea_log(linea)
            if log and log.get("nivel") == "CRITICAL":
                errores.append({
                    "numero_linea": linea_num,
                    "timestamp": log.get("timestamp", ""),
                    "nivel": log.get("nivel", ""),
                    "mensaje": log.get("mensaje", ""),
                    "usuario": log.get("usuario", ""),
                    "modulo": log.get("modulo", "")
                })
    
    with open(ruta_csv, "w", newline="", encoding="utf-8") as f:
        if errores:
            campos = errores[0].keys()
            escritor = csv.DictWriter(f, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(errores)
    
    print(f"{len(errores)} errores CRITICAL exportados a '{ruta_csv}'")


def mostrar_reporte(estadisticas):
    """
    Muestra reporte formateado de estadisticas.
    """
    print("\n" + "="*60)
    print("REPORTE DE ANALISIS DE LOGS")
    print("="*60)
    
    print(f"\nRESUMEN GENERAL:")
    print(f"  Analizados: {estadisticas['total_analizados']}")
    print(f"  Ignorados: {estadisticas['total_ignorados']}")
    
    print(f"\nPOR NIVEL:")
    for nivel, cantidad in estadisticas['por_nivel'].most_common():
        print(f"  {nivel:8s}: {cantidad:4d}")
    
    print(f"\nTOP 5 USUARIOS:")
    for usuario, cantidad in estadisticas['por_usuario'].most_common(5):
        print(f"  {usuario:12s}: {cantidad:4d}")
    
    print(f"\nACTIVIDAD POR HORA:")
    for hora in range(24):
        count = estadisticas['por_hora'][hora]
        if count > 0:
            print(f"  {hora:02d}h: {'*' * (count//10 + 1)} {count}")


def main():
    """
    Funcion principal interactiva.
    """
    ruta_logs = input("Archivo de logs [logs_ejemplo.jsonl]: ").strip() or "logs_ejemplo.jsonl"
    
    if not os.path.exists(ruta_logs):
        print("No existe el archivo. Generando logs de ejemplo...")
        generar_logs_ejemplo(ruta_logs, 1000)
    
    nivel_filtro = input("Nivel minimo [ERROR]: ").strip().upper() or "ERROR"
    usuario_filtro = input("Usuario especifico [todos]: ").strip()
    
    print("Analizando logs...")
    stats = analizar_logs(ruta_logs, nivel_filtro, usuario_filtro)
    
    mostrar_reporte(stats)
    
    exportar = input("\nExportar errores CRITICAL a CSV? [s/N]: ").lower().startswith('s')
    if exportar:
        exportar_errores_csv(ruta_logs, "errores_criticos.csv")


if __name__ == "__main__":
    main()
