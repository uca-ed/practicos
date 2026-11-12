class Nodo:
    def __init__(self, clave):
        self.clave = clave
        self.izq = self.der = None
        self.h = 1

def h(n): return n.h if n else 0
def fe(n): return h(n.der) - h(n.izq) if n else 0
def actualizar(n): n.h = 1 + max(h(n.izq), h(n.der))

def rot_der(y):
    x = y.izq
    y.izq, x.der = x.der, y
    actualizar(y); actualizar(x)
    return x

def rot_izq(x):
    y = x.der
    x.der, y.izq = y.izq, x
    actualizar(x); actualizar(y)
    return y

def insertar(n, clave):
    if n is None:
        return Nodo(clave)
    if clave < n.clave:
        n.izq = insertar(n.izq, clave)
    elif clave > n.clave:
        n.der = insertar(n.der, clave)
    else:
        return n                      # duplicado: se ignora
    actualizar(n)
    f = fe(n)
    if f < -1:                        # desbalance a la izquierda
        if fe(n.izq) > 0:             # caso LR
            n.izq = rot_izq(n.izq)
        return rot_der(n)             # LL
    if f > 1:                         # desbalance a la derecha
        if fe(n.der) < 0:             # caso RL
            n.der = rot_der(n.der)
        return rot_izq(n)             # RR
    return n

def leer_datos(ruta):
    with open(ruta) as f:
        return [int(x) for x in f.read().replace(',', ' ').split()]

def mostrar(n, nivel=0):              # vista rotada: derecha arriba
    if n:
        mostrar(n.der, nivel + 1)
        print('    ' * nivel + f'{n.clave} (FE={fe(n)})')
        mostrar(n.izq, nivel + 1)

if __name__ == '__main__':
    raiz = None
    for x in leer_datos('datos.txt'):
        raiz = insertar(raiz, x)
    mostrar(raiz)
