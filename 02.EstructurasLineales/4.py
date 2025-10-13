import json

def radixSort(A:list,P:list):
    # LAS PALABRAS SON [PALO,NUMERO]

    palos=A[0]
    numeros=A[1]

    colasAux=[]
    for e in numeros:
        colasAux.append([])

    while len(P)>0:
        x=P.pop(0)
        colasAux[numeros.index(x[1])].append(x)

    for cola in colasAux:
        while len(cola)>0:
            P.append(cola.pop(0))

    colasAux=[]
    for e in palos:
        colasAux.append([])

    while len(P)>0:
        x=P.pop(0)
        colasAux[palos.index(x[0])].append(x)
    
    for cola in colasAux:
        while len(cola)>0:
            P.append(cola.pop(0))

    return P

def leerJson(ruta):
    with open(ruta) as fi:
        estructura = json.load(fi)

    palos = estructura['alfabetos']['palos']
    numeros= estructura['alfabetos']['numeros']
    P=estructura['cartas']
    A=[palos,numeros]
    
    return [A,P]

def main():
    parametros=leerJson('/home/ignacio-berkelaar/Documents/GitHub/practicos/02.EstructurasLineales/datosRadix.json')

    print(f'PALABRAS DESORDENADAS: {parametros[1]}')
    PalabrasOrdenadas=radixSort(parametros[0],parametros[1])

    print(f'PALABRAS ORDENADAS: {PalabrasOrdenadas}')

if __name__=='__main__':
    main()