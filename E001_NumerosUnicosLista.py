"""
Números únicos en una lista
Pide al usuario una serie de números separados por espacios y guarda solo los valores únicos (sin repeticiones). Muestra la lista ordenada de menor a mayor.
"""

# Programa 1: Números únicos en una lista

def leer_numeros():
    """
    Lee del usuario una línea de números separados por espacios
    y devuelve una lista de enteros.
    """
    texto = input("Introduce números separados por espacios: ")
    partes = texto.split()
    numeros = []

    for parte in partes:
        try:
            numero = int(parte)
            numeros.append(numero)
        except ValueError:
            print(f"El valor '{parte}' no es un número entero. Se ignora.")
    return numeros


def obtener_unicos_ordenados(numeros):
    """
    Recibe una lista de números y devuelve una nueva lista
    con los valores únicos ordenados de menor a mayor.
    """
    # Convertimos a conjunto para eliminar duplicados
    conjunto_unicos = set(numeros)
    # Volvemos a lista y ordenamos
    lista_ordenada = sorted(conjunto_unicos)
    return lista_ordenada


def main():
    """
    Función principal del programa.
    """
    numeros = leer_numeros()
    unicos_ordenados = obtener_unicos_ordenados(numeros)

    print("Números introducidos:", numeros)
    print("Números únicos ordenados:", unicos_ordenados)


if __name__ == "__main__":
    main()
