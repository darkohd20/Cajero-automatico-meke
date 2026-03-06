from saldo import actualizar_saldo
from historial import registrar_historial
from config import obtener_nombre, acumular_retiros, obtener_retiros_realizados, obtener_limites_retiros
from fun_auxiliar import variables_del_tope_de_retiros
from reglas import validar_reglas
from validacion_numeral import validar_numero

def retirar(saldo):
    monto = int(input("Ingrese monto a retirar: "))

    if (validar_numero(monto)):
        if (validar_reglas("retiro", monto, saldo)):
            if (variables_del_tope_de_retiros(obtener_retiros_realizados(), obtener_limites_retiros())):
                print("\n[!] Lo sentimos, has superado el tope de retiros permitido (Máximo 3).")
            else:
                saldo -= monto
                acumular_retiros()
                registrar_historial(obtener_nombre(), "Retiro", monto, saldo)
                actualizar_saldo(saldo)
                print("Retiro exitoso")
                print(f"Nuevo saldo: {saldo}")
            return saldo