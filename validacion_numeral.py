def validar_numero(monto):
    while True:
        try:
            return monto
        except ValueError:
            print("Error: ingrese solo números")

