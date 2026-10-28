import sys

def leer_arbol_desde_archivo(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='utf-16') as archivo:
        arbol = [int(linea.strip()) for linea in archivo]
    return arbol


def barrido_por_niveles(arbol, r):
    visitados = []
    if (len(arbol) == 0):
        return visitados

    Q = [0]
    while (Q != []):
        x = Q.pop(0)
        visitados.append(arbol[x])
        for i in range(1, r + 1):
            hijo = r * x + i
            if (hijo < len(arbol)):
                Q.append(hijo)
    return visitados

def main():
    r = int(sys.argv[1])
    arbol = leer_arbol_desde_archivo(sys.argv[2])
    
    resultado_barrido = barrido_por_niveles(arbol, r)
    for i in range(len(resultado_barrido)):
        print(f"{resultado_barrido[i]}")

if __name__ == "__main__":
    main()