class Nodo:
    def __init__(self,valor):
        self.valor = valor
        self.izq = None
        self.der = None
        self.altura = 1

def obtener_altura(nodo):
    if nodo is None:
        return 0
    else:
        return nodo.altura

def obtener_balance(nodo):
    if nodo is None:
        return 0
    else:
        return obtener_altura(nodo.izq) - obtener_altura(nodo.der)

def rotar_derecha(nodo_desbalanceado):
    nueva_raiz = nodo_desbalanceado.izq
    subarbol_medio = nueva_raiz.der

    nueva_raiz.der = nodo_desbalanceado
    nodo_desbalanceado.izq = subarbol_medio

    nodo_desbalanceado.altura = 1 + max(
        obtener_altura(nodo_desbalanceado.izq),
        obtener_altura(nodo_desbalanceado.der)
    )

    nueva_raiz.altura = 1 + max(
        obtener_altura(nueva_raiz.izq),
        obtener_altura(nueva_raiz.der)
    )

    return nueva_raiz

def rotar_izquierda(nodo_desbalanceado):
    nueva_raiz = nodo_desbalanceado.der
    subarbol_medio = nueva_raiz.izq

    nueva_raiz.izq = nodo_desbalanceado
    nodo_desbalanceado.der = subarbol_medio

    nodo_desbalanceado.altura = 1 + max(
        obtener_altura(nodo_desbalanceado.izq),
        obtener_altura(nodo_desbalanceado.der)
    )

    nueva_raiz.altura = 1 + max(
        obtener_altura(nueva_raiz.izq),
        obtener_altura(nueva_raiz.der)
    )

    return nueva_raiz

def insertar(nodo_actual, valor):
    if nodo_actual is None:
        return Nodo(valor)

    if valor < nodo_actual.valor:
        nodo_actual.izq = insertar(nodo_actual.izq, valor)
    elif valor > nodo_actual.valor:
        nodo_actual.der = insertar(nodo_actual.der, valor)
    else:
        return nodo_actual

    nodo_actual.altura = 1 + max(
        obtener_altura(nodo_actual.izq),
        obtener_altura(nodo_actual.der)
    )


    balance = obtener_balance(nodo_actual)

    if balance > 1 and valor < nodo_actual.izq.valor:
        return rotar_derecha(nodo_desbalanceado=nodo_actual)

    if balance < -1 and valor > nodo_actual.der.valor:
        return rotar_izquierda(nodo_desbalanceado=nodo_actual)

    if balance > 1 and valor > nodo_actual.izq.valor:
        nodo_actual.izq = rotar_izquierda(nodo_desbalanceado=nodo_actual.izq)
        return rotar_derecha(nodo_desbalanceado=nodo_actual)

    if balance < -1 and valor < nodo_actual.der.valor:
        nodo_actual.der = rotar_derecha(nodo_desbalanceado=nodo_actual.der)
        return rotar_izquierda(nodo_desbalanceado=nodo_actual)

    return nodo_actual

def imprimir(nodo):
    if nodo is not None:
        imprimir(nodo.izq)
        print(f"Valor {nodo.valor} | Altura: {nodo.altura}")
        imprimir(nodo.der)

def main():
    raiz = None

    with open("datos.txt", "r") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if linea != "":
                partes = linea.replace(",","").split()
                for parte in partes:
                    numero = int(parte)
                    raiz = insertar(raiz,numero)

    print("Arbol AVL:\n")
    imprimir(raiz)

if __name__ == "__main__":
    main()