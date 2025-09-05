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



def esReflexiva(P):
    res=True
    n=len(P[0])
    for i in range(0,n):
        if P[i][i]!=1:
            res=False
    return res

def esSimetrica(P):
    res=True
    n=len(P[0])
    for i in range(0,n):
        for j in range(0,n):
            if P[i][j]!=P[j][i]:
                res=False
    return res

def esAntiSimetrica(P):
    res=True
    n=len(P[0])
    for i in range(0,n):
        for j in range(0,n):
            if  P[i][j]==1 and P[i][j]==P[j][i]:
                res=False
    return res

def esAntiSimetricaDebil(P):
    res=True
    n=len(P[0])
    for i in range(0,n):
        for j in range(0,n):
            if j!=i and P[i][j]==1 and P[i][j]==P[j][i]:
                res=False
    return res



def productoLogicoMatricial(P):  
    n=len(P[0])
    
    C = [[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if P[i][k] and P[k][j]:
                    C[i][j] = 1
                    break  
    return C

def esTransitiva(P):
    n = len(P)
    for k in range(n): # k nodo intermedio
        for i in range(n): 
            if P[i][k]: # si existe la relacion (i,k)
                for j in range(n):
                    if P[k][j] and not P[i][j]: #si existe (k,j) y no (i,j) entonces NO ES TRANSITIVA
                        return False
    return True


def esRDeOrden(P):
    return esTransitiva(P) and esReflexiva(P) and esAntiSimetricaDebil(P)

def esRDeEquivalencia(P):
    return esTransitiva(P) and esReflexiva(P) and esSimetrica(P)


def analisisCompletoDeMatrizDeAdyacencia(P):
    print(f"REFLEXIVIDAD: {esReflexiva(P)}")
    print(f"SIMETRIA: {esSimetrica(P)}")
    print(f"ANTISIMETRIA: {esAntiSimetrica(P)}")
    print(f"ANTISIMETRIA DEBIL: {esAntiSimetricaDebil(P)}")
    print(f"TRANSITIVIDAD: {esTransitiva(P)}")
    print(f"RELACION DE ORDEN: {esRDeOrden(P)}")
    print(f"RELACION DE EQUIVALENCIA: {esRDeEquivalencia(P)}")


def main():
    M1=leerJson('/home/ignacio-berkelaar/Documents/GitHub/practicos/01.Grafos/archivos_ej2/01.json')
    M2=leerJson('/home/ignacio-berkelaar/Documents/GitHub/practicos/01.Grafos/archivos_ej2/02.json')
    M3=leerJson('/home/ignacio-berkelaar/Documents/GitHub/practicos/01.Grafos/archivos_ej2/03.json')

    print("\nAnalisis M1:")
    analisisCompletoDeMatrizDeAdyacencia(M1)
    print("\nAnalisis M2:")
    analisisCompletoDeMatrizDeAdyacencia(M2)
    print("\nAnalisis M3:")
    analisisCompletoDeMatrizDeAdyacencia(M3)


main()
    
