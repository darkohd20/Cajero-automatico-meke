saldo = 1000

try:
    menu = int(input("Opcion de retiro ingrese 2: "))
    if menu == 2:
        monto = float(input("ingrese valor a retirar: "))
        saldo = saldo - monto
        if  monto <= 0:
            print("Valor invalido")
        elif monto > saldo:
            print("Fondos insuficientes.")
        else:
            print(f"Operacion exitosa su salgo actual es {saldo}.")
except:
    print("Error:valor invalido, ingrese una de las opcines disponible")