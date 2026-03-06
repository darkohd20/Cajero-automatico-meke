from saldo import consultar_saldo
from saldo import obtener_valor_saldo
from depositar import depositar
from historial import mostrar_historial
from retiro import retirar

def menu():
    print("\n--- Tech Bank Digital Riwi ---")
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. Historial")
    print("5. Salir")


def pedir_operaciones():
    while True:
        try:
            cantidad = int(input("¿Cuántas operaciones desea realizar?: "))

            if cantidad <= 0:
                print("Debe ingresar un número válido")
            else:
                return cantidad

        except ValueError:
            print("Eso no es un número, inténtelo otra vez")


def operaciones(cantidad):
    for i in range(cantidad):

        menu()

        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                consultar_saldo()

            elif opcion == 2:
                retirar(obtener_valor_saldo())

            elif opcion == 3:
                depositar(obtener_valor_saldo())

            elif opcion == 4:
                mostrar_historial()

            elif opcion == 5:
                print("Saliendo de Tech Bank Digital Riwi ;)")
                break

            else:
                print("Opción no válida")

        except ValueError:
            print("Eso no es un número, inténtelo otra vez")

            
