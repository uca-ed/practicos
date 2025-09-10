import argparse
import csv
import json
import os
from typing import List, Dict


class GrafoMatriz:
    def __init__(self, nodos: List[str]):
        self.nodos: List[str] = nodos
        self.idx: Dict[str, int] = {v: i for i, v in enumerate(nodos)}
        n = len(nodos)
        # Matriz de adyacencia (0/1)
        self.matriz: List[List[int]] = [[0]*n for _ in range(n)]
        # Estructuras auxiliares para eficiencia
        self.sucesores: List[List[int]] = [[] for _ in range(n)]
        self.predecesores: List[List[int]] = [[] for _ in range(n)]
        self.indegree: List[int] = [0]*n
        self.outdegree: List[int] = [0]*n

    def agregar_arista(self, origen: str, destino: str):
        if origen not in self.idx or destino not in self.idx:
            return
        i, j = self.idx[origen], self.idx[destino]
        if self.matriz[i][j] == 0:
            self.matriz[i][j] = 1
            self.sucesores[i].append(j)
            self.predecesores[j].append(i)
            self.outdegree[i] += 1
            self.indegree[j] += 1

    def vecindad_derecha(self, nodo: str) -> List[str]:
        i = self.idx[nodo]
        return [self.nodos[j] for j in self.sucesores[i]]

    def vecindad_izquierda(self, nodo: str) -> List[str]:
        i = self.idx[nodo]
        return [self.nodos[j] for j in self.predecesores[i]]

    def minimales(self) -> List[str]:
        return [self.nodos[i] for i, d in enumerate(self.indegree) if d == 0]

    def maximales(self) -> List[str]:
        return [self.nodos[i] for i, d in enumerate(self.outdegree) if d == 0]


def cargar_csv(path: str) -> GrafoMatriz:
    with open(path, newline='') as f:
        reader = csv.reader(f)
        filas = [list(map(int, row)) for row in reader if row]
    n = len(filas)
    if any(len(row) != n for row in filas):
        raise ValueError("La matriz no es cuadrada")
    nodos = [str(i+1) for i in range(n)]
    g = GrafoMatriz(nodos)
    for i in range(n):
        for j in range(n):
            if filas[i][j] != 0:
                g.agregar_arista(nodos[i], nodos[j])
    return g


def cargar_json(path: str) -> GrafoMatriz:
    with open(path) as f:
        data = json.load(f)
    nodos = data["P"]
    g = GrafoMatriz(nodos)
    # E contiene vecindad derecha
    for origen, destinos in data.get("E", {}).items():
        for destino in destinos:
            g.agregar_arista(origen, destino)
    return g


def cargar_grafo(path: str) -> GrafoMatriz:
    ext = os.path.splitext(path)[1].lower()
    if ext == '.csv':
        return cargar_csv(path)
    if ext == '.json':
        return cargar_json(path)
    raise ValueError("Formato no soportado")


def main():
    p = argparse.ArgumentParser(description="Ejercicio 1 - Grafos (matriz de adyacencia)")
    p.add_argument('archivo', help='Ruta al archivo .csv o .json')
    p.add_argument('--minimales', action='store_true')
    p.add_argument('--maximales', action='store_true')
    p.add_argument('--vec-der', metavar='NODO')
    p.add_argument('--vec-izq', metavar='NODO')
    args = p.parse_args()

    g = cargar_grafo(args.archivo)

    hizo_algo = False
    if args.minimales:
        print('Minimales:', ' '.join(g.minimales()))
        hizo_algo = True
    if args.maximales:
        print('Maximales:', ' '.join(g.maximales()))
        hizo_algo = True
    if args.vec_der:
        if args.vec_der not in g.idx:
            print('Nodo no encontrado')
        else:
            print('Vecindad derecha de', args.vec_der + ':', ' '.join(g.vecindad_derecha(args.vec_der)))
        hizo_algo = True
    if args.vec_izq:
        if args.vec_izq not in g.idx:
            print('Nodo no encontrado')
        else:
            print('Vecindad izquierda de', args.vec_izq + ':', ' '.join(g.vecindad_izquierda(args.vec_izq)))
        hizo_algo = True

    if not hizo_algo:
        # Por defecto muestra todo (puede ser grande)
        print('Minimales:', ' '.join(g.minimales()))
        print('Maximales:', ' '.join(g.maximales()))


if __name__ == '__main__':
    main()
