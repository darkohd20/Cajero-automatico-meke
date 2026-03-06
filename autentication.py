from datetime import datetime 
from control_intentos import control_intentos
from menu import operaciones
from menu import pedir_operaciones

print("Fecha:", datetime.now().strftime("%I:%M:%S %p"))
print ("=======================")
print ("=TechBank Riwi digital=")
print ("=======================")

def autenticar():
    usuario_autenticacion = "David"
    pin =  input ("ingrese pin: ")

    if pin.lower() == usuario_autenticacion.lower():
        operacion = pedir_operaciones()
        operaciones(operacion)
    else:
        control_intentos(pin)
