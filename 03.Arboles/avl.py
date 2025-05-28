import json

class NodoAVL:
    def __init__(self, clave):
        self.clave = clave
        self.izq = None
        self.der = None
        self.altura = 1

def get_altura(nodo):
    if not nodo:
        return 0
    
    return nodo.altura

def get_balance(nodo):
    if not nodo:
        return 0
    
    return get_altura(nodo.izq) - get_altura(nodo.der)

def rotar_derecha(y):
    x = y.izq
    T2 = x.der

    x.der = y
    y.izq = T2
    
    y.altura = max(get_altura(y.izq), get_altura(y.der)) + 1
    x.altura = max(get_altura(x.izq), get_altura(x.der)) + 1
    
    return x

def rotar_izquierda(x):
    y = x.der
    T2 = y.izq
    
    y.izq = x
    x.der = T2
    
    x.altura = max(get_altura(x.izq), get_altura(x.der)) + 1
    y.altura = max(get_altura(y.izq), get_altura(y.der)) + 1
    
    return y

def insertar(nodo, clave):
    if not nodo:
        return NodoAVL(clave)
    elif clave < nodo.clave:
        nodo.izq = insertar(nodo.izq, clave)
    else:
        nodo.der = insertar(nodo.der, clave)

    nodo.altura = 1 + max(get_altura(nodo.izq), get_altura(nodo.der))
    balance = get_balance(nodo)

    # Condiciones rotaacionales
    if balance > 1 and clave < nodo.izq.clave:
        return rotar_derecha(nodo)
    if balance < -1 and clave > nodo.der.clave:
        return rotar_izquierda(nodo)
    if balance > 1 and clave > nodo.izq.clave:
        nodo.izq = rotar_izquierda(nodo.izq)
        return rotar_derecha(nodo)
    if balance < -1 and clave < nodo.der.clave:
        nodo.der = rotar_derecha(nodo.der)
        return rotar_izquierda(nodo)

    return nodo

def barrido_inorden(nodo, resultado=None):
    if resultado is None:
        resultado = []
    if nodo:
        barrido_inorden(nodo.izq, resultado)
        resultado.append(nodo.clave)
        barrido_inorden(nodo.der, resultado)
    return resultado

def main():
    with open("02.json", 'r') as f:
        datos = json.load(f)
        inserciones = datos["valores"]

    raiz = None
    for clave in inserciones:
        raiz = insertar(raiz, clave)

    resultado = barrido_inorden(raiz)
    print("Recorrido inorden del árbol AVL:", resultado)

if __name__ == "__main__":
    main()