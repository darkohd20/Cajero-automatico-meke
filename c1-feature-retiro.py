
monto = int(input("Ingrese el monto a retirar: "))

            elif monto > saldo:
                print("Saldo insuficiente")
            else:
                saldo -= monto
                print("Retiro exitoso")
                print(f"Nuevo saldo: {saldo}")
                break