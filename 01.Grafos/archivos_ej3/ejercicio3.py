""" 3. Implementar el algoritmo de obtención de paso de un nodo a otro de un grafo. 
    La aplicación debe soportar leer el grafo desde un archivo de disco 
    y la salida debe ser una secuencia con los nodos a recorrer para recrear el paso."""

import os 
import json


# funcion aux para revisar si un nodo ya esta en la lista de pares
def estaEnLista(lista, nodo):
    for n,_ in lista:
        if n==nodo:
            return True
    return False

def paso(grafo,s,t):
    if s==t:
        return [s]
    
    if s not in grafo or t not in grafo:
        return "No se encuentran en el grafo"
    
    OPEN=[(s,None)]
    CLOSED=[]

    while OPEN:
        z,y=OPEN.pop(0)
        CLOSED.append((z,y))
        
        if not estaEnLista(CLOSED,z):
            CLOSED.append((z,y))

        if t in grafo.get(z,[]):
            CLOSED.append((t,z))
            break

        for w in grafo.get(z,[]):
            if not estaEnLista(OPEN,w) and not estaEnLista(CLOSED,w):
                OPEN.append((w,z))

    camino=[]
    actual=t
    padres={nodo: padre for nodo, padre in CLOSED}
    
    
    if actual not in padres:
        return None
    
    while actual is not None:
        camino.insert(0,actual)
        actual=padres.get(actual)
    return camino



   
   
def main():
    #tienen que estar en la misma carpeta 
    base = os.path.dirname(__file__)
    nombre_archivo = "multiplos200Ref.json" 
    
    """todos los archivos json para probar de la carpeta son: 
        esDivisorDe-200.json, esDivisorDe-2000.json, esDivisorDe-20000.json,
        multiplos200Ref.json, multiplos2000Ref, multiplos20000Ref"""""
        
    
    ruta = os.path.join(base, nombre_archivo)

    f = open(ruta, encoding="utf-8")
    estructura = json.load(f)
    f.close()

    grafo = estructura['E']

    
    origen = input("Ingrese el nodo origen: ").strip()
    destino = input("Ingrese el nodo destino: ").strip()

    if origen not in grafo and origen.isdigit() and (int(origen) in grafo):
        origen = int(origen)
    if destino not in grafo and destino.isdigit() and (int(destino) in grafo):
        destino = int(destino)

    camino = paso(grafo, origen, destino)

    if camino is None:
        print(f"No existe un camino de {origen} a {destino}.")
    elif origen==destino:
        print(f"El origen es igual al destino: {origen} = {destino}.")
    else:
        print(f"Camino de {origen} a {destino}: {camino}")


if __name__ == "__main__":
    main()