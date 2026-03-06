from saldo import actualizar_saldo
from historial import registrar_historial
from config import obtener_nombre
from reglas import validar_reglas
from validacion_numeral import validar_numero

def depositar(saldo):
    monto = int(input("Ingrese monto a depositar: "))

    if (validar_numero(monto)):
        if (validar_reglas("deposito", monto, saldo)):
            saldo = saldo + monto
            registrar_historial(obtener_nombre(), "Deposito", monto, saldo)
            actualizar_saldo(saldo)
            print("Depósito exitoso")
            print(f"Nuevo saldo: {saldo}")
