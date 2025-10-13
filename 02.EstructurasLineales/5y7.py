import json

def leerJson(ruta):
    with open(ruta) as fi:
        estructura = json.load(fi)

    E = estructura['E']
    P = estructura['P']

    return [P,E]

def MinimalUnico(P:list,E:dict):
    for nodo in P:
        cond = True  
        for aux in list(E.keys()):
            if nodo in E[str(aux)]:
                cond = False
                break
        if cond:
            return nodo
    return None

def restringir(E:dict,x):
    if x in list(E.keys()):
        E.pop(x)
    for aux in list(E.keys()):
            if x in E[aux]:
                E[aux].remove(x)
    


def tSort(P,E):
    Paux=P
    Eaux=E

    Q=[]
    OT=[]

    Q.append(MinimalUnico(Paux,Eaux))

    while Q[0]!=None:
        x=Q.pop(0)
        OT.append(x)
        Paux.remove(x)
        restringir(Eaux,str(x))
        Q.append(MinimalUnico(Paux,Eaux))

    if len(Paux)>0:
        print('ESTRUCTURA CICLICA')
        return None
    return OT


def main():
    print('\n\nGRAFO 1: ')
    Grafo=leerJson('/home/ignacio-berkelaar/Documents/GitHub/practicos/02.EstructurasLineales/grafo1.json')
    print(Grafo[1])
    print(Grafo[0])
    print('ORDENADO: ',tSort(Grafo[0],Grafo[1]))

    print('\n\nGRAFO 2: ')
    Grafo=leerJson('/home/ignacio-berkelaar/Documents/GitHub/practicos/02.EstructurasLineales/grafo2.json')
    print(Grafo[1])
    print(Grafo[0])
    print('ORDENADO: ',tSort(Grafo[0],Grafo[1]))


    print('\n\nGRAFO 3: ')
    Grafo=leerJson('/home/ignacio-berkelaar/Documents/GitHub/practicos/02.EstructurasLineales/grafo3.json')
    print(Grafo[1])
    print(Grafo[0])
    print('ORDENADO: ',tSort(Grafo[0],Grafo[1]))

if __name__=='__main__':
    main()