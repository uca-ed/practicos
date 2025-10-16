import json
def restringir(E: dict, x):
    if x in E:
        E.pop(x)
    for k in list(E.keys()):
        if x in E[k]:
            E[k].remove(x)
def Minimal(P: list, E: dict):
    for nodo in P:
        es_minimo = True
        for sucesores in E.values():
            if nodo in sucesores:
                es_minimo = False
                break
        if es_minimo:
            return nodo
    return None
def leerJson(ruta):
    with open(ruta) as fi:
        estructura = json.load(fi)
    E = estructura['E']  
    P = estructura['P']   
    return [P, E]         

def tSort(P, E):
    Paux = list(P)
    Eaux = {k: list(v) for k, v in E.items()}
    Q = []
    OT = []
    Q.append(Minimal(Paux, Eaux))
    while Q[0] != None:
        x = Q.pop(0)        
        OT.append(x)
        Paux.remove(x)
        restringir(Eaux, x)
        Q.append(Minimal(Paux, Eaux))

    if len(Paux) > 0:
        print('ESTRUCTURA CICLICA')
        return None
    return OT

def main():
    print('\n\nGRAFO 1: ')
    Grafo = leerJson('grafo.json')#poner direccion del Json
    print(Grafo[1]); print(Grafo[0])
    print('ORDENADO: ', tSort(Grafo[0], Grafo[1]))
if __name__ == '__main__':
    main()
