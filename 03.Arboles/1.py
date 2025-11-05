import math

def obtenerAlturaDesdeArreglo(arreglo, k):
    n = len(arreglo)
    if n == 0:
        return -1 # Árbol vacío
    altura = math.ceil(math.log(n, k)) 
    
    return altura

def visitar(nodo):
    print(nodo,end="  ")

def barridoPreOrder(arreglo,k):
    S=[]
    S.append(0) 

    while len(S)>0:
        indiceActual=S.pop()
        if indiceActual < len(arreglo):
            visitar(arreglo[indiceActual])
        else:
            continue
        
        for i in reversed(range(1,k+1)):
                indiceHijo=k*indiceActual+i
                if indiceHijo < len(arreglo):
                    S.append(indiceHijo)



def main():
    print(f"ARBOL TERNARIO 3 NIVELES LLENO")
    ArbolTernario3 = [i for i in range(13)] # como tiene 3 niveles, es 1+3+9=13
    k = 3
    print(f"Altura: {obtenerAlturaDesdeArreglo(ArbolTernario3, k)}")


    print(f"ARBOL BINARIO 5 NIVELES LLENO")
    ArbolBinario5 = [i for i in range(21)] # como tiene 5 niveles, es 1+2+4+8+16=21
    k = 5
    print(f"Altura: {obtenerAlturaDesdeArreglo(ArbolBinario5, k)}")

    print(f"\n\nPREORDER: ARBOL BINARIO 3 NIVELES LLENO")    
    arbolBinarioPREORDER = ['A', 'B', 'C', 'D', 'E', 'F','G']
    # esperado: A, B, D, E, C, F
    barridoPreOrder(arbolBinarioPREORDER,2)

    
    print(f"\n\nPREORDER: ARBOL BINARIO 3 NIVELES")
    arbolTernarioPREORDER = ['10', '20', '30', '40', '50', '60']
    # esperado: 10 20 50 60 30 40
    
    barridoPreOrder(arbolTernarioPREORDER, 3)

if __name__=="__main__":
    main()