"""
Fusionar y filtrar listas de productos
Pide al usuario dos listas de productos, cada una con nombres separados por comas.
Crea una lista única sin duplicados y luego pide una cadena de búsqueda para mostrar solo los productos que contengan dicho texto. Usa listas y comprensión de listas.
"""

# Programa 12: Fusionar y filtrar listas de productos

def leer_lista_productos(mensaje):
    """
    Lee una lista de productos separados por comas
    y devuelve una lista de cadenas sin espacios sobrantes.
    """
    texto = input(mensaje)
    partes = texto.split(",")
    productos = [p.strip() for p in partes if p.strip() != ""]
    return productos


def fusionar_sin_duplicados(lista1, lista2):
    """
    Fusiona dos listas y elimina duplicados respetando el orden.
    """
    vista = set()
    fusion = []
    for prod in lista1 + lista2:
        if prod not in vista:
            vista.add(prod)
            fusion.append(prod)
    return fusion


def filtrar_productos(productos, texto_busqueda):
    """
    Devuelve una nueva lista con los productos que contienen
    el texto de búsqueda (ignorando mayúsculas/minúsculas).
    """
    texto_busqueda = texto_busqueda.lower()
    return [p for p in productos if texto_busqueda in p.lower()]


def main():
    """
    Función principal del programa.
    """
    lista1 = leer_lista_productos("Introduce la primera lista de productos (separados por comas): ")
    lista2 = leer_lista_productos("Introduce la segunda lista de productos (separados por comas): ")

    fusion = fusionar_sin_duplicados(lista1, lista2)

    print("Lista fusionada sin duplicados:")
    print(fusion)

    texto_busqueda = input("Introduce texto para filtrar productos: ").strip()
    if texto_busqueda == "":
        print("No se ha introducido texto de búsqueda.")
        return

    filtrados = filtrar_productos(fusion, texto_busqueda)

    print("Productos que coinciden con la búsqueda:")
    if filtrados:
        for p in filtrados:
            print("-", p)
    else:
        print("No hay productos que coincidan.")


if __name__ == "__main__":
    main()
