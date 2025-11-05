import math 

def altura_sin_recorrido(arbol, r): 
    n = len(arbol) # Cantidad total de nodos del árbol
    if n==0:        # si non hay nodos, la altura es cero
        return 0
    

    '''
    aplicamos la formula matematica para estimar la altura con la cantidad de nodos y r. Con floor no contamos niveles incompletos. R seria el grado del arbol. 

    
    '''


    altura = math.floor(math.log((n * (r - 1)) + 1, r))
    return altura 

# ejemplo de uso:
arbol =  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
r =3  # grado del arbol ternario en este caso. 

print("Altura del arbol sobre arreglo de ejemplo: ", altura_sin_recorrido(arbol, r))

# El resultado deberia ser 2 pues el arbol es incompleto por lo que no incluimos niveles incompletos. 

# si usamos ceil() podemos incluir niveles incompletos, por lo que vamos a tener como resultado una altura de 3 

def altura_sin_recorrido_2(arbol, r): 
    n = len(arbol)
    if n==0:
        return 0
    altura = math.ceil(math.log((n * (r - 1)) + 1, r))
    return altura 

print("Altura del arbol sobre arreglo de ejemplo: ", altura_sin_recorrido_2(arbol, r))


def barridoPreorden(arbol, r, i=0):
    if i >= len(arbol): # caso base con indice invalido, retorna lista vacia
        return []
    
    resultado = [arbol[i]] # visitamos nodo actual raiz


    # para cada posible hijo de 1 a grado del arbol r 
    for k in range(1, r+1):
        hijo = r*i + k # formula para obtener indice del (k) eismo hijo
        if hijo < len(arbol): # verificamos que el hijo exista 
            resultado.extend(barridoPreorden(arbol, r, hijo))
            # llamamos recusrivamente al hijo
    
    return resultado # vamos retornando recorrido completo . 

print("Barrido preorden:", barridoPreorden(arbol, r))
# ➜ ['A', 'B', 'E', 'F', 'G', 'C', 'H', 'I', 'J', 'D']







