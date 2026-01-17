"""
Mezcla de listas
Genera dos listas de números aleatorios (usa random.randint) y:
- Combínalas alternando valores.
- Elimina los duplicados.
- Guarda el resultado en un fichero llamado resultado.txt.
"""

# Programa 4: Mezcla de dos listas de números aleatorios y guardado en fichero

import random  # Para generar números aleatorios


def generar_lista_aleatoria(tamano, minimo, maximo):
    """
    Genera y devuelve una lista de 'tamano' números enteros aleatorios
    entre 'minimo' y 'maximo' (ambos incluidos).
    """
    lista = []
    for _ in range(tamano):
        numero = random.randint(minimo, maximo)
        lista.append(numero)
    return lista


def mezclar_alternando(lista1, lista2):
    """
    Mezcla dos listas alternando sus elementos.
    Si una lista es más larga, añade los elementos restantes al final.
    """
    mezcla = []
    max_len = max(len(lista1), len(lista2))

    for i in range(max_len):
        if i < len(lista1):
            mezcla.append(lista1[i])
        if i < len(lista2):
            mezcla.append(lista2[i])
    return mezcla


def eliminar_duplicados(lista):
    """
    Devuelve una nueva lista a partir de otra, eliminando los elementos duplicados
    y conservando el orden de aparición.
    """
    vistos = set()
    resultado = []
    for elemento in lista:
        if elemento not in vistos:
            vistos.add(elemento)
            resultado.append(elemento)
    return resultado


def guardar_en_fichero(lista, ruta):
    """
    Guarda en un fichero de texto los elementos de la lista
    separados por espacios.
    """
    try:
        with open(ruta, "w", encoding="utf-8") as f:
            for numero in lista:
                f.write(str(numero) + " ")
        print(f"Lista final guardada en '{ruta}'.")
    except OSError as e:
        print("Error al escribir en el fichero:", e)


def main():
    """
    Función principal del programa.
    """
    # Configuración básica (se podría pedir por teclado)
    tamano = 10
    minimo = 1
    maximo = 20

    lista1 = generar_lista_aleatoria(tamano, minimo, maximo)
    lista2 = generar_lista_aleatoria(tamano, minimo, maximo)

    print("Lista 1:", lista1)
    print("Lista 2:", lista2)

    mezclada = mezclar_alternando(lista1, lista2)
    print("Lista mezclada:", mezclada)

    sin_duplicados = eliminar_duplicados(mezclada)
    print("Lista sin duplicados:", sin_duplicados)

    guardar_en_fichero(sin_duplicados, "resultado.txt")


if __name__ == "__main__":
    main()
