import json
from collections import deque

def cargar_grafo(ruta_archivo):
    # Esta es la forma estándar de leer JSON en Python.
    # Cuando subas la foto con el tip del profe, lo ajustamos si hace falta.
    with open(ruta_archivo, 'r', encoding='utf-8') as f:
        datos = json.load(f)
    return datos

def encontrar_camino_bfs(grafo, nodo_inicio, nodo_destino):
    # Extraemos el diccionario de enlaces (aristas) y la lista de nodos
    enlaces = grafo.get("E", {})
    nodos_validos = set(grafo.get("P", []))

    # Validamos que los nodos existan en el grafo
    if str(nodo_inicio) not in nodos_validos or str(nodo_destino) not in nodos_validos:
        print("Error: Uno o ambos nodos no existen en el grafo.")
        return None

    # Si el inicio y destino son el mismo
    if nodo_inicio == nodo_destino:
        return [nodo_inicio]

    # Cola para BFS: guarda tuplas con el formato (nodo_actual, [camino_hasta_aca])
    cola = deque([(str(nodo_inicio), [str(nodo_inicio)])])
    visitados = set([str(nodo_inicio)])

    while cola:
        nodo_actual, camino = cola.popleft()

        # Obtenemos los vecinos a los que este nodo apunta
        vecinos = enlaces.get(nodo_actual, [])
        
        for vecino in vecinos:
            # Si encontramos el destino, devolvemos el camino sumando este último salto
            if vecino == str(nodo_destino):
                return camino + [vecino]
            
            # Si no es el destino y no lo visitamos, lo agregamos a la cola
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append((vecino, camino + [vecino]))

    return None # Si se vacía la cola y no retornó nada, no hay camino posible

# --- Bloque principal de ejecución ---
if __name__ == "__main__":
    archivo_json = 'esDivisorDe-200.json'
    
    try:
        mi_grafo = cargar_grafo(archivo_json)
        
        # Probamos con dos nodos. Cambiá estos valores para testear.
        # Por ejemplo, en este grafo "2" es divisor de "4", y "4" de "12".
        inicio = "2"
        destino = "48"
        
        camino = encontrar_camino_bfs(mi_grafo, inicio, destino)
        
        if camino:
            print(f"Camino encontrado de {inicio} a {destino}:")
            # Unimos la lista con flechas para que se vea bien la secuencia
            print(" -> ".join(camino))
        else:
            print(f"No hay camino posible entre {inicio} y {destino}.")
            
    except FileNotFoundError:
        print(f"No se encontró el archivo {archivo_json}. Asegurate de que esté en la misma carpeta.")
