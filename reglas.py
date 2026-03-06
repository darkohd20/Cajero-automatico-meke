def validar_reglas(tipo_de_transaccion, monto, saldo):

    if monto <= 0:
        print("El monto debe ser mayor a 0")
        return False

    if (tipo_de_transaccion == "retiro"):
        if monto > saldo:
            print("Saldo insuficiente")
            return False

    return True