import csv
from collections import deque, defaultdict

def cargar_grafo_csv_aristas(ruta_csv):
    E = defaultdict(list)
    nodos = set()

    with open(ruta_csv, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader, None)
        for fila in reader:
            if len(fila) < 2:
                continue
            origen, destino = fila[0].strip(), fila[1].strip()
            E[origen].append(destino)
            nodos.update([origen, destino])

    return {"P": list(nodos), "E": dict(E)}

def t_sort(G):
    P = G["P"][:]
    E = {k: v[:] for k, v in G["E"].items()} 
    ST = []  
    indegree = {n: 0 for n in P}
    for vecinos in E.values():
        for v in vecinos:
            indegree[v] += 1

    Q = deque([n for n in P if indegree[n] == 0])

    while Q:
        X = Q.popleft()
        ST.append(X)
        P.remove(X)

        for vecino in E.get(X, []):
            indegree[vecino] -= 1
            if indegree[vecino] == 0:
                Q.append(vecino)

        E.pop(X, None)

    if P:
        print("El grafo es cíclico, no se puede realizar T-Sort.")
        ciclo = encontrar_ciclo(G["E"])
        if ciclo:
            print("Ciclo encontrado:", " -> ".join(ciclo))
        return None
    else:
        print("Orden topológico:", ST)
        return ST


def encontrar_ciclo(E):
    color = {u: 0 for u in E}  
    padre = {}

    def dfs(u):
        color[u] = 1
        for v in E.get(u, []):
            if color[v] == 0:
                padre[v] = u
                ciclo = dfs(v)
                if ciclo:
                    return ciclo
            elif color[v] == 1:
                ciclo = [v]
                x = u
                while x != v:
                    ciclo.append(x)
                    x = padre[x]
                ciclo.append(v)
                ciclo.reverse()
                return ciclo
        color[u] = 2
        return None

    for nodo in E:
        if color[nodo] == 0:
            padre[nodo] = None
            ciclo = dfs(nodo)
            if ciclo:
                return ciclo
    return None


def main():

    print("\nEjemplo 1--")
    # Pruebas
    estructura = cargar_grafo_csv_aristas("./grafo_dag.csv")
    t_sort(estructura)

    print("\nEjemplo 2--")
    estructura = cargar_grafo_csv_aristas("./grafo_ciclo.csv")
    t_sort(estructura)

print("\nEjercicio 7 - tsort 2")
main()
print()