from config import obtener_saldo_inicial
saldo = obtener_saldo_inicial()

def consultar_saldo():
    print(f"su saldo actual es: ${saldo}")

def obtener_valor_saldo():
    return saldo

def actualizar_saldo(nuevo_saldo):
    global saldo
    saldo = nuevo_saldo