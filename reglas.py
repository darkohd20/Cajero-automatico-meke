def validar_reglas(monto, saldo):

    if monto <= 0:
        print("El monto debe ser mayor a 0")
        return False

    elif monto > saldo:
        print("Saldo insuficiente")
        return False

    return True