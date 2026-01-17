"""
Notas por módulo desde fichero
Diseña un programa que lea desde un fichero de texto líneas con el formato alumno;modulo;nota.
Carga los datos en una lista de tuplas y muestra, para un módulo elegido por el usuario, la nota media, la nota máxima y la nota mínima de ese módulo.
"""

# Programa 13: Notas por módulo desde fichero

def leer_notas_desde_fichero(ruta):
    """
    Lee un fichero de texto donde cada línea tiene el formato:
    alumno;modulo;nota
    Devuelve una lista de tuplas (alumno, modulo, nota).
    """
    registros = []
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if linea == "":
                    continue
                partes = linea.split(";")
                if len(partes) != 3:
                    continue
                alumno = partes[0]
                modulo = partes[1]
                try:
                    nota = float(partes[2])
                except ValueError:
                    continue
                registros.append((alumno, modulo, nota))
    except FileNotFoundError:
        print("El fichero no existe.")
    except OSError as e:
        print("Error al leer el fichero:", e)
    return registros


def calcular_estadisticas_modulo(registros, modulo_buscado):
    """
    Calcula media, nota máxima y mínima para un módulo concreto.
    Devuelve una tupla (media, maxima, minima) o (None, None, None)
    si no hay datos.
    """
    notas = [nota for alumno, modulo, nota in registros
             if modulo.lower() == modulo_buscado.lower()]

    if not notas:
        return None, None, None

    media = sum(notas) / len(notas)
    maxima = max(notas)
    minima = min(notas)
    return media, maxima, minima


def main():
    """
    Función principal del programa.
    """
    ruta = input("Introduce el nombre del fichero de notas: ")
    registros = leer_notas_desde_fichero(ruta)

    if not registros:
        print("No se han leído datos de notas.")
        return

    modulo = input("Introduce el nombre del módulo a analizar: ")

    media, maxima, minima = calcular_estadisticas_modulo(registros, modulo)

    if media is None:
        print(f"No se han encontrado datos para el módulo '{modulo}'.")
        return

    print(f"\nEstadísticas para el módulo '{modulo}':")
    print(f"Nota media: {media:.2f}")
    print(f"Nota máxima: {maxima:.2f}")
    print(f"Nota mínima: {minima:.2f}")


if __name__ == "__main__":
    main()
