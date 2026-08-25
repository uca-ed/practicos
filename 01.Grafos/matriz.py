import csv

# ---------------------------------------------------------
# Elijo el archivo csv a usar. Si no escribo nada, usa 01.csv
# por defecto.
# ---------------------------------------------------------
archivo = input("Ingrese el archivo csv a usar (ej: 01.csv): ")
if archivo.strip() == "":
    archivo = "01.csv"

# ---------------------------------------------------------
# Lectura de la matriz de adyacencia desde el archivo csv
# Los nodos se identifican segun la posicion que ocupan en
# la matriz, empezando en 1 (fila/columna 0 -> nodo 1, etc)
# ---------------------------------------------------------
f = open(archivo)
lector = csv.reader(f)
matriz = []
for fila in lector:
    matriz.append([int(x) for x in fila])
f.close()

n = len(matriz)  # cantidad de nodos del grafo

print()
print("Archivo cargado:", archivo, "-", n, "nodos")
print()

# ---------------------------------------------------------
# c. Vecindad derecha de un nodo a
# Son todos los nodos b para los que existe una arista a -> b,
# es decir, los j tales que matriz[a-1][j] == 1
# ---------------------------------------------------------
a = 1  # nodo sobre el que se calculan las vecindades (se puede cambiar)

vecindad_derecha_a = []
for j in range(n):
    if matriz[a - 1][j] == 1:
        vecindad_derecha_a.append(j + 1)

print("Vecindad derecha de", a, ":", vecindad_derecha_a)
print("Cardinalidad vecindad derecha de", a, ":", len(vecindad_derecha_a))

# ---------------------------------------------------------
# d. Vecindad izquierda de un nodo a
# Son todos los nodos b para los que existe una arista b -> a,
# es decir, los i tales que matriz[i][a-1] == 1
# ---------------------------------------------------------
vecindad_izquierda_a = []
for i in range(n):
    if matriz[i][a - 1] == 1:
        vecindad_izquierda_a.append(i + 1)

print("Vecindad izquierda de", a, ":", vecindad_izquierda_a)
print("Cardinalidad vecindad izquierda de", a, ":", len(vecindad_izquierda_a))

# ---------------------------------------------------------
# a. Minimales del grafo
# Un nodo i es minimal si ningun otro nodo distinto de el
# llega hasta el, es decir, en su columna no hay ningun otro
# 1 aparte (eventualmente) del propio
# ---------------------------------------------------------
minimales = []
for i in range(n):
    es_minimal = True
    for k in range(n):
        if k != i and matriz[k][i] == 1:
            es_minimal = False
    if es_minimal:
        minimales.append(i + 1)

print("Minimales del grafo:", minimales)

# ---------------------------------------------------------
# b. Maximales del grafo
# Un nodo i es maximal si no llega a ningun otro nodo distinto
# de el, es decir, en su fila no hay ningun otro 1 aparte
# (eventualmente) del propio
# ---------------------------------------------------------
maximales = []
for i in range(n):
    es_maximal = True
    for k in range(n):
        if k != i and matriz[i][k] == 1:
            es_maximal = False
    if es_maximal:
        maximales.append(i + 1)

print("Maximales del grafo:", maximales)