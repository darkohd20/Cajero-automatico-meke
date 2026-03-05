def validar_numero():
    while True:
        try:
            monto = int(input("Ingrese el monto a retirar: "))
            return monto
        except ValueError:
            print("Error: ingrese solo números")
