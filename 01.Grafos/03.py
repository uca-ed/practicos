import json
import csv

def cargar_json(ruta_archivo):
    f = open(ruta_archivo)                       
    estructura = json.load(f)
    f.close()
    return estructura 



def paso_json(grafo, inicio, fin):
    visitados = []
    cola = [[inicio]]

    while len(cola) > 0:
        paso = cola.pop(0)
        nodo = paso[-1]

        if nodo == fin:
            return paso

        if nodo not in visitados:
            visitados.append(nodo)
            vecinos = grafo["E"].get(nodo,[])
            for vecino in vecinos:
                nuevo_paso = paso + [vecino]
                cola.append(nuevo_paso)

    return [] 



def main_3(arch):
    grafo = cargar_json("esDivisorDe-200.json")
    #como en todos los casos el grafo tiene multiplos y divisores, siempre el paso si existe va a ser directo

    inicio = input("Nodo de inicio: ")
    fin = input("Nodo de destino: ")

    paso = paso_json(grafo, inicio, fin)

    if paso:
        print("Hay paso entre", " , ".join(paso))
    else:
        print("No hay paso entre esos nodos.")

main_3('esDivisorDe-200.json')