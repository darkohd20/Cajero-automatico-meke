import os
from datetime import datetime   
saldo= 1000
retiros_realizados = 0
limite_de_retiros = 3
nombre = input("Ingrese su nombre: ")

def obtener_nombre():
    return nombre

def obtener_saldo_inicial():
    return saldo

def obtener_retiros_realizados():
    return retiros_realizados

def acumular_retiros():
    global retiros_realizados
    retiros_realizados = retiros_realizados + 1

def obtener_limites_retiros():
    return limite_de_retiros