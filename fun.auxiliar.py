#funcion auxilar
def variables_del_tope_de_retiros(retiros_realizados, limite_de_retiros):
    if retiros_realizados >= limite_de_retiros:
        print("\n[!] Lo sentimos, has superado el tope de retiros permitido (Máximo 3).")
        return False
    return True
