import sys


def leer_arbol(nombre_archivo):
    arbol = []
    archivo = open(nombre_archivo)
    for linea in archivo:
        linea = linea.strip()
        if linea != "":
            arbol.append(int(linea))
    archivo.close()
    return arbol


def preorden(arbol, g):
    n = len(arbol)
    if n == 0:
        return
    pila = []
    pila.append(0)
    while len(pila) > 0:
        i = pila.pop()
        print(arbol[i])
        j = g
        while j >= 1:
            hijo = g * i + j
            if hijo < n:
                pila.append(hijo)
            j = j - 1

def main():
    grado = int(sys.argv[1])   
    nombre_archivo = sys.argv[2]      
    arbol = leer_arbol(nombre_archivo)
    preorden(arbol, grado)

if __name__ == "__main__":
    main()
