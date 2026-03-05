import os
from datetime import datetime   
saldo= 1000
retiros_realizados = 0
limite_de_retiros = 3
nombre = input("Ingrese su nombre: ")

# este archivo config estaba incompleto, por que ? nada mas tenia el saldo y el nombre pero
# no habia forma de obtener los valores para poder trabajarlos en los demas archivos
#  Se crearon 5 funciones que son necesarias para obtener los valores del config en otros archivos
#  Se agregaron 2 variables que faltaban que era retiros realizados y limite de retiros esas variables son necesarias aca en el config
## si necesitan explicacion le pueden decir a Cristian y hacemos una reunion y vemos parte por parte 

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