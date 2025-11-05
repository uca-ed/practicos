from collections import deque
from typing import Iterable, Optional, List

class Nodo:
    __slots__ = ("key", "izq", "der", "h")
    def __init__(self, key: int):
        self.key = key
        self.izq: Optional[Nodo] = None
        self.der: Optional[Nodo] = None
        self.h: int = 1  

def altura(n: Optional[Nodo]) -> int:
    return n.h if n else 0

def actualizar_altura(n: Nodo) -> None:
    n.h = 1 + max(altura(n.izq), altura(n.der))

def balance(n: Optional[Nodo]) -> int:
    return altura(n.izq) - altura(n.der) if n else 0

def rot_der(y: Nodo) -> Nodo:
    x = y.izq
    T2 = x.der if x else None
    x.der = y
    y.izq = T2
    actualizar_altura(y)
    actualizar_altura(x)
    return x

def rot_izq(x: Nodo) -> Nodo:
    y = x.der
    T2 = y.izq if y else None
    y.izq = x
    x.der = T2
    actualizar_altura(x)
    actualizar_altura(y)
    return y

def insertar(raiz: Optional[Nodo], key: int) -> Nodo:

    if raiz is None:
        return Nodo(key)
    if key < raiz.key:
        raiz.izq = insertar(raiz.izq, key)
    elif key > raiz.key:
        raiz.der = insertar(raiz.der, key)
    else:
        return raiz


    actualizar_altura(raiz)
    b = balance(raiz)
    if b > 1 and key < raiz.izq.key:
        return rot_der(raiz)
    if b < -1 and key > raiz.der.key:
        return rot_izq(raiz)
    if b > 1 and key > raiz.izq.key:
        raiz.izq = rot_izq(raiz.izq)
        return rot_der(raiz)
    if b < -1 and key < raiz.der.key:
        raiz.der = rot_der(raiz.der)
        return rot_izq(raiz)

    return raiz

def construir_avl(datos: Iterable[int]) -> Optional[Nodo]:
    raiz: Optional[Nodo] = None
    for x in datos:
        raiz = insertar(raiz, int(x))
    return raiz

def inorder(n: Optional[Nodo]) -> List[int]:
    if not n: return []
    return inorder(n.izq) + [n.key] + inorder(n.der)

def preorder(n: Optional[Nodo]) -> List[int]:
    if not n: return []
    return [n.key] + preorder(n.izq) + preorder(n.der)

def niveles(n: Optional[Nodo]) -> List[List[int]]:
    if not n: return []
    q, res = deque([n]), []
    while q:
        nivel = []
        for _ in range(len(q)):
            u = q.popleft()
            nivel.append(u.key)
            if u.izq: q.append(u.izq)
            if u.der: q.append(u.der)
        res.append(nivel)
    return res

if __name__ == "__main__":
    #datos = [10, 20, 30, 40, 50, 25]
    datos =[30, 50, 40, 60, 55]  

    avl = construir_avl(datos)

    print("Inorden (debe quedar ordenado):", inorder(avl))
    print("Preorden:", preorder(avl))
    print("Por niveles:", niveles(avl))
