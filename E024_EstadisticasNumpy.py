"""
Estadísticas con numpy 
Diseña un programa que, usando la librería numpy (si no está instalada, ejecuta la instruccion 'pip install numpy' en la consola), cree un array con 100 números aleatorios en el rango [0, 100).
Debe calcular:
- Media, desviación estándar y valor máximo.
- Número de valores mayores que la media.
Si numpy no está disponible, muestra un mensaje indicando que no se puede ejecutar el ejercicio.
"""

# Programa 24: Estadísticas con numpy

import random

try:
    import numpy as np
except ImportError:
    np = None


def main():
    """
    Función principal del programa.
    """
    if np is None:
        print("La librería 'numpy' no está disponible. Instálala para ejecutar este ejercicio.")
        return

    # Creamos una lista de 100 números aleatorios entre 0 y 100
    lista = [random.uniform(0, 100) for _ in range(100)]
    array = np.array(lista)

    media = array.mean()
    desviacion = array.std()
    maximo = array.max()

    mayores_media = (array > media).sum()

    print("Array de ejemplo (primeros 10 valores):")
    print(array[:10])
    print(f"\nMedia: {media:.2f}")
    print(f"Desviación estándar: {desviacion:.2f}")
    print(f"Valor máximo: {maximo:.2f}")
    print(f"Número de valores mayores que la media: {mayores_media}")


if __name__ == "__main__":
    main()
