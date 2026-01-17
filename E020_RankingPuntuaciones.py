"""
Pequeño “ranking” de puntuaciones
Pide al usuario que introduzca varias puntuaciones de jugadores en el formato nombre;puntuacion, hasta que introduzca una cadena vacía.
Guarda los datos en una lista de tuplas (nombre, puntuacion) y al final muestra un ranking con los 5 jugadores con mayor puntuación. Si hay menos de 5, muestra todos.
"""

# Programa 20: Ranking de puntuaciones de jugadores

def leer_puntuaciones():
    """
    Lee puntuaciones de jugadores desde teclado.
    Cada entrada tiene el formato: nombre;puntuacion
    Termina cuando se introduce una línea vacía.
    Devuelve una lista de tuplas (nombre, puntuacion).
    """
    puntuaciones = []
    print("Introduce puntuaciones en el formato nombre;puntuacion.")
    print("Pulsa ENTER sin escribir nada para terminar.\n")

    while True:
        linea = input("Entrada: ").strip()
        if linea == "":
            break

        partes = linea.split(";")
        if len(partes) != 2:
            print("Formato incorrecto. Debe ser nombre;puntuacion.")
            continue

        nombre = partes[0].strip()
        if nombre == "":
            print("El nombre no puede estar vacío.")
            continue

        try:
            puntuacion = int(partes[1])
        except ValueError:
            print("La puntuación debe ser un número entero.")
            continue

        puntuaciones.append((nombre, puntuacion))

    return puntuaciones


def mostrar_ranking(puntuaciones, limite=5):
    """
    Muestra el ranking de los 'limite' jugadores con mayor puntuación.
    Si hay menos de 'limite' jugadores, muestra todos.
    """
    if not puntuaciones:
        print("No se han introducido puntuaciones.")
        return

    # Ordenamos por puntuación descendente
    ordenadas = sorted(puntuaciones, key=lambda x: x[1], reverse=True)

    print(f"\n--- RANKING (TOP {limite}) ---")
    for posicion, (nombre, puntuacion) in enumerate(ordenadas[:limite], start=1):
        print(f"{posicion}. {nombre} - {puntuacion}")


def main():
    """
    Función principal del programa.
    """
    puntuaciones = leer_puntuaciones()
    mostrar_ranking(puntuaciones, limite=5)


if __name__ == "__main__":
    main()
