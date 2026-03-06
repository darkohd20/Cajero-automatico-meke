historial = []

def registrar_historial(nombre, tipo, monto, saldo):
    if monto is None:
        historial.append(f" {nombre} - {tipo} - saldo: ${saldo}")
    else:
        historial.append(f"{nombre} - {tipo} - monto: ${monto} - saldo: ${saldo}")

def mostrar_historial():
    if len(historial) == 0:
        print("no hay operaciones registradas.")
        return

    print("\n===== historial =====")
    for operacion in historial:
        print(operacion)

    return