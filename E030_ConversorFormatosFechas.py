"""
Conversor de formatos de fecha con datetime
Escribe un programa que use la librería datetime para:
- Pedir al usuario una fecha en formato dd/mm/aaaa.
- Convertirla a un objeto date.
- Mostrar la misma fecha en diferentes formatos: aaaa-mm-dd, nombre del día de la semana en castellano, y el número de día del año (1–365/366).
Opcional: encapsular la lógica en una clase FechaUtil.
"""

# Programa 30: Conversor de formatos de fecha con datetime

from datetime import datetime, date  # Para manejar fechas y formato


def obtener_nombre_dia_semana(fecha):
    """
    Devuelve el nombre del día de la semana en castellano
    para una fecha dada.
    """
    nombres_dias = [
        "lunes", "martes", "miércoles", "jueves",
        "viernes", "sábado", "domingo"
    ]
    # weekday() devuelve 0 para lunes, 6 para domingo
    return nombres_dias[fecha.weekday()]


def main():
    """
    Función principal del programa.
    """
    texto_fecha = input("Introduce una fecha en formato dd/mm/aaaa: ")

    try:
        fecha_obj = datetime.strptime(texto_fecha, "%d/%m/%Y").date()
    except ValueError:
        print("La fecha no tiene el formato correcto o no es válida.")
        return

    # Formato aaaa-mm-dd
    formato_iso = fecha_obj.isoformat()

    # Nombre del día de la semana
    dia_semana = obtener_nombre_dia_semana(fecha_obj)

    # Número de día del año
    dia_del_anyo = fecha_obj.timetuple().tm_yday

    print("\nFORMATOS DE FECHA:")
    print("Formato ISO (aaaa-mm-dd):", formato_iso)
    print("Día de la semana:", dia_semana)
    print("Día del año:", dia_del_anyo)


if __name__ == "__main__":
    main()
