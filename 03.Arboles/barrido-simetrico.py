"""
Ejercicio 1e: barrido simétrico de un árbol binario (SAI, raíz, SAD).
"""
from arbol_arreglo import leer_arbol, leer_argumentos, imprimir


def simetrico(A: list[str], k: int, resultado: list[str]):
    if k >= len(A):
        return
    simetrico(A, 2 * k + 1, resultado)  # SAI
    resultado.append(A[k])
    simetrico(A, 2 * k + 2, resultado)  # SAD


if __name__ == "__main__":
    r, archivo = leer_argumentos(con_grado=False)
    if r != 2:
        raise ValueError("El barrido simétrico solo está definido para árboles binarios (grado 2).")
    A = leer_arbol(archivo)
    resultado = []
    simetrico(A, 0, resultado)
    imprimir(resultado)
