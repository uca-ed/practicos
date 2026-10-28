"""
Ejercicio 2: Creación de un Árbol AVL a partir de un archivo de datos.

Implementa inserción balanceada según la teoría de la cátedra (Knuth / Adelson-Velsky y Landis):
- Factor de balanceo: fb(p) = h(SAD) - h(SAI) en {-2, -1, 0, 1, 2}.
- Caso 1: Rotación simple a izquierda (fb == 2, fb(der) >= 0).
- Caso 1 espejo: Rotación simple a derecha (fb == -2, fb(izq) <= 0).
- Caso 2: Rotación doble derecha-izquierda (fb == 2, fb(der) < 0).
- Caso 2 espejo: Rotación doble izquierda-derecha (fb == -2, fb(izq) > 0).
"""

import argparse
import os
import sys


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
    # Faap Factor de balanceo: h(SAD) - h(SAI)
    return (altura(p.der) - altura(p.izq)) if p else 0


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


def balancear(a: Nodo, log: list) -> Nodo:
    actualizar_altura(a)

    # Desbalance hacia la derecha
    if fb(a) == 2:
        if fb(a.der) >= 0:
            log.append(f"  caso 1 (rotación simple a izquierda) en {a.clave}")
        else:
            log.append(
                f"  caso 2 (rotación doble derecha-izquierda) en {a.clave}, sube {a.der.izq.clave}"
            )
            a.der = rotar_derecha(a.der)
        return rotar_izquierda(a)

    # Desbalance hacia la izquierda
    if fb(a) == -2:
        if fb(a.izq) <= 0:
            log.append(f"  caso 1 espejo (rotación simple a derecha) en {a.clave}")
        else:
            log.append(
                f"  caso 2 espejo (rotación doble izquierda-derecha) en {a.clave}, sube {a.izq.der.clave}"
            )
            a.izq = rotar_izquierda(a.izq)
        return rotar_derecha(a)

    return a


def insertar(p: Nodo, clave, log: list) -> Nodo:
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


def dibujar(p: Nodo, prefijo: str = "", renglones: list = None) -> list:
    """Dibuja el árbol acostado: SAD arriba, SAI abajo; muestra FB entre paréntesis."""
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


def leer_datos(ruta_archivo: str) -> list:
    # Si la ruta no existe directa, busca relativa al directorio del script
    if not os.path.isabs(ruta_archivo) and not os.path.exists(ruta_archivo):
        posible = os.path.join(os.path.dirname(os.path.abspath(__file__)), ruta_archivo)
        if os.path.exists(posible):
            ruta_archivo = posible

    contenido = ""
    for enc in ("utf-8", "utf-16", "latin-1"):
        try:
            with open(ruta_archivo, "r", encoding=enc) as f:
                contenido = f.read()
                break
        except (UnicodeDecodeError, UnicodeError):
            continue
    if not contenido:
        with open(ruta_archivo, "r") as f:
            contenido = f.read()

    claves = contenido.replace(",", " ").split()
    try:
        return [int(c) for c in claves]
    except ValueError:
        return claves


def autotest():
    """Autochequeo con asserts de los 4 casos de rotación e invariantes AVL."""
    pruebas = [
        ([10, 20, 30], "caso 1"),
        ([30, 20, 10], "caso 1 espejo"),
        ([10, 30, 20], "caso 2"),
        ([30, 10, 20], "caso 2 espejo"),
    ]
    for secuencia, caso_esperado in pruebas:
        r = None
        logs = []
        for x in secuencia:
            l = []
            r = insertar(r, x, l)
            logs.extend(l)
        assert any(caso_esperado in m for m in logs), f"Fallo al detectar {caso_esperado} en {secuencia}"
        assert r.clave == 20, f"La nueva raíz debió ser 20 en {secuencia}"
        assert abs(fb(r)) <= 1, f"El factor de balanceo excede el límite en {secuencia}"
        sim = []
        simetrico(r, sim)
        assert sim == [10, 20, 30], f"El recorrido simétrico no quedó ordenado: {sim}"
    print("Autochequeo: todos los casos de rotación verificados con éxito.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Construcción y visualización de un Árbol AVL.")
    parser.add_argument("archivo", nargs="?", default="datos.txt", help="Archivo con claves a insertar (defecto: datos.txt)")
    parser.add_argument("--test", action="store_true", help="Ejecuta batería de pruebas automáticas")
    args = parser.parse_args()

    if args.test:
        autotest()
        sys.exit(0)

    raiz = None
    datos = leer_datos(args.archivo)
    for clave in datos:
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
