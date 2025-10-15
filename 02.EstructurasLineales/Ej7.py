import json

def procesarGrafoJson(archivo):
    with open(archivo, "r") as f:
        grafo = json.load(f)

    visitado = []
    enCamino = []
    pila = []
    hayCiclo = [False]

    def dfs(nodo):
        if nodo in enCamino:
            hayCiclo[0] = True
            return
        if nodo in visitado:
            return
        enCamino.append(nodo)
        for vecino in grafo.get(nodo, []):
            dfs(vecino)
        enCamino.remove(nodo)
        visitado.append(nodo)
        pila.insert(0, nodo)

    for nodo in grafo:
        if nodo not in visitado:
            dfs(nodo)

    print(f"\nGrafo desde {archivo}:")
    for k, v in grafo.items():
        print(f"{k}: {v}")

    if hayCiclo[0]:
        print("El grafo es ciclico. No se puede generar un orden topologico.")
    else:
        print("Orden topologico:", pila)

# -------------------
# Main
# -------------------
def main():
    print("Grafo Aciclico 1")
    procesarGrafoJson("grafoA.json")

    print("\nGrafo Aciclico 2")
    procesarGrafoJson("grafoA2.json")

    print("\nGrafo Ciclico")
    procesarGrafoJson("grafoC.json")

main()