import csv
from pathlib import Path


def cargar_matriz_csv(path):
    with open(path, newline='', encoding='utf-8') as f:
        filas = [linea for linea in csv.reader(f) if linea and any(x.strip() for x in linea)]

    grafo = {}
    for i, fila in enumerate(filas, start=1):
        vecinos = [str(j) for j, valor in enumerate(fila, start=1) if valor.strip() == '1']
        grafo[str(i)] = vecinos
    return grafo


def main():
    base = Path(__file__).resolve().parent.parent / 'ENTREGA1' / 'archivos_ej1'
    for archivo in sorted(base.glob('*.csv')):
        grafo = cargar_matriz_csv(archivo)
        print(f'Archivo: {archivo.name}')
        print(f'Cantidad de nodos: {len(grafo)}')
        print('Primeros nodos:')
        for nodo in sorted(grafo, key=lambda x: int(x))[:5]:
            print(f'  {nodo}: {grafo[nodo]}')
        print('---')


if __name__ == '__main__':
    main()
