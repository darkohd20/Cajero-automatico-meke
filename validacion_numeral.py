# buena implementacion, solo estaba de mas pedir el monto
# si necesitan explicacion le pueden decir a Cristian y hacemos una reunion y vemos parte por parte 
def validar_numero(monto):
    while True:
        try:
            return monto
        except ValueError:
            print("Error: ingrese solo números")

