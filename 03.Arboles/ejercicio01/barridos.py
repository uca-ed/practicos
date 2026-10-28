def pre_orden(arreglo: list, r: int, i: int = 0):
    if i >= len(arreglo):
        return

    print(arreglo[i])

    for k in range(1, r + 1):
        hijo_idx = r * i + k
        pre_orden(arreglo, r, hijo_idx)
        
def post_orden(arreglo: list, r: int, i: int = 0):
    if i >= len(arreglo):
        return

    for k in range(1, r + 1):
        hijo_idx = r * i + k
        post_orden(arreglo, r, hijo_idx)

    print(arreglo[i])
    
import sys


def por_niveles(arreglo: list):
    for nodo in arreglo:
        print(nodo)

def barrido_simetrico(arreglo: list, i: int = 0):
    if i >= len(arreglo):
        return

    hijo_izq = 2 * i + 1
    hijo_der = 2 * i + 2

    barrido_simetrico(arreglo, hijo_izq)

    print(arreglo[i])

    barrido_simetrico(arreglo, hijo_der)