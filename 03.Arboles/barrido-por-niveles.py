import sys

grado = int(sys.argv[1])
if grado < 1:
    sys.exit("El grado debe ser mayor que cero")

arbol = []
archivo = open(sys.argv[2], "r")
for linea in archivo:
    arbol.append(int(linea.strip()))
archivo.close()

# El arreglo ya guarda los nodos en orden por niveles.
for valor in arbol:
    print(valor)
