"""
Promedios con tuplas
Crea una función que reciba una lista de tuplas, donde cada tupla contiene (nombre, nota1, nota2, nota3), y devuelva un nuevo diccionario con el promedio de cada alumno. Muestra los nombres ordenados por nota media descendente.
"""

# Programa 3: Promedio de notas con lista de tuplas

def calcular_promedios(lista_alumnos):
    """
    Recibe una lista de tuplas con el formato:
    (nombre, nota1, nota2, nota3)
    Devuelve un diccionario: {nombre: nota_media}
    """
    promedios = {}
    for nombre, nota1, nota2, nota3 in lista_alumnos:
        media = (nota1 + nota2 + nota3) / 3
        promedios[nombre] = media
    return promedios


def mostrar_ordenados_por_media(promedios):
    """
    Recibe un diccionario {nombre: media} y muestra los alumnos
    ordenados por su nota media de mayor a menor.
    """
    # sorted devuelve una lista de tuplas (nombre, media)
    # key indica que se ordene por el valor de la media
    lista_ordenada = sorted(promedios.items(),
                            key=lambda par: par[1],
                            reverse=True)

    print("Alumnos ordenados por nota media (mayor a menor):")
    for nombre, media in lista_ordenada:
        print(f"{nombre}: {media:.2f}")


def leer_alumnos():
    """
    Permite introducir alumnos por teclado.
    Devuelve una lista de tuplas (nombre, nota1, nota2, nota3).
    """
    alumnos = []
    print("Introduce datos de alumnos (deja el nombre vacío para terminar).")
    while True:
        nombre = input("Nombre del alumno: ").strip()
        if nombre == "":
            break

        try:
            nota1 = float(input("Nota 1: "))
            nota2 = float(input("Nota 2: "))
            nota3 = float(input("Nota 3: "))
        except ValueError:
            print("Alguna nota no es válida. Vuelve a intentarlo.")
            continue

        alumnos.append((nombre, nota1, nota2, nota3))
    return alumnos


def main():
    """
    Función principal del programa.
    """
    alumnos = leer_alumnos()
    if not alumnos:
        print("No se han introducido alumnos.")
        return

    promedios = calcular_promedios(alumnos)
    mostrar_ordenados_por_media(promedios)


if __name__ == "__main__":
    main()
