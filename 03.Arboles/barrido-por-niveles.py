import sys

def barrido_por_niveles(arbol, r):
    Q = [0]
    aux = []
    while len(Q) > 0:
        h = Q.pop(0)
        aux.append(arbol[h])
        for i in range(1, r + 1):
            if r*h+i <= len(arbol)-1:
                Q.append(r*h+i)
    return aux

if __name__ == "__main__":
    r = int(sys.argv[1])
    nombre_archivo = sys.argv[2]
    
    with open(nombre_archivo, 'r') as archivo:
        APD = [int(linea.strip()) for linea in archivo]
        
    resultado = barrido_por_niveles(APD, r)
    
    for nodo in resultado:
        print(nodo)