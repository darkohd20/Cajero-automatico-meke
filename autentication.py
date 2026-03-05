form control-intentos.py inmport control_intentos
form menu.py import menu

print("Fecha:", datetime.now().strftime("%I:%M:%S %p"))
print ("=======================")
print ("=TechBank Riwi digital=")
print ("=======================")

def autenticar():
    usuario_autenticacion = "David"
    pin =  input ("ingrese pin: ")

    if pin.lower() == usuario_autenticacion.lower():
        return True
    else:
        return control-intentos(pin)
ingreso=autenticar()
if ingreso:
    return menu()
