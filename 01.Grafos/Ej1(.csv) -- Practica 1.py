import csv
archivo = input("Ingrese el archivo csv a usar (ej: 01.csv): ")
if archivo.strip() == "":
    archivo = "01.csv"
f = open(archivo)
lector = csv.reader(f)
matriz = []
for fila in lector:
    matriz.append([int(x) for x in fila])
f.close()
a = 1  
vecindad_derecha_a = []
for j in range(n):
    if matriz[a - 1][j] == 1:
        vecindad_derecha_a.append(j + 1)

print("Vecindad derecha de", a, ":", vecindad_derecha_a)
print("Cardinalidad vecindad derecha de", a, ":", len(vecindad_derecha_a))
vecindad_izquierda_a = []
for i in range(n):
    if matriz[i][a - 1] == 1:
        vecindad_izquierda_a.append(i + 1)

print("Vecindad izquierda de", a, ":", vecindad_izquierda_a)
print("Cardinalidad vecindad izquierda de", a, ":", len(vecindad_izquierda_a))
minimales = []
for i in range(n):
    es_minimal = True
    for k in range(n):
        if k != i and matriz[k][i] == 1:
            es_minimal = False
    if es_minimal:
        minimales.append(i + 1)

print("Minimales del grafo:", minimales)

maximales = []
for i in range(n):
    es_maximal = True
    for k in range(n):
        if k != i and matriz[i][k] == 1:
            es_maximal = False
    if es_maximal:
        maximales.append(i + 1)

print("Maximales del grafo:", maximales)
