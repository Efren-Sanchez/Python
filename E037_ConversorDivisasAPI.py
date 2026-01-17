"""
Conversor de divisas con API externa
Haz un programa de consola que:
- Pregunte una cantidad en euros y una moneda de destino (por ejemplo, USD, GBP, JPY).
- Consulte una API de tipos de cambio (o use un JSON local que simule esa API) para obtener el tipo de cambio actual.
- Muestre el resultado de la conversion junto con la fecha de la tasa de cambio.
"""

# Programa 37: Conversor de divisas con API (version con datos simulados)

import requests
from datetime import date


def obtener_tipo_cambio(moneda_destino):
    """
    Obtiene el tipo de cambio EUR -> moneda_destino.
    En version real: consulta exchangerate-api.com (necesita API key).
    Aqui simulamos con datos fijos.
    """
    tipos_cambio = {
        "USD": 1.08,
        "GBP": 0.85,
        "JPY": 160.0,
        "CAD": 1.45
    }
    
    if moneda_destino.upper() in tipos_cambio:
        # Usar la fecha actual en lugar de fecha hardcodeada
        fecha_actual = date.today().isoformat()
        return tipos_cambio[moneda_destino.upper()], fecha_actual
    return None, None


def convertir_divisa(cantidad_eur, moneda_destino):
    """
    Convierte cantidad en euros a la moneda destino.
    """
    tipo_cambio, fecha = obtener_tipo_cambio(moneda_destino)
    if tipo_cambio is None:
        return None, None
    cantidad_destino = cantidad_eur * tipo_cambio
    return cantidad_destino, fecha


def main():
    """
    Funcion principal del programa.
    """
    try:
        cantidad = float(input("Cantidad en euros: "))
    except ValueError:
        print("Cantidad no valida.")
        return

    moneda = input("Moneda destino (USD, GBP, JPY, CAD): ").strip()

    cantidad_destino, fecha = convertir_divisa(cantidad, moneda)

    if cantidad_destino is None:
        print("Moneda no soportada.")
    else:
        print(f"\n{cantidad} EUR = {cantidad_destino:.2f} {moneda}")
        print(f"Tipo de cambio actualizado el: {fecha}")


if __name__ == "__main__":
    main()
