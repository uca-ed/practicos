import sys

def barrido_pre_orden(arbol, r):
    S = [0]
    aux = []
    while len(S) > 0:
        h = S.pop()
        aux.append(arbol[h])
        for i in range(r, 0, -1):
            if(r*h+i <= len(arbol)-1):
                S.append(r*h+i)  
    return aux

if __name__ == "__main__":
    r = int(sys.argv[1])
    nombre_archivo = sys.argv[2]
    
    with open(nombre_archivo, 'r') as archivo:        APD = [int(linea.strip()) for linea in archivo]    
    resultado = barrido_pre_orden(APD, r)
    
    for nodo in resultado:
        print(nodo)