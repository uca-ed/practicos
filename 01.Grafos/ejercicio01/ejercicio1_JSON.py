import json

def main():
    f = open('01.json')
    estructura = json.load(f)

    print("\n----------------------------------------\n")
    a = input("Vecidad derecha del nodo: ")
    print (estructura['E'][ str(a)])

    print("\n----------------------------------------\n")
    b = input("Vecidad izquierda del nodo: ")
    print( VecindadIzq(estructura, b) )

    print("\n----------------------Minimales de la matriz----------------------\n")
    print (Minimales(estructura))

    print("\n----------------------Maximales de la matriz----------------------\n")
    print (Maximales(estructura))

    f.close();


def VecindadIzq(estr, nodo_buscado):
    vecinos_izquierdos = []

    for nodo, vecinos in estr['E'].items():
       
        if str(nodo_buscado) in vecinos:
            
            vecinos_izquierdos.append(int(nodo))
            
    return vecinos_izquierdos


def Maximales(estr):

    maximales = []

    for a in range(len(estr['E'])):
        if estr['E'][ str(a+1) ]==[]:
            maximales.append(a+1);

    print(maximales);


def Minimales(estr):
    minimales = []

    for b in range(len(estr['E'])):
        if estr['E'][ str(b+1) ] == []:
            minimales.append(b+1)

    return minimales;



main()