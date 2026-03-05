if monto<=0:            
    print("Error: El monto debe ser mayor a 0")
    return False

if monto > saldo:
   print("Error: Fondos insuficientes")
   return False
