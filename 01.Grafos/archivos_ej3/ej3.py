import json
from collections import deque

def cargarGrafo(ruta_json):
    f=open(ruta_json, "r")
    estructura=json.load(f)
    return estructura["E"]

def buscarPaso(E, s, t): #Busqueda de Paso
    openLst=deque([(s, None)])
    closedLst=[]
    padre={s: None}
    while openLst!=None:
        z, y = openLst.popleft()
        closedLst.append((z, y))
        
        if z in E:
            camino=E[z]
        else:
            camino=[]
        if t in camino:
            padre[t]=z
            return reconstruirCamino(padre, t)
        
        for nodoPrimero in openLst:
            n=nodoPrimero[0]
            openLst.add(n)
        for nodoPrimero in closedLst:
            n=nodoPrimero[0]
            closedLst.add(n)
        for w in E.get(z, []):
            if w not in openLst and w not in closedLst and w not in padre:
                padre[w] = z
                openLst.append((w, z))
    return None

def reconstruirCamino(padre,t):
    camino = [t]
    while padre[camino[-1]] is not None:
        camino.append(padre[camino[-1]])
    camino.reverse()
    return camino

def main():
    grafo=cargarGrafo("esDivisorDe-200.json")
    s, t="1", "192" #Sea s el nodo inicial y t el final
    camino = buscarPaso(grafo, s, t)
    if camino:
        print("Secuencia de nodos para recrear el paso:")
        print(" -> ".join(camino))
    else:
        print(f"No existe camino desde "+s+" hasta"+t)
main()