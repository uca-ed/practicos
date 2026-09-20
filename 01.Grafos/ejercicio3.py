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


def componentes_conexas(grafo):
    no_visitados = set(grafo['E'].keys())
    componentes = []
    while no_visitados:
        inicio = next(iter(no_visitados))
        alc = alcanzables(grafo, inicio)
        componentes.append(alc)
        no_visitados -= alc
    return componentes


def main():
    base = Path(__file__).resolve().parent.parent / 'ENTREGA1' / 'archivos_ej3'

    multiplos = cargar_grafo_json(base / 'multiplos200Ref.json')
    alc = alcanzables(multiplos, '2')
    print('Ejercicio 3 - múltiplos 200:')
    print(f'Cantidad alcanzables desde 2: {len(alc)}')
    print(f'Incluye 100? {"100" in alc}')
    print(f'Incluye 198? {"198" in alc}')
    print(f'Incluye 199? {"199" in alc}')
    print(f'Incluye 3? {"3" in alc}')
    print('---')

    divisores = cargar_grafo_json(base / 'esDivisorDe-200.json')
    comps = componentes_conexas(divisores)
    print('Ejercicio 3 - divisores de 200:')
    print(f'Cantidad de componentes: {len(comps)}')
    print(f'Primera componente: {sorted(next(iter(comps)))[:10]}')


if __name__ == '__main__':
    main()
