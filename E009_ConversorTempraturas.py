"""
Conversor de temperaturas
Implementa varias funciones para convertir entre Celsius, Fahrenheit y Kelvin.
Pide los datos por teclado y guarda un historial de conversiones en un fichero de texto.
"""

# Programa 9: Conversor de temperaturas con historial

def celsius_a_fahrenheit(c):
    """
    Convierte una temperatura de grados Celsius a Fahrenheit.
    """
    return c * 9 / 5 + 32


def fahrenheit_a_celsius(f):
    """
    Convierte una temperatura de grados Fahrenheit a Celsius.
    """
    return (f - 32) * 5 / 9


def celsius_a_kelvin(c):
    """
    Convierte una temperatura de grados Celsius a Kelvin.
    """
    return c + 273.15


def kelvin_a_celsius(k):
    """
    Convierte una temperatura de Kelvin a Celsius.
    """
    return k - 273.15


def guardar_en_historial(texto):
    """
    Guarda una línea de texto en el fichero de historial.
    """
    try:
        with open("historial_conversiones.txt", "a", encoding="utf-8") as f:
            f.write(texto + "\n")
    except OSError as e:
        print("Error al escribir en el historial:", e)


def mostrar_menu():
    """
    Muestra el menú de opciones y devuelve la opción elegida.
    """
    print("\n===== CONVERSOR DE TEMPERATURAS =====")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    print("3. Celsius a Kelvin")
    print("4. Kelvin a Celsius")
    print("5. Salir")
    opcion = input("Elige una opción (1-5): ")
    return opcion


def main():
    """
    Función principal del programa.
    """
    while True:
        opcion = mostrar_menu()

        if opcion == "5":
            print("Saliendo del conversor...")
            break

        try:
            valor = float(input("Introduce la temperatura: "))
        except ValueError:
            print("Temperatura no válida.")
            continue

        if opcion == "1":
            resultado = celsius_a_fahrenheit(valor)
            texto = f"{valor:.2f} ºC = {resultado:.2f} ºF"
        elif opcion == "2":
            resultado = fahrenheit_a_celsius(valor)
            texto = f"{valor:.2f} ºF = {resultado:.2f} ºC"
        elif opcion == "3":
            resultado = celsius_a_kelvin(valor)
            texto = f"{valor:.2f} ºC = {resultado:.2f} K"
        elif opcion == "4":
            resultado = kelvin_a_celsius(valor)
            texto = f"{valor:.2f} K = {resultado:.2f} ºC"
        else:
            print("Opción no válida.")
            continue

        print("Resultado:", texto)
        guardar_en_historial(texto)


if __name__ == "__main__":
    main()
