import sys

def barrido_post_orden(arbol, r):
    S = [(0, 0)]
    aux = []
    while len(S) > 0:
        x, e = S.pop()
        if e == 0:
            S.append((x, 1))
            for i in range(r, 0, -1):
                if r*x+i <= len(arbol)-1:
                    S.append((r*x+i, 0))
        else:
            aux.append(arbol[x])
    return aux

if __name__ == "__main__":
    r = int(sys.argv[1])
    nombre_archivo = sys.argv[2]
    
    with open(nombre_archivo, 'r') as archivo:        APD = [int(linea.strip()) for linea in archivo]    
    resultado = barrido_post_orden(APD, r)
    
    for nodo in resultado:
        print(nodo)