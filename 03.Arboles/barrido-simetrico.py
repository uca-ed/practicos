import sys

def barrido_simetrico(arbol):
    r = 2 
    S = [(0, 0)]
    aux = []
    while len(S) > 0:
        x, e = S.pop()
        if e == 0:
            S.append((x, 1))
            if r*x+1 <= len(arbol)-1:
                S.append((r*x+1, 0))
        else:
            aux.append(arbol[x])
            if r*x+2 <= len(arbol)-1:
                S.append((r*x+2, 0))
    return aux

if __name__ == "__main__":
    nombre_archivo = sys.argv[1]
    
    with open(nombre_archivo, 'r') as archivo:
        arbol_binario = [int(linea.strip()) for linea in archivo]
        
    resultado = barrido_simetrico(arbol_binario)
    
    for nodo in resultado:
        print(nodo)