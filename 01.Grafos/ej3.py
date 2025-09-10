import argparse
import json
from collections import deque
from typing import List, Dict, Optional


class GrafoLista:
    """Representación liviana por listas de adyacencia.

    Formato de entrada (JSON): {"P": [...], "E": { nodo: [sucesores] }}

    Elegimos listas (o sets) para sucesores. Aquí mantenemos listas (tal cual vienen)
    y además un set por nodo para membership O(1) si se necesitara (no imprescindible
    para BFS). Se prioriza bajo costo de carga para grafos grandes.
    """

    def __init__(self, nodos: List[str]):
        self.nodos = nodos
        self.idx: Dict[str, int] = {v: i for i, v in enumerate(nodos)}
        self.sucesores: List[List[str]] = [[] for _ in nodos]

    @staticmethod
    def cargar_json(path: str) -> "GrafoLista":
        with open(path) as f:
            data = json.load(f)
        g = GrafoLista(data["P"])
        for a, lista in data.get("E", {}).items():
            if a in g.idx:
                g.sucesores[g.idx[a]] = lista  # usamos la lista tal cual
        return g

    # --- Algoritmos de búsqueda ---
    # Teoría -> práctica: encontrar un "paso" = un camino dirigido de origen a destino.
    # Usamos BFS para obtener el camino de menor cantidad de aristas (en grafos no ponderados).
    # BFS expande en capas: primero distancia 0, luego 1, etc. Guardamos predecesores para
    # reconstruir la secuencia al llegar a destino.

    def camino_bfs(self, origen: str, destino: str) -> List[str]:
        if origen == destino:
            return [origen]
        n = len(self.nodos)
        visitado = [False]*n
        pred: List[Optional[int]] = [None]*n
        dq = deque()
        if origen not in self.idx or destino not in self.idx:
            return []
        s = self.idx[origen]
        t = self.idx[destino]
        visitado[s] = True
        dq.append(s)
        while dq:
            u = dq.popleft()
            if u == t:
                break
            for v_str in self.sucesores[u]:
                if v_str not in self.idx:  # robustez si hay destino no listado
                    continue
                v = self.idx[v_str]
                if not visitado[v]:
                    visitado[v] = True
                    pred[v] = u
                    dq.append(v)
        if not visitado[t]:
            return []  # no hay camino
        # reconstrucción inversa
        camino_idx = []
        cur = t
        while cur is not None:
            camino_idx.append(cur)
            cur = pred[cur]
        camino_idx.reverse()
        return [self.nodos[i] for i in camino_idx]

    def camino_dfs(self, origen: str, destino: str) -> List[str]:
        # DFS recursivo simple: no garantiza mínima longitud, solo algún camino.
        if origen not in self.idx or destino not in self.idx:
            return []
        s = self.idx[origen]
        t = self.idx[destino]
        n = len(self.nodos)
        visitado = [False]*n
        pred: List[Optional[int]] = [None]*n

        def dfs(u: int) -> bool:
            if u == t:
                return True
            visitado[u] = True
            for v_str in self.sucesores[u]:
                if v_str not in self.idx:
                    continue
                v = self.idx[v_str]
                if not visitado[v]:
                    pred[v] = u
                    if dfs(v):
                        return True
            return False

        if not dfs(s):
            return []
        # reconstrucción
        camino = []
        cur = t
        while cur is not None:
            camino.append(self.nodos[cur])
            cur = pred[cur]
        return list(reversed(camino))

    def camino(self, origen: str, destino: str, alg: str) -> List[str]:
        if alg == 'dfs':
            return self.camino_dfs(origen, destino)
        return self.camino_bfs(origen, destino)  # default bfs


def main():
    p = argparse.ArgumentParser(description="Ejercicio 3 - Camino entre dos nodos")
    p.add_argument('archivo', help='Ruta a archivo JSON con P y E')
    p.add_argument('origen')
    p.add_argument('destino')
    p.add_argument('--alg', choices=['bfs', 'dfs'], default='bfs', help='Algoritmo: bfs (por defecto, camino más corto en aristas) o dfs')
    p.add_argument('--solo-longitud', action='store_true', help='Muestra solo la longitud del camino')
    args = p.parse_args()

    g = GrafoLista.cargar_json(args.archivo)
    if args.origen not in g.idx:
        print('Origen no encontrado')
        return
    if args.destino not in g.idx:
        print('Destino no encontrado')
        return

    camino = g.camino(args.origen, args.destino, args.alg)
    if not camino:
        print('No existe camino')
        return
    if args.solo_longitud:
        print('Longitud (aristas):', len(camino) - 1)
    else:
        print(' -> '.join(camino))


if __name__ == '__main__':
    main()
