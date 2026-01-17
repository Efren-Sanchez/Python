"""
Framework de testing unitario casero
Implementa un mini framework de tests con las siguientes características:
- Función assert_equals(valor_real, valor_esperado) que lance AssertionError descriptivo.
- Función assert_raises(Exception, funcion, *args) para comprobar excepciones.
- Función run_tests(lista_tests) que ejecute tests y muestre % de éxito.
"""

# Programa 46: Mini framework de testing unitario

# NO definimos AssertionError personalizada - usamos la nativa de Python


def assert_equals(valor_real, valor_esperado, mensaje=""):
    """
    Comprueba que dos valores sean iguales.
    """
    if valor_real != valor_esperado:
        raise AssertionError(
            f"AssertionError: {valor_real} != {valor_esperado}"
            f"{' (' + mensaje + ')' if mensaje else ''}"
        )


def assert_raises(tipo_excepcion, funcion, *args, **kwargs):
    """
    Comprueba que una función lance la excepción esperada.
    """
    try:
        funcion(*args, **kwargs)
    except tipo_excepcion:
        return True
    except Exception as e:
        raise AssertionError(f"Se esperaba {tipo_excepcion.__name__}, pero se obtuvo {type(e).__name__}: {e}")
    else:
        raise AssertionError(f"La función NO lanzó {tipo_excepcion.__name__}")


def run_tests(tests):
    """
    Ejecuta una lista de tests y devuelve estadísticas.
    """
    total = len(tests)
    fallidos = 0
    
    print("Ejecutando tests...\n")
    
    for i, test in enumerate(tests, 1):
        nombre = test.get("nombre", f"Test {i}")
        try:
            test["funcion"]()
            print(f"✅ {nombre}")
        except AssertionError as e:
            print(f"❌ {nombre}: {e}")
            fallidos += 1
    
    exito = (total - fallidos) / total * 100
    print(f"\n=== RESULTADOS ===")
    print(f"Total: {total} | Fallidos: {fallidos} | Éxito: {exito:.1f}%")
    return fallidos == 0


def test_suma():
    """
    Test de ejemplo para suma.
    """
    assert_equals(2 + 2, 4, "2+2 debe ser 4")
    assert_equals(5 * 3, 15, "5*3 debe ser 15")


def test_excepcion():
    """
    Test que comprueba una excepción.
    """
    def dividir_cero():
        return 1 / 0
    
    assert_raises(ZeroDivisionError, dividir_cero)


def main():
    """
    Función principal con tests de ejemplo.
    """
    mis_tests = [
        {"nombre": "Test suma básica", "funcion": test_suma},
        {"nombre": "Test excepción ZeroDivisionError", "funcion": test_excepcion}
    ]
    
    todos_pasados = run_tests(mis_tests)
    print("¡TODOS LOS TESTS HAN PASADO!" if todos_pasados else "ALGUNOS TESTS HAN FALLADO.")


if __name__ == "__main__":
    main()
