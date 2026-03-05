def validacion_numerica(): 
    monto = int(input("ingrese monto: "))
    while monto <=0:
        print("monto invalido")
        monto = int(input("ingrese nuevamente un monto: "))
   
validacion_numerica()