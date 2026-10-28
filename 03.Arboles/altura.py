import sys

grado = int(sys.argv[1])
if grado < 1:
    sys.exit("El grado debe ser mayor que cero")

arbol = []
archivo = open(sys.argv[2], "r")
for linea in archivo:
    arbol.append(int(linea.strip()))
archivo.close()

# Contamos niveles sin recorrer los nodos del arbol.
altura = 0
posiciones = 0
nodos_del_nivel = 1

while posiciones < len(arbol):
    posiciones = posiciones + nodos_del_nivel
    nodos_del_nivel = nodos_del_nivel * grado
    altura = altura + 1

print(altura)
