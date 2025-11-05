class NodoAVL:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None
        self.altura = 1  

def obtener_altura(nodo):
    if not nodo:
        return 0
    return nodo.altura

def balance(nodo):
    if not nodo:
        return 0
    return obtener_altura(nodo.izq) - obtener_altura(nodo.der)

def rotar_derecha(y):
    x = y.izq
    T2 = x.der

    x.der = y
    y.izq = T2

    y.altura = 1 + max(obtener_altura(y.izq), obtener_altura(y.der))
    x.altura = 1 + max(obtener_altura(x.izq), obtener_altura(x.der))

    return x

def rotar_izquierda(x):
    y = x.der
    T2 = y.izq

    y.izq = x
    x.der = T2

    x.altura = 1 + max(obtener_altura(x.izq), obtener_altura(x.der))
    y.altura = 1 + max(obtener_altura(y.izq), obtener_altura(y.der))

    return y
 
def insertar(nodo, clave):
    if not nodo:
        return NodoAVL(clave)

    if clave < nodo.valor:
        nodo.izq = insertar(nodo.izq, clave)
    elif clave > nodo.valor:
        nodo.der = insertar(nodo.der, clave)
    else:
        return nodo  

    nodo.altura = 1 + max(obtener_altura(nodo.izq), obtener_altura(nodo.der))
    b = balance(nodo)

    if b > 1 and clave < nodo.izq.valor:
        return rotar_derecha(nodo)

    if b < -1 and clave > nodo.der.valor:
        return rotar_izquierda(nodo)

    if b > 1 and clave > nodo.izq.valor:
        nodo.izq = rotar_izquierda(nodo.izq)
        return rotar_derecha(nodo)

    if b < -1 and clave < nodo.der.valor:
        nodo.der = rotar_derecha(nodo.der)
        return rotar_izquierda(nodo)

    return nodo

def en_orden(nodo):
    if not nodo:
        return []
    return en_orden(nodo.izq) + [nodo.valor] + en_orden(nodo.der)

with open("Archivos/AVL.txt", "r", encoding="utf-8") as f:
    datos = [int(linea.strip()) for linea in f if linea.strip().isdigit()]

raiz = None
for valor in datos:
    raiz = insertar(raiz, valor)

print("Recorrido en orden del arbol AVL:", en_orden(raiz))
