class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None
        self.altura = 1  # toda hoja arranca con altura 1

def altura(nodo):
    if not nodo:
        return 0
    return nodo.altura


def factor_balance(nodo):
    if not nodo:
        return 0
    return altura(nodo.izq) - altura(nodo.der)

def rotacion_derecha(y):
    x = y.izq
    T2 = x.der

    x.der = y
    y.izq = T2

    y.altura = 1 + max(altura(y.izq), altura(y.der))
    x.altura = 1 + max(altura(x.izq), altura(x.der))

    return x 


def rotacion_izquierda(x):
    y = x.der
    T2 = y.izq

    y.izq = x
    x.der = T2

    x.altura = 1 + max(altura(x.izq), altura(x.der))
    y.altura = 1 + max(altura(y.izq), altura(y.der))

    return y  

def insertar(nodo, valor):
    if not nodo:
        return Nodo(valor)
    elif valor < nodo.valor:
        nodo.izq = insertar(nodo.izq, valor)
    elif valor > nodo.valor:
        nodo.der = insertar(nodo.der, valor)
    else:
        return nodo 

    nodo.altura = 1 + max(altura(nodo.izq), altura(nodo.der))

    balance = factor_balance(nodo)


    if balance > 1 and valor < nodo.izq.valor:
        return rotacion_derecha(nodo)

    if balance < -1 and valor > nodo.der.valor:
        return rotacion_izquierda(nodo)

    if balance > 1 and valor > nodo.izq.valor:
        nodo.izq = rotacion_izquierda(nodo.izq)
        return rotacion_derecha(nodo)

    if balance < -1 and valor < nodo.der.valor:
        nodo.der = rotacion_derecha(nodo.der)
        return rotacion_izquierda(nodo)

    return nodo 

def preorden_iterativo(raiz):
    if raiz is None:
        return
    pila = [raiz]
    while pila:
        nodo = pila.pop()
        print(nodo.valor, end='  ')
        if nodo.der:
            pila.append(nodo.der)
        if nodo.izq:
            pila.append(nodo.izq)


def cargar_datos(nombre_archivo):
    with open(nombre_archivo, "r", encoding="utf-8") as f:
        return [int(x) for x in f.read().split()]


def main():
    datos = cargar_datos("Arbol AVL.txt")

    raiz = None
    for valor in datos:
        raiz = insertar(raiz, valor)

    print("\nRecorrido en preorden del arbol AVL:")
    preorden_iterativo(raiz)
    print()

main()
