from ausgfuasdif import consultar_saldo
def menu():
    print("\n--- Menu Ñekli ---")
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. Salir")

def opciones():
    while True:
        try:
            operaciones = int(input("¿Cuántas operaciones desea realizar?: "))

            if operaciones <= 0:
                print("Debe ingresar un número válido")
            else:
                return operaciones

        except ValueError:
            print("Eso no es un número, inténtelo otra vez")


def real(operaciones):
    for i in range(operaciones):

        menu()

        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                consultar_saldo()

            elif opcion == 2:
                print("Ejecutando opción dos...")

            elif opcion == 3:
                print("Ejecutando opción tres...")

            elif opcion == 4:
                print("Saliendo de Ñekli ;)")
                break

            else:
                print("Opción no válida")

        except ValueError:
            print("Debe ingresar un número")