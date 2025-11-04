import math

def alturaArbol(arr):
    grado = arr[0]                #         r
    cantNodos = len(arr[1])       #        |P|
    
    var = 1+cantNodos*(grado-1)   #     1+|P|(r-1)    
    altura = math.log(var,grado)  # log(r)[1+|P|(r-1)]

    return math.ceil(altura)

def preorden(arr):
    grado = arr[0]
    nodos = arr[1]
    resultado = []

    def recorrer(i):
        if i < len(nodos):
            resultado.append(nodos[i])
            for k in range(1, grado + 1):
                hijo = grado * i + k
                recorrer(hijo)

    recorrer(0)
    return resultado


def main():
    # ARBOL = [grado, array nodos]
    arbol1 = [2,[10, 5, 20, 3, 7, 15, 25]]
    print("Arbol 1 tiene una altura de: ",alturaArbol(arbol1))
    print("Recorrido Pre-Orden Arbol 1: ",preorden(arbol1))
    
    print("="*70)
    
    arbol2 = [3,['A', 'B', 'C', 'D', 'E', 'F', 'G']]
    print("Arbol 2 tiene una altura de: ",alturaArbol(arbol2))
    print("Recorrido Pre-Orden Arbol 2: ",preorden(arbol2))
    
    print("="*70)
    
    arbol3 = [4,[1, 2, 3, 4, 5, 6, 7, 8, 9]]
    print("Arbol 3 tiene una altura de: ",alturaArbol(arbol3))
    print("Recorrido Pre-Orden Arbol 3: ",preorden(arbol3))
    
    print("="*70)
    
    arbol4 = [2,[10, 5, 20, 3, 7, 15]]
    print("Arbol 4 (binario incompleto) tiene una altura de: ",alturaArbol(arbol4))
    print("Recorrido Pre-Orden Arbol 4: ",preorden(arbol4))
    
main()