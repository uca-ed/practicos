"""
Ejercicio 2: crea un árbol AVL realizando las inserciones dadas en el archivo de datos.

El archivo de datos tiene las claves a insertar separadas por espacios o renglones.
"""
import argparse


class Nodo:
    def __init__(self, clave):
        self.clave = clave
        self.izq = None   
        self.der = None   
        self.altura = 1


def altura(p: Nodo) -> int:
    return p.altura if p else 0


def actualizar_altura(p: Nodo):
    p.altura = 1 + max(altura(p.izq), altura(p.der))


def fb(p: Nodo) -> int:
    return altura(p.der) - altura(p.izq)


def rotar_izquierda(a: Nodo) -> Nodo:
    b = a.der
    a.der = b.izq
    b.izq = a
    actualizar_altura(a)
    actualizar_altura(b)
    return b


def rotar_derecha(a: Nodo) -> Nodo:
    b = a.izq
    a.izq = b.der
    b.der = a
    actualizar_altura(a)
    actualizar_altura(b)
    return b


def balancear(a: Nodo, log: list[str]) -> Nodo:
    actualizar_altura(a)
    if fb(a) == 2:
        if fb(a.der) >= 0:
            log.append(f"  caso 1 (rotación simple a izquierda) en {a.clave}")
        else:
            log.append(f"  caso 2 (rotación doble derecha-izquierda) en {a.clave}, sube {a.der.izq.clave}")
            a.der = rotar_derecha(a.der)
        return rotar_izquierda(a)
    if fb(a) == -2:
        if fb(a.izq) <= 0:
            log.append(f"  caso 1 espejo (rotación simple a derecha) en {a.clave}")
        else:
            log.append(f"  caso 2 espejo (rotación doble izquierda-derecha) en {a.clave}, sube {a.izq.der.clave}")
            a.izq = rotar_izquierda(a.izq)
        return rotar_derecha(a)
    return a


def insertar(p: Nodo, clave, log: list[str]) -> Nodo:
    if p is None:
        return Nodo(clave)
    if clave < p.clave:
        p.izq = insertar(p.izq, clave, log)
    elif clave > p.clave:
        p.der = insertar(p.der, clave, log)
    else:
        log.append(f"  {clave} ya está en el árbol, no se inserta")
        return p
    return balancear(p, log)


def dibujar(p: Nodo, prefijo: str = "", renglones: list[str] = None) -> list[str]:
    """Dibuja el árbol acostado: el SAD arriba, el SAI abajo, y el FB entre paréntesis."""
    if renglones is None:
        renglones = []
    if p is not None:
        dibujar(p.der, prefijo + "        ", renglones)
        renglones.append(f"{prefijo}{p.clave} ({fb(p):+d})")
        dibujar(p.izq, prefijo + "        ", renglones)
    return renglones


def pre_orden(p: Nodo, resultado: list):
    if p is not None:
        resultado.append(p.clave)
        pre_orden(p.izq, resultado)
        pre_orden(p.der, resultado)


def simetrico(p: Nodo, resultado: list):
    if p is not None:
        simetrico(p.izq, resultado)
        resultado.append(p.clave)
        simetrico(p.der, resultado)


def leer_datos(archivo: str) -> list:
    with open(archivo) as f:
        claves = f.read().replace(",", " ").split()
    try:
        return [int(c) for c in claves]
    except ValueError:
        return claves 


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("archivo", help="Archivo con las claves a insertar")
    args = parser.parse_args()

    raiz = None
    for clave in leer_datos(args.archivo):
        log = []
        raiz = insertar(raiz, clave, log)
        print(f"Inserto {clave}")
        for renglon in log:
            print(renglon)

    print()
    print("Árbol AVL resultante (acostado: SAD arriba, SAI abajo; entre paréntesis el FB):")
    print("\n".join(dibujar(raiz)))
    print()
    pre, sim = [], []
    pre_orden(raiz, pre)
    simetrico(raiz, sim)
    print("Pre-orden:", ", ".join(map(str, pre)))
    print("Simétrico:", ", ".join(map(str, sim)))
    print("Altura:", altura(raiz))
