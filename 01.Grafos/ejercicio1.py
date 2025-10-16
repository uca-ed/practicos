import json

def leerjson():
    f = open(r"C:\Users\Fede\Documents\GitHub\practicos\01.Grafos\archivos_ej1\01.json")
    estructura = json.load(f)
    f.close()
    MJSON=[]
    f=0
    for i in estructura['P']:
        MJSON.append([])
        for j in estructura['P']:
            if j in estructura['E'][i]:
                MJSON[f].append(1)
            else:
                MJSON[f].append(0)
        f+=1
    return MJSON

def leer_csv(ruta):
    f=open(ruta,'r')
    M=[]
    while True:
        line=f.readline()
        if not line:
            break
        strline=line.strip().split(',')
        for i in range(0,len(strline)):
            strline[i]=int(strline[i])
        M.append(strline)
    return M

def vecindadDerecha(matriz, nodo):
    idx = nodo - 1
    vecinos = []
    for j in range(len(matriz)):
        if matriz[idx][j] == 1:
            vecinos.append(j+1)
    return vecinos

def vecindadIzquierda(matriz, nodo):
    idx = nodo - 1
    vecinos = []
    for i in range(len(matriz)):
        if matriz[i][idx] == 1:
            vecinos.append(i+1)
    return vecinos

def minimales_matriz(matriz):
    n = len(matriz)
    res = []
    for j in range(n):
        if all(matriz[i][j] == 0 for i in range(n)):
            res.append(j+1)
    return res

def maximales_matriz(matriz):
    n = len(matriz)
    res = []
    for i in range(n):
        if sum(matriz[i]) == 0:
            res.append(i+1)
    return res


def main():
    MJSON = leerjson()
    M1 = leer_csv(r"C:\Users\Fede\Documents\GitHub\practicos\01.Grafos\archivos_ej1\01.csv")
    M2 = leer_csv(r"C:\Users\Fede\Documents\GitHub\practicos\01.Grafos\archivos_ej1\02.csv")
    M3 = leer_csv(r"C:\Users\Fede\Documents\GitHub\practicos\01.Grafos\archivos_ej1\03.csv")
    M4 = leer_csv(r"C:\Users\Fede\Documents\GitHub\practicos\01.Grafos\archivos_ej1\04.csv")

    print("===== ARCHIVO 01.json =====")

    print("NODOS MINIMALES:", minimales_matriz(MJSON))
    print("NODOS MAXIMALES:", maximales_matriz(MJSON))
    print("\nVecindades en JSON:")
    for nodo in range(1, len(MJSON)+1):
        print(f"Nodo {nodo}: VD={vecindadDerecha(MJSON, nodo)}, VI={vecindadIzquierda(MJSON, nodo)}")

    print("\n===== ARCHIVO 01.csv =====")

    print("NODOS MINIMALES:", minimales_matriz(M1))
    print("NODOS MAXIMALES:", maximales_matriz(M1))
    for nodo in range(1, len(M1)+1):
        print(f"Nodo {nodo}: VD={vecindadDerecha(M1, nodo)}, VI={vecindadIzquierda(M1, nodo)}")

    print("\n===== ARCHIVO 02.csv =====")

    print("NODOS MINIMALES:", minimales_matriz(M2))
    print("NODOS MAXIMALES:", maximales_matriz(M2))
    for nodo in range(1, len(M2)+1):
        print(f"Nodo {nodo}: VD={vecindadDerecha(M2, nodo)}, VI={vecindadIzquierda(M2, nodo)}")

    print("\n===== ARCHIVO 03.csv =====")

    print("NODOS MINIMALES:", minimales_matriz(M3))
    print("NODOS MAXIMALES:", maximales_matriz(M3))
    for nodo in range(1, len(M3)+1):
        print(f"Nodo {nodo}: VD={vecindadDerecha(M3, nodo)}, VI={vecindadIzquierda(M3, nodo)}")
    print("\n===== ARCHIVO 04.csv =====")

    print("NODOS MINIMALES:", minimales_matriz(M4))
    print("NODOS MAXIMALES:", maximales_matriz(M4))
    for nodo in range(1, len(M4)+1):
        print(f"Nodo {nodo}: VD={vecindadDerecha(M4, nodo)}, VI={vecindadIzquierda(M4, nodo)}")





    print("INTEGRANTES GRUPO: JUAN FEDERICO ROSENFELD, IGNACIO GONZALEZ IÑIGO Y NICOLAS LUCINI")

main()