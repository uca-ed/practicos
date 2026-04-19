import json

def cargar_grafo(ruta):
    """Lee un JSON y arma la matriz de adyacencia."""
    with open(ruta, 'r', encoding='utf-8') as f:
        estructura = json.load(f)

    nodos = [str(x) for x in estructura['P']]
    n = len(nodos)
    indice = {nodo: i for i, nodo in enumerate(nodos)}

    # matriz de n x n inicializada en 0
    matriz = [[0] * n for _ in range(n)]

    for origen, vecinos in estructura['E'].items():
        i = indice[origen]
        for destino in vecinos:
            j = indice[str(destino)]
            matriz[i][j] = 1

    return nodos, matriz


def es_reflexiva(matriz):
    # Para todo i: (i, i) debe estar en la relacion
    n = len(matriz)
    for i in range(n):
        if matriz[i][i] == 0:
            return False
    return True


def es_simetrica(matriz):
    # Si (i, j) esta, entonces (j, i) tambien
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            if matriz[i][j] == 1 and matriz[j][i] == 0:
                return False
    return True


def es_antisimetrica(matriz):
    # Si (i, j) y (j, i) estan, entonces i == j
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            if i != j and matriz[i][j] == 1 and matriz[j][i] == 1:
                return False
    return True


def es_transitiva(matriz):
    # Si (i, j) y (j, k) estan, entonces (i, k) tambien
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            if matriz[i][j] == 1:
                for k in range(n):
                    if matriz[j][k] == 1 and matriz[i][k] == 0:
                        return False
    return True


def analizar(ruta):
    nodos, matriz = cargar_grafo(ruta)

    reflexiva = es_reflexiva(matriz)
    simetrica = es_simetrica(matriz)
    antisimetrica = es_antisimetrica(matriz)
    transitiva = es_transitiva(matriz)

    print(f'Archivo: {ruta}')
    print(f'Cantidad de nodos: {len(nodos)}')
    print(f'Reflexiva:     {reflexiva}')
    print(f'Simetrica:     {simetrica}')
    print(f'Antisimetrica: {antisimetrica}')
    print(f'Transitiva:    {transitiva}')

    if reflexiva and antisimetrica and transitiva:
        print('=> La relacion es un ORDEN.')
    elif reflexiva and simetrica and transitiva:
        print('=> La relacion es una RELACION DE EQUIVALENCIA.')
    else:
        print('=> La relacion NO es ni orden ni equivalencia.')


if __name__ == '__main__':
    if __name__ == '__main__':
        analizar('01.json')
        analizar('02.json')
        analizar('03.json')
