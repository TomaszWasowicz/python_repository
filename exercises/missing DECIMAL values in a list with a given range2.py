from decimal import *


def decimal():
    lista = []
    i = Decimal('2.0')
    while i < 6:
        lista.append(i)
        i += Decimal('0.5')
    print(lista)
    return


decimal()



