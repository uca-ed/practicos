#5) T-Sort
def leer_grafo(nombre_archivo):
    grafo={}
    with open(nombre_archivo,'r') as f:
        for linea in f:
            partes=linea.strip().split()
            if len(partes)==2:
                origen,destino=partes
                if origen not in grafo:
                    grafo[origen]=[]
                if destino not in grafo:
                    grafo[destino]=[]
                grafo[origen].append(destino)
    return grafo
def T_Sort(grafo):
    grado={}
    for nodo in grafo:
        grado[nodo]=0
    for nodo in grafo:
        for vecino in grafo[nodo]:
            grado[vecino]+=1
    cola= []
    for nodo in grafo:
        if grado[nodo] ==0:
            cola.append(nodo)
    orden=[]
    while cola:
        actual=cola.pop(0)
        orden.append(actual)
        for vecino in grafo.get(actual, []):
            grado[vecino]-=1
            if grado[vecino]==0:
                cola.append(vecino)
    if len(orden) !=len(grafo):
        print("La estructura es ciclica (no se puede realizar T-Sort).")
        return None
    return orden
def procesar_tsort(nombre_archivo):
    try:
        grafo = leer_grafo(nombre_archivo)
        orden = T_Sort(grafo)
        if orden:
            print("Orden topológico:", orden)
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no se encontró.")

if __name__ == "__main__":
    procesar_tsort("grafo.txt")
