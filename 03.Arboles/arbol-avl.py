import sys

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None
        self.altura = 1

def altura(nodo):
    if nodo is None:
        return 0
    return nodo.altura

def actualizar(nodo):
    nodo.altura = 1 + max(altura(nodo.izquierdo), altura(nodo.derecho))

def balance(nodo):
    if nodo is None:
        return 0
    return altura(nodo.izquierdo) - altura(nodo.derecho)

def rotar_derecha(y):
    x = y.izquierdo
    subarbol = x.derecho
    x.derecho = y
    y.izquierdo = subarbol
    actualizar(y)
    actualizar(x)
    return x

def rotar_izquierda(x):
    y = x.derecho
    subarbol = y.izquierdo
    y.izquierdo = x
    x.derecho = subarbol
    actualizar(x)
    actualizar(y)
    return y

def insertar(raiz, valor):
    if raiz is None:
        return Nodo(valor)

    if valor < raiz.valor:
        raiz.izquierdo = insertar(raiz.izquierdo, valor)
    elif valor > raiz.valor:
        raiz.derecho = insertar(raiz.derecho, valor)
    else:
        return raiz  # No se insertan valores duplicados.

    actualizar(raiz)
    fb = balance(raiz)

    # Caso izquierda-izquierda
    if fb > 1 and valor < raiz.izquierdo.valor:
        return rotar_derecha(raiz)

    # Caso derecha-derecha
    if fb < -1 and valor > raiz.derecho.valor:
        return rotar_izquierda(raiz)

    # Caso izquierda-derecha
    if fb > 1 and valor > raiz.izquierdo.valor:
        raiz.izquierdo = rotar_izquierda(raiz.izquierdo)
        return rotar_derecha(raiz)

    # Caso derecha-izquierda
    if fb < -1 and valor < raiz.derecho.valor:
        raiz.derecho = rotar_derecha(raiz.derecho)
        return rotar_izquierda(raiz)

    return raiz

def preorden(nodo):
    if nodo is not None:
        print(nodo.valor)
        preorden(nodo.izquierdo)
        preorden(nodo.derecho)

def main():
    if len(sys.argv) != 2:
        print("Uso: python arbol-avl.py archivo-datos.txt", file=sys.stderr)
        sys.exit(1)

    # El archivo debe contener los valores a insertar, separados por espacios o saltos de línea.
    with open(sys.argv[1], "r", encoding="utf-8") as archivo:
        contenido = archivo.read().split()

    raiz = None
    for elemento in contenido:
        raiz = insertar(raiz, int(elemento))

    # Imprime el AVL resultante en preorden, un nodo por renglón.
    preorden(raiz)

if __name__ == "__main__":
    main()
