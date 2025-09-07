import json


print("===== ARCHIVO JSON =====")
f = open(r"C:\Users\Fede\Documents\GitHub\practicos\01.Grafos\archivos_ej1\01.json")

estructura = json.load(f)

print("VECINDAD DERECHA DEL NODO 1500:")
print(estructura['E']["1500"])

print("VECINDAD IZQUIERDA DEL NODO 1500:")
vecIzq = []
for v in estructura['E']:                
    for u in estructura['E'][v]:             
        if u == "1500":      
            vecIzq.append(v)
print(vecIzq )

# Minimales del grafo son los vertices sin aristas de entrada
nodosMinimales = []
for v in estructura['E']:                 # recorro cada nodo
    es_minimal = True
    for u in estructura['E']:             # miro todos los demás
        if v in estructura['E'][u]:       # si alguien apunta a v
            es_minimal = False
            break
    if es_minimal:
        nodosMinimales.append(v)

print("NODOS MINIMALES: ")
print(nodosMinimales)

# Maximales del grafo son los vertices sin aristas de salida
nodosMaximales = []
for i in estructura['E']:        #recorro cada nodo
    if len(estructura['E'][i]) == 0:   #si la vecindad derecha del nodo es cero => es maximal
        nodosMaximales.append(i)

print("NODOS MAXIMALES: ")
print(nodosMaximales)

f.close()
print("===== FIN ARCHIVO JSON =====")
print("\n")
print("===== ARCHIVO CSV =====")

matriz = []
with open(r"C:\Users\Fede\Documents\GitHub\practicos\01.Grafos\archivos_ej1\02.csv", encoding="utf-8") as f:
    for linea in f:
        # Elimino salto de línea y espacios
        linea = linea.strip()
        if not linea:   # si la línea está vacía, la salto
            continue
        # Divido por comas y convierto cada valor a entero
        fila = [int(x) for x in linea.split(",")]
        matriz.append(fila)

print("Matriz leida:")
for fila in matriz:  
    print(fila)


print("VECINDAD DERECHA DE CADA NODO")

def vecindadDerecha(nodo):
    idx = nodo - 1
    vecinos = []
    for j in range(len(matriz)):
        if matriz[idx][j] == 1:
            vecinos.append(j+1)
    return vecinos

print("VECINDAD DERECHA DE NODO 1:", vecindadDerecha(1))
print("VECINDAD DERECHA DE NODO 2:", vecindadDerecha(2))
print("VECINDAD DERECHA DE NODO 3:", vecindadDerecha(3))
print("VECINDAD DERECHA DE NODO 4:", vecindadDerecha(4))
print("VECINDAD DERECHA DE NODO 5:", vecindadDerecha(5))
print("VECINDAD DERECHA DE NODO 6:", vecindadDerecha(6))




print("VECINDAD IZQUIERDA DE CADA NODO")
def vecindadIzquierda(nodo):
    idx = nodo - 1
    vecinos = []
    i=0
    while i < len(matriz):
        if matriz[i][idx] == 1:
            vecinos.append(i+1)
        i+=1
    return vecinos

print("VECINDAD IZQUIERDA DE NODO 1:", vecindadIzquierda(1))
print("VECINDAD IZQUIERDA DE NODO 2:", vecindadIzquierda(2))
print("VECINDAD IZQUIERDA DE NODO 3:", vecindadIzquierda(3))
print("VECINDAD IZQUIERDA DE NODO 4:", vecindadIzquierda(4))
print("VECINDAD IZQUIERDA DE NODO 5:", vecindadIzquierda(5))


def minimales_matriz(matriz):
    n = len(matriz)
    res = []
    for j in range(n):
        if all(matriz[i][j] == 0 for i in range(n)):
            res.append(j+1)
    return res

def maximales_matriz(matriz):
    n = len(matriz)
    res = []
    for i in range(n):
        if sum(matriz[i]) == 0:
            res.append(i+1)
    return res

print("NODOS MINIMALES:", minimales_matriz(matriz))
print("NODOS MAXIMALES:", maximales_matriz(matriz))




print("===== FIN ARCHIVO CSV =====")
