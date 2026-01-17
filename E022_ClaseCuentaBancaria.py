"""
Clase CuentaBancaria con control de saldo
Implementa una clase CuentaBancaria con atributos titular, iban y saldo.
Debe tener métodos para:
- Ingresar dinero.
- Retirar dinero (no permitir saldo negativo).
- Mostrar información de la cuenta.
Crea un pequeño menú para operar con un objeto CuentaBancaria desde teclado.
"""

# Programa 22: Clase CuentaBancaria con control de saldo

class CuentaBancaria:
    """
    Clase que representa una cuenta bancaria sencilla.
    """

    def __init__(self, titular, iban, saldo_inicial=0.0):
        """
        Constructor de la clase.
        """
        self.titular = titular
        self.iban = iban
        self.saldo = saldo_inicial

    def ingresar(self, cantidad):
        """
        Ingresa una cantidad de dinero en la cuenta.
        """
        if cantidad <= 0:
            print("La cantidad a ingresar debe ser positiva.")
            return
        self.saldo += cantidad
        print(f"Ingreso realizado. Saldo actual: {self.saldo:.2f} €")

    def retirar(self, cantidad):
        """
        Retira una cantidad de dinero si hay saldo suficiente.
        """
        if cantidad <= 0:
            print("La cantidad a retirar debe ser positiva.")
            return
        if cantidad > self.saldo:
            print("No hay saldo suficiente para realizar la operación.")
            return
        self.saldo -= cantidad
        print(f"Retirada realizada. Saldo actual: {self.saldo:.2f} €")

    def mostrar_informacion(self):
        """
        Muestra la información de la cuenta.
        """
        print("===== INFORMACIÓN DE LA CUENTA =====")
        print(f"Titular: {self.titular}")
        print(f"IBAN: {self.iban}")
        print(f"Saldo: {self.saldo:.2f} €")


def mostrar_menu():
    """
    Muestra el menú de operaciones y devuelve la opción elegida.
    """
    print("\n===== MENÚ CUENTA BANCARIA =====")
    print("1. Mostrar información")
    print("2. Ingresar dinero")
    print("3. Retirar dinero")
    print("4. Salir")
    return input("Elige una opción (1-4): ")


def main():
    """
    Función principal del programa.
    """
    titular = input("Introduce el nombre del titular: ")
    iban = input("Introduce el IBAN: ")

    cuenta = CuentaBancaria(titular, iban, saldo_inicial=0.0)

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            cuenta.mostrar_informacion()
        elif opcion == "2":
            try:
                cantidad = float(input("Cantidad a ingresar: "))
            except ValueError:
                print("Cantidad no válida.")
                continue
            cuenta.ingresar(cantidad)
        elif opcion == "3":
            try:
                cantidad = float(input("Cantidad a retirar: "))
            except ValueError:
                print("Cantidad no válida.")
                continue
            cuenta.retirar(cantidad)
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
