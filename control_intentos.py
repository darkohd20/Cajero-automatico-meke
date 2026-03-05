# este codigo esta bien solo seria cambiar el valor de usuario_autenticacion a un valor numerico o alfanumerico
# puedes hablar con el couder que hizo el config, seria bueno que esa variable usuario_autenticacion este en el archivo config
# si necesitan explicacion le pueden decir a Cristian y hacemos una reunion y vemos parte por parte 

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