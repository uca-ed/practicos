archivo = open("grafo.txt", "r")
cantidad = int(archivo.readline())

matriz = []
for i in range(cantidad):
    matriz.append([0] * cantidad)

for linea in archivo:
    origen, destino = linea.split()
    matriz[int(origen)][int(destino)] = 1
archivo.close()

visitados = [False] * cantidad
orden = []

while len(orden) < cantidad:
    pendientes = []
    for nodo in range(cantidad):
        if not visitados[nodo]:
            pendientes.append(nodo)

    minimales = []
    for nodo in pendientes:
        tiene_entrantes = False
        for origen in pendientes:
            if matriz[origen][nodo] == 1:
                tiene_entrantes = True
                break

        if not tiene_entrantes:
            minimales.append(nodo)

    if len(minimales) == 0:
        break

    # Marcamos despues de encontrar todos los minimales de esta iteracion.
    for nodo in minimales:
        orden.append(nodo)
        visitados[nodo] = True

if len(orden) == cantidad:
    print("Sort topologico:", orden)
else:
    print("El grafo tiene un ciclo")
