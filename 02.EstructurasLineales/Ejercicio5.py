import json

def T_Sort(Q,gradoEntrada,P,E):
    ST = [] 
    while (len(Q) != 0 ): 
        T = Q.pop(0) #saco el elemento en la primera posicion pq trabajo con colas (FIFO)
        ST.append(T)
        for vecino in E[T]: 
            gradoEntrada[vecino] -=1
            if gradoEntrada[vecino] == 0: 
                Q.append(vecino)

    if len(ST) == len(P): 
        return ST 
    return "Hay ciclo"

def funcion_auxiliar(Q,gradoEntrada,P,E): 
    for nodo in P: #recorro el grafo y en el diccionario guardo cuantos grados de entrada tiene 
            gradoEntrada[nodo] = 0
    
    for nodo in E: 
        for vecino in E[nodo]: 
            gradoEntrada[vecino] +=1

    #meto todos los minimales a Q
    for nodo in gradoEntrada: 
        if gradoEntrada[nodo] == 0: 
            Q.append(nodo)



def main(): 
    with open("archivo.json") as f:
        datos = json.load(f)

    P = datos["P"]   # lista de nodos
    E = datos["E"]   # diccionario nodo (lista de vecinos)

    Q=[]
    gradoEntrada = {}

    funcion_auxiliar(Q,gradoEntrada,P,E)
    print("T-SORT: ",T_Sort(Q,gradoEntrada,P,E))

main()

    

