"""
Conversor de monedas con fichero de tasas
En un fichero de texto se almacenan tasas de conversión con el formato codigo_moneda;valor_en_euros (por ejemplo: USD;0.93).
El programa debe: leer el fichero, pedir una cantidad en euros y una moneda destino, y mostrar la conversión. Si la moneda no existe en el fichero, avisar al usuario.
"""

# Programa 16: Conversor de monedas usando fichero de tasas

def cargar_tasas(ruta):
    """
    Carga las tasas de conversión desde un fichero de texto.
    Cada línea tiene el formato: codigo_moneda;valor_en_euros
    Devuelve un diccionario {codigo: valor_en_euros}.
    """
    tasas = {}
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if linea == "":
                    continue
                partes = linea.split(";")
                if len(partes) != 2:
                    continue
                codigo = partes[0].strip().upper()
                try:
                    valor = float(partes[1])
                except ValueError:
                    continue
                tasas[codigo] = valor
    except FileNotFoundError:
        print("El fichero de tasas no existe.")
    except OSError as e:
        print("Error al leer el fichero de tasas:", e)
    return tasas


def convertir_desde_euros(cantidad, codigo_destino, tasas):
    """
    Convierte una cantidad en euros a la moneda destino, usando el diccionario
    de tasas. Cada valor en 'tasas' es el equivalente de 1 unidad de moneda
    destino en euros.
    """
    if codigo_destino not in tasas:
        return None
    valor_en_euros = tasas[codigo_destino]
    # Si 1 unidad de moneda destino vale 'valor_en_euros' euros,
    # entonces 1 euro vale 1 / valor_en_euros unidades de moneda destino.
    conversion = cantidad / valor_en_euros
    return conversion


def main():
    """
    Función principal del programa.
    """
    ruta_tasas = input("Introduce el nombre del fichero de tasas: ")
    tasas = cargar_tasas(ruta_tasas)

    if not tasas:
        print("No se han cargado tasas de conversión.")
        return

    try:
        cantidad_euros = float(input("Introduce la cantidad en euros: "))
    except ValueError:
        print("Cantidad no válida.")
        return

    codigo_destino = input("Introduce el código de la moneda destino (ej: USD): ").strip().upper()

    resultado = convertir_desde_euros(cantidad_euros, codigo_destino, tasas)

    if resultado is None:
        print("La moneda indicada no existe en el fichero de tasas.")
    else:
        print(f"{cantidad_euros:.2f} EUR = {resultado:.2f} {codigo_destino}")


if __name__ == "__main__":
    main()
