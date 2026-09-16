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
    minimal = -1

    for nodo in range(cantidad):
        if not visitados[nodo]:
            tiene_entrantes = False

            for origen in range(cantidad):
                if not visitados[origen] and matriz[origen][nodo] == 1:
                    tiene_entrantes = True
                    break

            if not tiene_entrantes:
                minimal = nodo
                break

    if minimal == -1:
        break

    orden.append(minimal)
    visitados[minimal] = True

if len(orden) == cantidad:
    print("T-Sort:", orden)
else:
    print("La estructura es cíclica")
