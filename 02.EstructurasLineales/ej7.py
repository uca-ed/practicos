def leerGrafo(nombreArchivo):
    grafo = []
    with open(nombreArchivo, "r") as f:
        for linea in f:
            origen, destino = linea.strip().split()
            grafo.append([origen, destino])
    return grafo


def Tsort(grafo):
    grafores = grafo.copy()
    orden = []

    while True:
        origenes = [r[0] for r in grafores]
        destinos = [r[1] for r in grafores]

        sin_predecesor = [n for n in origenes if n not in destinos]

        if not sin_predecesor:
            if grafores:
                print("El grafo es cíclico, no se puede hacer T-Sort.")
            break

        orden.extend(sin_predecesor)
        grafores = [r for r in grafores if r[0] not in sin_predecesor]

        if not grafores:
            for d in destinos:
                if d not in orden:
                    orden.append(d)
            break

    ordenres=[]
    for nodo in orden:
        if(not nodo in ordenres):
            ordenres.append(nodo)

    print(f"Orden topológico: {ordenres}")
    return ordenres


def main():
    grafo = leerGrafo("grafo.txt")
    print(f"Grafo original = {grafo}")
    Tsort(grafo)


main()