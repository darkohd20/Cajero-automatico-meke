usuario_autenticacion = "David"
def control_intentos(pin):

    for i in range(2):
        

        if pin.lower() == usuario_autenticacion.lower():
            print("PIN Correcto.")
            break
        else:
            print(f"Error, PIN incorrecto. Intento: {i + 1}")
            pin = input("Ingrese PIN: ")
    else:
        print("No tiene más intentos.")
        return False