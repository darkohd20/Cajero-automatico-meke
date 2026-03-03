historial = []

def registrar(nombre, tipo, monto, saldo):
    if monto is None:
        historial.append(f"{nombre} - {tipo} - saldo: ${saldo}")
    else:
        historial.append(f"{nombre} - {tipo} - monto: ${monto} - saldo: ${saldo}")

