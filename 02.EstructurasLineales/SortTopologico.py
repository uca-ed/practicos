import json

def sortTopologico(grafo):
    gradoDeCadaNodo = {node: 0 for node in grafo} #Creo un dicionario por cada nodo en donde
    #inicialmente cada grado del nodo es cero. Grado nodo = cantidad de entradas al nodo
    
    for node in grafo:#Recorro nodo por nodo en el grafo
        for vecino in grafo[node]:
            gradoDeCadaNodo[vecino] += 1 #Por cada uno de los vecinos del nodo en el que estoy, entro al diccionario de
            #grados del VECINO y sumo uno.
            
    queue = [node for node in grafo if gradoDeCadaNodo[node] == 0] #Creo una cola para todos los nodos con grado
    #uno ya que son los que tengo que ir sacando
    
    sort = [] #Las lista con los nodos que voy a devolver una vez terminado el algoritmo
    
    while queue: #Mientras la cola no este vacia
        node = queue.pop(0) #Saco el primer elemento de la cola (nodo con grado cero)
        sort.append(node) #Lo guardo en la sita de sort que luego retornare
        
        for vecino in grafo.get(node, []): #Por cada vecino de cada grafo
            gradoDeCadaNodo[vecino] -= 1 #Le saco un grado, pues el nodo que elimine ya  no apuanta a el
            if gradoDeCadaNodo[vecino] == 0:#Si luego de sacar un nodo alguno de los vecinos llego a tener el grado en 0
                #lo meto en la cola para ser eliminado
                queue.append(vecino)
    
    # Una vez que termino el ciclo tengo que comprobar que no halla sido ciclico
    if len(sort) == len(grafo): #Si el largo de la lista que devuelvo es mayor a la cantidad de nodos del
        #grafo hay un error pues se repitio un nodo habiendo asi un ciclo
        return sort
    else:
        return None #Esto es para que si hay ciclo pueda detectarlo y expresarlo por consola

if __name__ == "__main__":
    with open('esDivisorDe-200.json', 'r') as arch:
        datos = json.load(arch)
    
    # Crear el grafo a partir de las aristas, uso un dicionario con la clave siendo el nodo el su contenido una lista de los vecinos
    
    grafo = {}
    for nodo in datos['P']:#Recorro cada nodo
        vecinos = datos['E'].get(nodo, []) #Tomo  los vecinos
        grafo[nodo] = vecinos
    
    sort = sortTopologico(grafo)
    if sort:
        print("Ordenamiento topológico:", sort)
    else:
        print("Hay ciclo, no cumple 1 condicion para ordenamiento topologico")
