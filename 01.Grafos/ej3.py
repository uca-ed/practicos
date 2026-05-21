import json
import os

def buscar_paso(grafo_E, inicio, fin):
    """
    Busca un camino entre dos nodos usando BFS.
    Retorna la lista de nodos si existe, de lo contrario None.
    """
    if inicio == fin:
        return [inicio]
    
    cola = [[inicio]]
    visitados = {inicio}
    
    while cola:
        camino = cola.pop(0)
        nodo_actual = camino[-1]
        
        if nodo_actual == fin:
            return camino
        
        # Usamos .get para que si el nodo no tiene salidas, no rompa el programa
        vecinos = grafo_E.get(nodo_actual, [])
        
        for vecino in vecinos:
            if vecino not in visitados:
                visitados.add(vecino)
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                cola.append(nuevo_camino)
    return None

# Lista con tus 6 archivos exactos
archivos = [
    "esDivisorDe-200.json",
    "esDivisorDe-2000.json",
    "esDivisorDe-20000.json",
    "multiplos200Ref.json",
    "multiplos2000Ref.json",
    "multiplos20000Ref.json"
]

# Definimos qué nodos queremos buscar (ajustalos según tu preferencia)
nodo_inicio = "2"
nodo_fin = "16"

print(f"INICIANDO BÚSQUEDA DE PASO DE '{nodo_inicio}' A '{nodo_fin}'")

for nombre_archivo in archivos:
    if os.path.exists(nombre_archivo):
        try:
            with open(nombre_archivo, 'r') as f:
                data = json.load(f)
            
            # Obtenemos la estructura de conexiones
            grafo_E = data.get('E', {})
            
            # Ejecutamos la búsqueda
            resultado = buscar_paso(grafo_E, nodo_inicio, nodo_fin)
            
            print(f"\nArchivo: {nombre_archivo}")
            if resultado:
                print(f"  Paso encontrado: {' -> '.join(resultado)}")
            else:
                print(f"  No existe un paso entre '{nodo_inicio}' y '{nodo_fin}' en este grafo.")
                
        except Exception as e:
            print(f"\n[!] Error al procesar {nombre_archivo}: {e}")
    else:
        print(f"\n[!] El archivo {nombre_archivo} no se encuentra en la carpeta.")
