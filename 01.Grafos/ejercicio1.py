import csv
import json
import os

# Carpeta donde vive este script, para poder ejecutarlo desde cualquier lugar
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def ruta(archivo):
    return os.path.join(BASE_DIR, archivo)

def cargar_csv(archivo):
    matriz = []
    with open(ruta(archivo), 'r') as f:
        for fila in csv.reader(f):
            if fila:
                matriz.append([int(x) for x in fila])
    nodos = list(range(len(matriz)))
    return matriz, nodos

def cargar_json(archivo):
    with open(ruta(archivo), 'r') as f:
        datos = json.load(f)
    
    if isinstance(datos, list): 
        matriz = [[int(x) for x in fila] for fila in datos]
        nodos = list(range(len(matriz)))
    else: 
        nodos = datos['P']
        n = len(nodos)
        matriz = [[0] * n for _ in range(n)]
        for u in nodos:
            for v in datos['E'][u]:
                if v in nodos:
                    matriz[nodos.index(u)][nodos.index(v)] = 1
    return matriz, nodos

def vecindad_derecha(matriz, nodos, nodo):
    idx = nodos.index(nodo)
    return [nodos[col] for col in range(len(nodos)) if matriz[idx][col] == 1]

def vecindad_izquierda(matriz, nodos, nodo):
    idx = nodos.index(nodo)
    return [nodos[fila] for fila in range(len(matriz)) if matriz[fila][idx] == 1]

def minimales(matriz, nodos):
    return [n for n in nodos if len(vecindad_izquierda(matriz, nodos, n)) == 0]

def maximales(matriz, nodos):
    return [n for n in nodos if len(vecindad_derecha(matriz, nodos, n)) == 0]

def mostrar_grafo(matriz, nodos):
    if len(nodos) > 50: # para no imprimir matriz muy grande en consola
        print(f"(grafo con {len(nodos)} nodos, matriz muy grande para mostrar)")
        print()
        return
    print("    " + " ".join(f"[{n}]" for n in nodos))
    for idx, fila in enumerate(matriz):
        print(f"[{nodos[idx]}] " + "   ".join(str(x) for x in fila))
    print()


def main():
    
    archivos = ["01.csv", "02.csv", "03.csv", "04.csv"]

    for arch in archivos:
        print("======================================")
        print(f"ARCHIVO: {arch}")
        print("======================================")
        matriz, nodos = cargar_csv(arch)
        mostrar_grafo(matriz, nodos)
        print("Nodos Minimales:  ", minimales(matriz, nodos))
        print("Nodos Maximales:  ", maximales(matriz, nodos))

        if nodos:
            test_node = nodos[0]
            print(f"Vecindad Derecha de {test_node} R({test_node}): ", vecindad_derecha(matriz, nodos, test_node))
            print(f"Vecindad Izquierda de {test_node} L({test_node}):", vecindad_izquierda(matriz, nodos, test_node))
        print("\n")

    arch = "01.json"
    print("======================================")
    print(f"ARCHIVO: {arch}")
    print("======================================")
    matriz, nodos = cargar_json(arch)
    mostrar_grafo(matriz, nodos)

    print("Nodos Minimales:  ", minimales(matriz, nodos))
    print("Nodos Maximales:  ", maximales(matriz, nodos))

    if nodos:
        test_node = nodos[0]
        print(f"Vecindad Derecha de {test_node} R({test_node}): ", vecindad_derecha(matriz, nodos, test_node))
        print(f"Vecindad Izquierda de {test_node} L({test_node}):", vecindad_izquierda(matriz, nodos, test_node))

if __name__ == "__main__":
    main()