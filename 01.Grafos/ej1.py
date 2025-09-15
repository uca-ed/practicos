# -- coding: utf-8 --
import json

# Abrir y cargar el archivo JSON
f = open('01.json', encoding='utf-8')
estructura = json.load(f)
f.close()   # cerramos apenas terminamos de leer

# Estructura esperada:
#   estructura["P"] : lista de nodos
#   estructura["E"] : diccionario nodo -> lista de vecinos (vecindad derecha)

# ----------------- Funciones de operadores -----------------


# a) Nodos minimales: sin vecinos a la izquierda
def minimales(G):
    P, E = G["P"], G["E"]
    # conjunto de todos los nodos que aparecen como destino
    con_entradas = {v for vecinos in E.values() for v in vecinos}
    return [v for v in P if v not in con_entradas]

# b) Nodos maximales: sin vecinos a la derecha
def maximales(G):
    P, E = G["P"], G["E"]
    return [v for v in P if not E.get(v, [])]

# c) Vecindad derecha de un nodo
def vecindad_derecha(G, x):
    return G["E"].get(x, [])

# d) Vecindad izquierda de un nodo
def vecindad_izquierda(G, x):
    return [u for u, vecinos in G["E"].items() if x in vecinos]

# ----------------- Uso / Pruebas -----------------

# Imprimo los nodos que tienen vecindad derecha
print("Nodos con vecindad derecha:", list(estructura["E"].keys()))

# Imprimo la vecindad y la cardinalidad derecha de 'a'
print("Vecindad derecha de 'a':", estructura["E"].get("a", []))
print("Cardinalidad derecha de 'a':", len(estructura["E"].get("a", [])))

print("Cantidad de nodos:", len(estructura["P"]))
print("Minimales:", minimales(estructura))
print("Maximales:", maximales(estructura))

# Cambiá 'a' por el nodo que quieras probar
nodo_prueba = "1"
#print("Vecindad derecha de '1':", estructura["E"].get("1", []))
print("Cardinalidad derecha de '1':", len(estructura["E"].get("1", [])))

print("Nodos:", len(estructura["P"]))        # te da 1999
print("Vecinos de 1:", estructura["E"]["1"]) # imprime todos los vecinos de 1
print("Cantidad de vecinos de 1:", len(estructura["E"]["1"]))  # 1999