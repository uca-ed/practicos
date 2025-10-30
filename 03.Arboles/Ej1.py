import math

def altura_arbol(arbol, r):
    return math.ceil(math.log(len(arbol) * (r - 1) + 1, r))-1

def preorden(arreglo, r,):
    pila = [0]  # índice de la raíz

    while pila:
        i = pila.pop()
        print(arreglo[i], end='  ') # Visito el nodo

        # Agregar hijos en orden inverso (derecha → izquierda)
        hijos = []
        for k in range(r): # range(r)=grado del arbol
            hijo = r * i + 1 + k # La vecindad derecha arranca en r*i+1
            if hijo < len(arreglo):
                hijos.append(hijo)
        # Invertimos para que el izquierdo se procese primero
        pila.extend(reversed(hijos))
        

def main():
    arbol_binario = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    r_bin=2
    arbol_ternario = ['A','B','C','D','E','F','G','H','I','J','K','L','M']
    r_ter = 3
    print(f"La altura del arbol binario es: {altura_arbol(arbol_binario,r_bin)}")
    print(f"La altura del arbol ternario es: {altura_arbol(arbol_ternario,r_ter)}")
    print("Preorden del arbol binario:")
    preorden(arbol_binario,r_bin)   
    print() #Para insertar un \n
    print("Preorden del arbol ternario:")
    preorden(arbol_ternario,r_ter)   
main()