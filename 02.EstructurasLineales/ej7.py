import json
import sys
from collections import deque

def preparar_estructuras(ruta_archivo):
    #abrimos y cargamos el archivo json
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
    except FileNotFoundError:
        print(f"error: no se encontro el archivo {ruta_archivo}")
        sys.exit(1)

    #extraemos los vertices y las conexiones
    nodos = set(datos.get("P", []))
    adyacencias = datos.get("E", {})
    #armamos el diccionario de grados de entrada arrancando todos en cero
    grados = {nodo: 0 for nodo in nodos}
    
    #recorremos las conexiones para sumar las dependencias correspondientes
    for origen, destinos in adyacencias.items():
        for destino in destinos:
            #sumamos una flecha entrante al destino si existe en nuestro conjunto
            if destino in grados:
                grados[destino] += 1
                
    return adyacencias, grados, nodos

def ejecutar_kahn(grafo, grados, nodos):
    #metemos a la cola los elementos que arrancan libres de prerequisitos
    cola = deque([n for n in nodos if grados[n] == 0])
    camino = [] 
    #procesamos cada elemento de la cola hasta vaciarla
    while cola:
        actual = cola.popleft()
        camino.append(actual)
        
        #restamos uno al grado de entrada de todos sus vecinos
        for vecino in grafo.get(actual, []):
            grados[vecino] -= 1          
            #agregamos el vecino a la cola si ya se liberaron sus dependencias
            if grados[vecino] == 0:
                cola.append(vecino)
                
    #comprobamos comparando longitudes que no hayan quedado ciclos atrapados
    if len(camino) != len(nodos):
        return None
        
    return camino

if __name__ == "__main__":
    #definimos el nombre del archivo local que contiene el grafo
    archivo_json = "grafo.json"
    
    #ejecutamos las funciones pasando los datos extraidos
    grafo_armado, grados_entrada, total_nodos = preparar_estructuras(archivo_json)
    resultado_final = ejecutar_kahn(grafo_armado, grados_entrada, total_nodos)
    
    #verificamos el retorno para mostrar el resultado por consola
    if resultado_final is None:
        print("se detecto un ciclo")
    else:
        print("orden topologico resultante:")
        print(" -> ".join(resultado_final))