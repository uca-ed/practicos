class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None
        self.altura = 1

def altura(nodo):
    if nodo is None:
        return 0
    return nodo.altura

def balance(nodo):
    if nodo is None:
        return 0
    # altura izquierda menos altura derecha
    return altura(nodo.izq) - altura(nodo.der)

def rotar_derecha(y):
    x = y.izq
    aux = x.der  # guardo el hijo derecho de x antes de moverlo

    x.der = y
    y.izq = aux

    # actualizo alturas, primero y despues x
    y.altura = 1 + max(altura(y.izq), altura(y.der))
    x.altura = 1 + max(altura(x.izq), altura(x.der))

    return x

def rotar_izquierda(x):
    y = x.der
    aux = y.izq  # guardo el hijo izquierdo de y

    y.izq = x
    x.der = aux

    # actualizo alturas
    x.altura = 1 + max(altura(x.izq), altura(x.der))
    y.altura = 1 + max(altura(y.izq), altura(y.der))

    return y

def insertar(nodo, valor):
    # caso base, lugar vacio
    if nodo is None:
        return Nodo(valor)

    if valor < nodo.valor:
        nodo.izq = insertar(nodo.izq, valor)
    elif valor > nodo.valor:
        nodo.der = insertar(nodo.der, valor)
    else:
        return nodo  # no inserto duplicados

    # actualizo la altura del nodo actual
    nodo.altura = 1 + max(altura(nodo.izq), altura(nodo.der))

    fb = balance(nodo)  # factor de balance

    # izquierda izquierda
    if fb > 1 and valor < nodo.izq.valor:
        return rotar_derecha(nodo)

    # derecha derecha
    if fb < -1 and valor > nodo.der.valor:
        return rotar_izquierda(nodo)

    # izquierda derecha
    if fb > 1 and valor > nodo.izq.valor:
        nodo.izq = rotar_izquierda(nodo.izq)
        return rotar_derecha(nodo)

    # derecha izquierda
    if fb < -1 and valor < nodo.der.valor:
        nodo.der = rotar_derecha(nodo.der)
        return rotar_izquierda(nodo)

    return nodo

def preorden(nodo):
    if nodo is not None:
        print(nodo.valor)
        preorden(nodo.izq)
        preorden(nodo.der)


# datos de prueba, despues los reemplazo con los del archivo
datos = [10, 20, 30, 40, 50, 25]

raiz = None
for valor in datos:
    raiz = insertar(raiz, valor)
    # print("inserte", valor)  # esto lo usaba para debuggear

print("Valores insertados:", datos)
print("Recorrido preorden:")
preorden(raiz)
