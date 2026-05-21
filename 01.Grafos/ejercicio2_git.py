import csv
def leer_csv(nombre_archivo):
    matriz = []
    with open(nombre_archivo, 'r') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            matriz.append([int(numero) for numero in fila])
    return matriz

#Propiedades

def es_reflexiva(matriz):
    #Todos los nodos deben tener un 1 en la diagonal (i, i)
    n = len(matriz)
    for i in range(n):
        if matriz[i][i] == 0:
            return False # Si encuentro un solo cero en la diagonal, ya no es reflexiva
    return True

def es_simetrica(matriz):
    #Si hay flecha de ida (i,j), DEBE haber de vuelta (j,i)
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            if matriz[i][j] == 1:
                if matriz[j][i] == 0:
                    return False # Hay ida pero no vuelta
    return True

def es_antisimetrica(matriz):
    #Si hay ida (i,j) y vuelta (j,i), entonces i y j deben ser el mismo nodo (rulo).
       
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            if i != j: # Evaluamos solo nodos distintos
                if matriz[i][j] == 1 and matriz[j][i] == 1:
                    return False 
    return True

def es_transitiva(matriz):
    #Si hay camino de i->j y de j->k, DEBE haber atajo directo i->k
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if matriz[i][j] == 1 and matriz[j][k] == 1:
                    if matriz[i][k] == 0:
                        return False 
    return True



def clasificar_grafo(matriz):
    reflexiva = es_reflexiva(matriz)
    simetrica = es_simetrica(matriz)
    antisimetrica = es_antisimetrica(matriz)
    transitiva = es_transitiva(matriz)
    
    print("--- Propiedades ---")
    print(f"Reflexiva: {reflexiva}")
    print(f"Simétrica: {simetrica}")
    print(f"Antisimétrica: {antisimetrica}")
    print(f"Transitiva: {transitiva}")
    
    print("\n--- Clasificación ---")
    if reflexiva and simetrica and transitiva:
        print("El grafo es una Relación de EQUIVALENCIA.")
    elif reflexiva and antisimetrica and transitiva:
        print("El grafo es un ORDEN PARCIAL.")
    else:
        print("El grafo no es ni Equivalencia ni Orden Parcial.")

mi_matriz = leer_csv('01.csv')
clasificar_grafo(mi_matriz)
