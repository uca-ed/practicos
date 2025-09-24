import csv

def cargar_grafo_csv_matriz(ruta_csv):
    P = []  # Lista de nodos
    E = {}  # Diccionario de vecindades

    with open(ruta_csv, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        
        matriz = list(reader)
        num_nodos = len(matriz)

        P = [str(i+1) for i in range(num_nodos)]

        for i in range(num_nodos):
            E[P[i]] = [P[j] for j in range(num_nodos) if matriz[i][j] == '1']
    
    return {"P": P, "E": E}

def minimales(G):
    P, E = G["P"], G["E"]
    con_entradas = {v for vecinos in E.values() for v in vecinos}
    return [v for v in P if v not in con_entradas]

def maximales(G):
    P, E = G["P"], G["E"]
    return [v for v in P if all(vecino == v for vecino in E[v])]

def vecindad_derecha(G, nodo):
    return G["E"].get(nodo, [])

def vecindad_izquierda(G, nodo):
    return [u for u, vecinos in G["E"].items() if nodo in vecinos]



estructura = cargar_grafo_csv_matriz('01.csv')

print("Nodos con vecindad derecha:", list(estructura["E"].keys()))

nodo_prueba = "1"
print(f"Vecindad derecha de '{nodo_prueba}':", estructura["E"].get(nodo_prueba, []))
print(f"Cardinalidad derecha de '{nodo_prueba}':", len(estructura["E"].get(nodo_prueba, [])))

print("Cantidad de nodos:", len(estructura["P"]))
print("Minimales:", minimales(estructura))
print("Maximales:", maximales(estructura))

print(f"Vecindad derecha de {nodo_prueba}:", estructura["E"].get(nodo_prueba, []))
print(f"Cardinalidad derecha de {nodo_prueba}:", len(estructura["E"].get(nodo_prueba, [])))

print("Vecinos de 3:", estructura["E"].get("3", []))
print("Cantidad de vecinos de 1:", len(estructura["E"].get("1", [])))
