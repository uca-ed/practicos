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


def simetrico(arbol, i):
    n = len(arbol)
    pila=[]
    i = 0
    while(i<n or len(pila)>0):
        while(i<n):
            pila.append(i)
            i=2*i+1 #hijo izquierdo
        i=pila.pop()
        print(arbol(i))
        i=2*i+2 #hijo derecho del nodo que imprimi, ya me imprimi a mi mismo le toca a mi derecho

def main():
    nombre_archivo = sys.argv[1]       
    arbol = leer_arbol(nombre_archivo)
    simetrico(arbol, 0)              

if __name__ == "__main__":
    main()
