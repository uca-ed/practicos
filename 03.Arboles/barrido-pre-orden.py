import sys 

def leer_arbol_desde_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        arbol = [int(linea.strip()) for linea in archivo]
    return arbol

def barrido_pre_orden(arbol, r, index=0):
    S = [0]
    while S:
        x = S.pop()
        print(arbol[x])
        for i in range(r,0,-1):
            hijo = r * x + i
            if hijo < len(arbol):
                S.append(hijo)

def main():
    r = int(sys.argv[1])
    arbol = leer_arbol_desde_archivo((sys.argv[2]))

    barrido_pre_orden(arbol, r)
main()
