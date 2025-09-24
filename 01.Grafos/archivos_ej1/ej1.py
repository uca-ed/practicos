import csv

# Leer el archivo CSV y convertirlo a un grafo de nodos y sus vecindades
def cargar_grafo_csv_matriz(ruta_csv):
    P = []  # Lista de nodos
    E = {}  # Diccionario de vecindades

    with open(ruta_csv, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        
        # Cargar la matriz de adyacencia
        matrix = list(reader)
        N = len(matrix)  # Asumimos que la matriz es cuadrada (N x N)

        # Los nodos son simplemente los índices de la matriz (1 a N)
        P = [str(i+1) for i in range(N)]  # Nodos como "1", "2", ..., "N"

        # Convertimos la matriz en un diccionario de vecindades
        for i in range(N):
            # La i-ésima fila de la matriz representa los vecinos del nodo i+1
            E[P[i]] = [P[j] for j in range(N) if matrix[i][j] == '1']
    
    return {"P": P, "E": E}

# ----------------- Funciones de operadores -----------------

# a) Nodos minimales: sin vecinos a la izquierda
def minimales(G):
    P, E = G["P"], G["E"]
    # conjunto de todos los nodos que aparecen como destino
    con_entradas = {v for vecinos in E.values() for v in vecinos}
    return [v for v in P if v not in con_entradas]  # No hay nodos sin entradas

# b) Nodos maximales: sin vecinos a la derecha
def maximales(G):
    P, E = G["P"], G["E"]
    # Un nodo será máximo si no tiene vecinos que no sean él mismo (es decir, no tiene salidas a otros nodos)
    return [v for v in P if all(neighbor == v for neighbor in E[v])]  # Verificamos que todos los vecinos sean el nodo mismo

# c) Vecindad derecha de un nodo
def vecindad_derecha(G, x):
    return G["E"].get(x, [])

# d) Vecindad izquierda de un nodo
def vecindad_izquierda(G, x):
    return [u for u, vecinos in G["E"].items() if x in vecinos]

# ----------------- Uso / Pruebas -----------------

# Cargar el grafo desde el archivo CSV
estructura = cargar_grafo_csv_matriz('01.csv')

# Imprimo los nodos que tienen vecindad derecha
print("Nodos con vecindad derecha:", list(estructura["E"].keys()))

# Asegúrate de probar solo nodos válidos dentro del rango
nodo_prueba = "1"  # Cambia esto por cualquier nodo válido en el grafo
print(f"Vecindad derecha de '{nodo_prueba}':", estructura["E"].get(nodo_prueba, []))
print(f"Cardinalidad derecha de '{nodo_prueba}':", len(estructura["E"].get(nodo_prueba, [])))

# Imprimir la cantidad de nodos y los nodos minimales y máximos
print("Cantidad de nodos:", len(estructura["P"]))
print("Minimales:", minimales(estructura))  # Esto debería devolver una lista vacía
print("Maximales:", maximales(estructura))  # Todos los nodos son máximos

# Cambia el nodo por el que quieras probar (asegurándote de que está en el rango de nodos)
print(f"Vecindad derecha de {nodo_prueba}:", estructura["E"].get(nodo_prueba, []))
print(f"Cardinalidad derecha de {nodo_prueba}:", len(estructura["E"].get(nodo_prueba, [])))

# Ejemplo adicional con el nodo 3 (o cualquier nodo válido)
print("Vecinos de 3:", estructura["E"].get("3", []))  # Imprime los vecinos de 3
print("Cantidad de vecinos de 1:", len(estructura["E"].get("1", [])))  # Muestra cuántos vecinos tiene el nodo 1
