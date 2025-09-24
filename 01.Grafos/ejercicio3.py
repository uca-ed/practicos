import json
import sys

def cargar_grafo(nombre):
    with open(nombre, "r", encoding="utf-8") as f:
        data = json.load(f)

    nodos = data["P"]
    aristas = data["E"]

    grafo = {n: [] for n in nodos}

    # aristas es un diccionario
    for u, vecinos in aristas.items():  
        for v in vecinos:
            if v in nodos:
                grafo[u].append(v)
            
    return grafo

def encolar(cola,elem):
    cola.append(elem)

def desencolar(cola):
    return cola.pop(0)

def buscar_camino(grafo, inicio, fin):
    cola=[]
    encolar(cola,[inicio])
    visitados={nodo: False for nodo in grafo}
    visitados[inicio]= True
    while cola:
        camino= desencolar(cola)
        nodo=camino[-1]
        if nodo == fin:
            return camino
        for vecino in grafo[nodo]:
            if not visitados[vecino]:
                visitados[vecino]= True
                nuevo_camino=camino+[vecino]
                encolar(cola,nuevo_camino)
    return []

def main():
    nombre_archivo = "archivos_ej3/multiplos200Ref.json"  # mismo directorio que el .py
    grafo = cargar_grafo(nombre_archivo)
    print("Nodos disponibles: ",list(grafo.keys()))
    inicio= input("Nodo de inicio: ")
    fin= input("Nodo de fin: ")
    if inicio not in grafo or fin not in grafo:
        print("Error: nodos invalidos. ")
        return
    camino=buscar_camino(grafo, inicio, fin)
    if camino:
        print("Camino encontrado: ")
        for nodo in camino:
            print(nodo)
    else:
        print("No existe camino entre ", inicio, " y ", fin)
if __name__ == "__main__":
    main()



