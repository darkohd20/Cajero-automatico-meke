def menu():
    print("\n--- Menu Ñekli ---")
    print("1. Opción uno")
    print("2. Opción dos")
    print("3. Opción tres")
    print("4. Salir")


while True:
    try:
        operaciones = int(input("Cuántas operaciones desea realizar?: "))
        

        if operaciones <= 0:
            print("Debe ingresar un número válido")
        else:
            break

    except ValueError:
        print("Eso no es un número, inténtelo otra vez")