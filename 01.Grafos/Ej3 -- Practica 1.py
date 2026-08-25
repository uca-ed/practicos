import json
archivo = input("Ingrese el archivo json a usar (ej: esDivisorDe-200.json): ")
if archivo.strip() == "":
    archivo = "esDivisorDe-200.json"

f = open(archivo)
estructura = json.load(f)
f.close()

nodos = estructura['P']
arcos = estructura['E']

print()
print("Archivo cargado:", archivo, "-", len(nodos), "nodos")
print()

origen = input("Nodo de origen: ")
destino = input("Nodo de destino: ")

visitados = set()
visitados.add(origen)
padre = {}
cola = [origen]
indice = 0
encontrado = (origen == destino)

while indice < len(cola) and not encontrado:
    actual = cola[indice]
    indice = indice + 1
    vecinos = arcos.get(actual, [])
    for vecino in vecinos:
        if vecino not in visitados:
            visitados.add(vecino)
            padre[vecino] = actual
            cola.append(vecino)
            if vecino == destino:
                encontrado = True
                break
if encontrado:
    camino = [destino]
    actual = destino
    while actual != origen:
        actual = padre[actual]
        camino.append(actual)
    camino.reverse()
    print("Camino de", origen, "a", destino, ":", camino)
    print("Cantidad de pasos:", len(camino) - 1)
else:
    print("No existe un camino de", origen, "a", destino)