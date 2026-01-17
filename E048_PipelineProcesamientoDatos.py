"""
Pipeline de procesamiento de datos con generadores
Crea un pipeline de datos usando generadores encadenados:
datos → pares → cuadrados → filtrar > 1000 → suma
Cada paso debe ser un generador independiente que reciba datos del anterior.
"""

# Programa 48: Pipeline de datos con generadores encadenados

def numeros_aleatorios(cantidad, min_val=1, max_val=100):
    """
    Generador de números aleatorios.
    """
    import random
    for _ in range(cantidad):
        yield random.randint(min_val, max_val)


def solo_pares(numeros):
    """
    Generador que filtra solo números pares de un iterable.
    """
    for numero in numeros:
        if numero % 2 == 0:
            yield numero


def cuadrados(numeros):
    """
    Generador que calcula cuadrados de un iterable.
    """
    for numero in numeros:
        yield numero ** 2


def filtrar_mayor_que(numeros, limite):
    """
    Generador que filtra números > limite de un iterable.
    """
    for numero in numeros:
        if numero > limite:
            yield numero


def pipeline_procesamiento(datos_entrada, limite=1000):
    """
    Pipeline completo: numeros → pares → cuadrados → >limite → suma
    """
    # Encadenar generadores correctamente
    pipeline = filtrar_mayor_que(
        cuadrados(
            solo_pares(datos_entrada)
        ), limite)
    
    return sum(pipeline)


def main():
    """
    Función principal que prueba el pipeline.
    """
    datos = list(range(1, 101))  # Datos de prueba
    
    resultado = pipeline_procesamiento(datos, limite=1000)
    print(f"Suma de cuadrados de pares > 1000: {resultado}")
    
    # Mostrar pipeline paso a paso
    print("\nPipeline paso a paso:")
    pares = [n for n in datos if n % 2 == 0]
    print(f"Pares: {len(pares)} números")
    
    cuadrados_grandes = [n**2 for n in pares if n**2 > 1000]
    print(f"Cuadrados > 1000: {len(cuadrados_grandes)} números")
    print(f"Suma: {sum(cuadrados_grandes)}")


if __name__ == "__main__":
    main()
