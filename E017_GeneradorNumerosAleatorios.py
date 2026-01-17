"""
Generador y analizador de números aleatorios
Haz un programa que genere N números aleatorios entre un mínimo y un máximo, usando la librería random, y los guarde en una lista.
Después:
- Muestra la lista ordenada.
- Muestra cuántos son pares e impares.
- Guarda la lista en un fichero de texto, un número por línea.
"""

# Programa 17: Generador y analizador de números aleatorios

import random  # Para generar números aleatorios


def generar_numeros(cantidad, minimo, maximo):
    """
    Genera una lista de 'cantidad' números enteros aleatorios
    entre 'minimo' y 'maximo' (incluidos).
    """
    lista = []
    for _ in range(cantidad):
        lista.append(random.randint(minimo, maximo))
    return lista


def contar_pares_impares(lista):
    """
    Cuenta cuántos números pares e impares hay en una lista.
    Devuelve una tupla (num_pares, num_impares).
    """
    pares = 0
    impares = 0
    for numero in lista:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares


def guardar_lista_en_fichero(lista, ruta):
    """
    Guarda una lista de números en un fichero de texto,
    un número por línea.
    """
    try:
        with open(ruta, "w", encoding="utf-8") as f:
            for numero in lista:
                f.write(str(numero) + "\n")
        print(f"Lista guardada en '{ruta}'.")
    except OSError as e:
        print("Error al escribir en el fichero:", e)


def main():
    """
    Función principal del programa.
    """
    try:
        cantidad = int(input("¿Cuántos números deseas generar?: "))
        minimo = int(input("Valor mínimo: "))
        maximo = int(input("Valor máximo: "))
    except ValueError:
        print("Debes introducir valores enteros válidos.")
        return

    if minimo > maximo or cantidad <= 0:
        print("Rango o cantidad no válidos.")
        return

    numeros = generar_numeros(cantidad, minimo, maximo)

    print("\nLista generada:")
    print(numeros)

    numeros_ordenados = sorted(numeros)
    print("\nLista ordenada:")
    print(numeros_ordenados)

    pares, impares = contar_pares_impares(numeros)
    print(f"\nNúmeros pares: {pares}")
    print(f"Números impares: {impares}")

    guardar_lista_en_fichero(numeros_ordenados, "numeros_aleatorios.txt")


if __name__ == "__main__":
    main()
