import json
from pathlib import Path
from collections import deque


def cargar_grafo_json(path):
    with open(path, encoding='utf-8') as f:
        data = json.load(f)

    grafo = {'P': [str(v) for v in data.get('P', [])], 'E': {}}
    for v in grafo['P']:
        vecinos = data.get('E', {}).get(v, [])
        if vecinos is None:
            vecinos = []
        grafo['E'][v] = []
        vistos = set()
        for n in vecinos:
            nodo = str(n)
            if nodo and nodo not in vistos:
                grafo['E'][v].append(nodo)
                vistos.add(nodo)
    return grafo


def alcanzables(grafo, inicio):
    inicio = str(inicio)
    visitados = set()
    cola = deque([inicio])

    while cola:
        actual = cola.popleft()
        if actual in visitados:
            continue
        visitados.add(actual)
        for vecino in grafo['E'].get(actual, []):
            if vecino not in visitados:
                cola.append(vecino)
    return visitados


def main():
    base = Path(__file__).resolve().parent.parent / 'ENTREGA1' / 'archivos_ej2'
    for archivo in sorted(base.glob('*.json')):
        grafo = cargar_grafo_json(archivo)
        print(f'Archivo: {archivo.name}')
        print(f'Cantidad de nodos: {len(grafo["P"])}')
        primero = next(iter(grafo['E']))
        print(f'E[{primero}][:10] = {grafo["E"][primero][:10]}')
        print(f'Alcanzables desde {primero}: {len(alcanzables(grafo, primero))}')
        print('---')


if __name__ == '__main__':
    main()
