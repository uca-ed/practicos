
import json


def main():

    f = open('01.json')
    estructura = json.load(f)

    print("\n----------------------Propiedades----------------------\n")

    ref = Reflexividad(estructura)
    sim = Simetria(estructura)
    anti = Antisimetria(estructura)
    trans = Transitividad(estructura)

    print("Reflexiva:", ref)
    print("Simétrica:", sim)
    print("Antisimétrica:", anti)
    print("Transitiva:", trans)

    print("\n----------------------Tipo de relación----------------------\n")

    if ref and sim and trans:
        print("Es una relación de equivalencia")

    if ref and anti and trans:
        print("Es una relación de orden")

    if not (ref and sim and trans) and not (ref and anti and trans):
        print("No es relación de equivalencia ni de orden")

    f.close()


def Reflexividad(estr):

    for nodo in estr['E']:

        if nodo not in estr['E'][nodo]:
            return False

    return True


def Simetria(estr):

    for nodo, vecinos in estr['E'].items():

        for vecino in vecinos:

            if nodo not in estr['E'][vecino]:
                return False

    return True


def Antisimetria(estr):

    for nodo, vecinos in estr['E'].items():

        for vecino in vecinos:

            if nodo != vecino and nodo in estr['E'][vecino]:
                return False

    return True


def Transitividad(estr):

    for nodo, vecinos in estr['E'].items():

        for vecino in vecinos:

            for vecino_del_vecino in estr['E'][vecino]:

                if vecino_del_vecino not in estr['E'][nodo]:
                    return False

    return True


main()