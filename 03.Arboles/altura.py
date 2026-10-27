"""
Ejercicio 1a: detecta la altura del árbol sin hacer recorridos.
"""
from arbol_arreglo import leer_arbol, altura, leer_argumentos


if __name__ == "__main__":
    r, archivo = leer_argumentos()
    A = leer_arbol(archivo)
    print(altura(len(A), r))
