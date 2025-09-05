import json

import json

def leerJson(ruta):
    with open(ruta) as fi:
        estructura = json.load(fi)

    nodos = estructura['P']
    indice = {nodo: idx for idx, nodo in enumerate(nodos)}  
    n = len(nodos)

    adyacencia = {u: set(estructura['E'].get(u, [])) for u in nodos}

    M1 = [[0]*n for _ in range(n)]
    for u in nodos:
        i = indice[u]
        for v in adyacencia[u]:
            j = indice[v]
            M1[i][j] = 1
    
    return M1


def l(P,z):
    z-=1
    vIzq=[]
    for j in range(0,len(P[0])):
        if P[j][z]!=0: # si tiene un arco entrante
            vIzq.append(j+1)
        
    return vIzq

def r(P,z):
    z-=1
    vDer=[]
    for j in range(0,len(P[0])):
        if P[z][j]!=0: # si tiene un arco saliente
            vDer.append(j+1)
        
    return vDer



def formarRespuesta(CLOSED, inicio, fin):
    camino = []
    actual = fin
    while actual is not None:
        camino.append(actual)
        # buscar predecesor
        pred = None
        for (n, p) in CLOSED:
            if n == actual:
                pred = p
                break
        actual = pred
    return list(reversed(camino))

def encontraPaso(M,a,b):
    OPEN=[]
    CLOSED=[]
    OPEN.append((a,None))
    while len(OPEN)>0:
        (z,y)=OPEN.pop(0)
        CLOSED.append((z,y))
        Rz=r(M,z)
        if b in Rz:
            CLOSED.append((b,z))
            return formarRespuesta(CLOSED, a, b)
        visitados = {n for (n, _) in OPEN} | {n for (n, _) in CLOSED}
        for w in Rz:
            if w not in visitados:
                OPEN.append((w, z))
    return None
            
        


def main():
    M1=leerJson('/home/ignacio-berkelaar/Documents/GitHub/practicos/01.Grafos/archivos_ej3/esDivisorDe-200.json')
    M2=leerJson('/home/ignacio-berkelaar/Documents/GitHub/practicos/01.Grafos/archivos_ej3/esDivisorDe-2000.json')
    M3=leerJson('/home/ignacio-berkelaar/Documents/GitHub/practicos/01.Grafos/archivos_ej3/esDivisorDe-20000.json')
    M4=leerJson('/home/ignacio-berkelaar/Documents/GitHub/practicos/01.Grafos/archivos_ej3/multiplos200Ref.json')
    M5=leerJson('/home/ignacio-berkelaar/Documents/GitHub/practicos/01.Grafos/archivos_ej3/multiplos2000Ref.json')
    M6=leerJson('/home/ignacio-berkelaar/Documents/GitHub/practicos/01.Grafos/archivos_ej3/multiplos20000Ref.json')

    print(encontraPaso(M1,3,20))
    print(encontraPaso(M2,5,120))
    print(encontraPaso(M3,5,120))
    print(encontraPaso(M4,5,120))
    print(encontraPaso(M5,5,120))
    print(encontraPaso(M6,5,120))
    

main()