"""
CLI profesional con argparse
Desarrolla una aplicación CLI gestor-archivos con subcomandos:
text
gestor-archivos listar --directorio /ruta
gestor-archivos limpiar --extension .tmp --dias 7
gestor-archivos comparar dir1 dir2
gestor-archivos --verbose --config config.json
Con ayuda contextual, auto-completado y validación de argumentos.
"""

# Programa 55: CLI profesional con argparse

import argparse
import os
import glob
from datetime import datetime, timedelta


def listar_directorio(args):
    """
    Subcomando 'listar': lista contenido de directorio.
    """
    directorio = args.directorio or "."
    if not os.path.isdir(directorio):
        print(f"❌ '{directorio}' no es un directorio")
        return
    
    print(f"Contenido de '{directorio}':")
    for elemento in sorted(os.listdir(directorio)):
        ruta_completa = os.path.join(directorio, elemento)
        tipo = "DIR" if os.path.isdir(ruta_completa) else "FIL"
        tamano = os.path.getsize(ruta_completa) if os.path.isfile(ruta_completa) else "-"
        print(f"  {tipo:3s} {tamano:>10,} {elemento}")


def limpiar_antiguos(args):
    """
    Subcomando 'limpiar': elimina ficheros antiguos por extensión.
    """
    directorio = args.directorio or "."
    extension = args.extension.lstrip(".")
    dias = args.dias
    
    patron = os.path.join(directorio, f"*.{extension}")
    ficheros = glob.glob(patron)
    
    cutoff = datetime.now() - timedelta(days=dias)
    eliminados = 0
    
    for fichero in ficheros:
        mtime = datetime.fromtimestamp(os.path.getmtime(fichero))
        if mtime < cutoff:
            try:
                os.remove(fichero)
                print(f"🗑️  Eliminado: {fichero}")
                eliminados += 1
            except OSError as e:
                print(f"❌ Error eliminando {fichero}: {e}")
    
    print(f"\nEliminados {eliminados} ficheros .{extension} > {dias} días")


def comparar_directorios(args):
    """
    Subcomando 'comparar': compara contenido de dos directorios.
    """
    dir1, dir2 = args.dir1, args.dir2
    
    if not os.path.isdir(dir1):
        print(f"❌ '{dir1}' no existe")
        return
    if not os.path.isdir(dir2):
        print(f"❌ '{dir2}' no existe")
        return
    
    ficheros1 = set(os.listdir(dir1))
    ficheros2 = set(os.listdir(dir2))
    
    solo1 = ficheros1 - ficheros2
    solo2 = ficheros2 - ficheros1
    comunes = ficheros1 & ficheros2
    
    print(f"Solo en '{dir1}': {len(solo1)} ficheros")
    for f in sorted(solo1):
        print(f"  + {f}")
    
    print(f"\nSolo en '{dir2}': {len(solo2)} ficheros")
    for f in sorted(solo2):
        print(f"  + {f}")
    
    print(f"\nComunes: {len(comunes)} ficheros")


def main():
    """
    Configuración del parser CLI.
    """
    parser = argparse.ArgumentParser(
        description="Gestor de Archivos CLI Profesional",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos:
  gestor-archivos listar --directorio /tmp
  gestor-archivos limpiar --extension tmp --dias 7
  gestor-archivos comparar dir1 dir2
        """
    )
    parser.add_argument("--verbose", "-v", action="store_true", help="Modo verboso")
    
    subparsers = parser.add_subparsers(dest="comando", help="Subcomandos")
    
    # Subcomando listar
    listar = subparsers.add_parser("listar", help="Lista contenido directorio")
    listar.add_argument("--directorio", "-d", help="Directorio a listar")
    
    # Subcomando limpiar
    limpiar = subparsers.add_parser("limpiar", help="Limpia ficheros antiguos")
    limpiar.add_argument("--extension", "-e", required=True, help="Extensión a limpiar")
    limpiar.add_argument("--dias", "-d", type=int, default=7, help="Días de antigüedad")
    limpiar.add_argument("--directorio", help="Directorio a limpiar")
    
    # Subcomando comparar
    comparar = subparsers.add_parser("comparar", help="Compara dos directorios")
    comparar.add_argument("dir1", help="Primer directorio")
    comparar.add_argument("dir2", help="Segundo directorio")
    
    args = parser.parse_args()
    
    if args.verbose:
        print(f"Argumentos: {vars(args)}")
    
    if args.comando == "listar":
        listar_directorio(args)
    elif args.comando == "limpiar":
        limpiar_antiguos(args)
    elif args.comando == "comparar":
        comparar_directorios(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
