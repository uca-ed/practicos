"""
EJERCICIO 2 - Propiedades de una relacion representada como grafo.

Un grafo dirigido G = (P, E) es exactamente una relacion binaria R sobre P:

        a R b   <=>   existe la arista a -> b   <=>   M[a][b] == 1

Propiedades (todas se leen sobre la matriz de adyacencia M):

    Reflexiva      M[a][a] == 1 para todo a            (diagonal llena)
    Simetrica      M[a][b] == M[b][a] para todo a,b    (M == M traspuesta)
    Antisimetrica  si M[a][b] y M[b][a] entonces a==b  (sin pares mutuos fuera
                                                        de la diagonal)
    Transitiva     si M[a][b] y M[b][c] entonces M[a][c]

Clasificacion:

    ES UN ORDEN                reflexiva + antisimetrica + transitiva
    ES RELACION DE EQUIVALENCIA  reflexiva + simetrica + transitiva

Uso desde la terminal de VS Code:

    python ejercicio2.py 01.json
    python ejercicio2.py 01.json 02.json 03.json
    python ejercicio2.py            (analiza 01, 02 y 03 si estan en la carpeta)
"""

import json
import os
import sys
import time


# ======================================================================
# 1. El grafo: matriz de adyacencia guardada como bitset por fila
# ======================================================================
#
# 03.json tiene 9999 nodos -> la matriz tiene 9999 x 9999 = 99.980.001
# celdas. Guardar eso como lista de listas de enteros de Python son varios
# GB de RAM. Por eso cada FILA se guarda como un entero grande de Python
# usado como conjunto de bits: el bit j prendido significa "existe i -> j".
# Asi las comparaciones entre filas (union, interseccion, inclusion) las
# resuelve Python en C de un saque, en vez de con un for en Python.

class Grafo:

    def __init__(self, nodos):
        self.nodos = list(nodos)              # nombres, en orden de fila
        self.n = len(self.nodos)
        self.indice = {v: i for i, v in enumerate(self.nodos)}
        self.fila = [0] * self.n              # fila[i] = bitset de sucesores

    def agregar(self, origen, destino):
        i = self.indice[origen]
        j = self.indice[destino]
        self.fila[i] |= (1 << j)

    def hay_arista(self, a, b):
        return (self.fila[self.indice[a]] >> self.indice[b]) & 1 == 1

    def cantidad_aristas(self):
        return sum(bin(f).count("1") for f in self.fila)

    def columna(self, j):
        """Bitset de los predecesores del nodo j (recorre la columna)."""
        col = 0
        for i in range(self.n):
            if (self.fila[i] >> j) & 1:
                col |= (1 << i)
        return col

    def __str__(self):
        return f"{self.n} nodos, {self.cantidad_aristas()} aristas"


def bits(x, nombres):
    """Convierte un bitset en la lista de nombres de nodo que contiene."""
    salida = []
    while x:
        b = x & -x                 # bit mas bajo prendido
        salida.append(nombres[b.bit_length() - 1])
        x ^= b
    return salida


# ======================================================================
# 2. Lectura del json
# ======================================================================

def leer_json(ruta):
    """Formato de los archivos:

        {"P": ["1","2",...],
         "E": {"1": ["1","34","39",...], "2": [...], ...}}

    P = puntos (nodos).  E = por cada nodo, con quienes se relaciona: el
    primer elemento de cada lista es el propio nodo, es decir, el bucle
    a -> a (la relacion incluye a cada elemento consigo mismo).
    """
    with open(ruta, encoding="utf-8") as f:
        datos = json.load(f)

    g = Grafo(datos["P"])
    for origen, lista in datos["E"].items():
        for destino in lista:
            g.agregar(origen, destino)
    return g


# ======================================================================
# 3. Las cuatro propiedades
# ======================================================================
# Cada funcion devuelve (cumple, contraejemplo) para poder explicar el "no".

def es_reflexiva(g):
    faltan = [g.nodos[i] for i in range(g.n) if not (g.fila[i] >> i) & 1]
    return (not faltan), faltan[:5]


def es_simetrica(g):
    """M[i][j] == M[j][i]. Se compara la fila i contra la columna i:
    si son distintas, el primer bit en que difieren es el contraejemplo."""
    for i in range(g.n):
        dif = g.fila[i] ^ g.columna(i)
        if dif:
            j = (dif & -dif).bit_length() - 1
            if (g.fila[i] >> j) & 1:
                return False, (g.nodos[i], g.nodos[j])   # esta i->j, falta j->i
            return False, (g.nodos[j], g.nodos[i])
    return True, None


def es_antisimetrica(g):
    """Falla si estan i->j y j->i con i != j.
    fila_i AND columna_i = los j que van y vuelven; se ignora el bit i (bucle)."""
    for i in range(g.n):
        mutuos = g.fila[i] & g.columna(i)
        mutuos &= ~(1 << i)                  # los bucles no rompen antisimetria
        if mutuos:
            j = (mutuos & -mutuos).bit_length() - 1
            return False, (g.nodos[i], g.nodos[j])
    return True, None


def es_transitiva(g):
    """i->j y j->k  =>  i->k.

    Equivale a: para cada i, la union de las filas de sus sucesores tiene
    que estar CONTENIDA en la fila de i.

        union_sucesores  AND  NOT fila_i  != 0   =>  falta una arista
    """
    for i in range(g.n):
        fi = g.fila[i]
        union = 0
        for j in bits_indices(fi):
            union |= g.fila[j]
        faltante = union & ~fi
        if faltante:
            k = (faltante & -faltante).bit_length() - 1
            # busco un j que justifique el contraejemplo: i->j y j->k
            for j in bits_indices(fi):
                if (g.fila[j] >> k) & 1:
                    return False, (g.nodos[i], g.nodos[j], g.nodos[k])
    return True, None


def bits_indices(x):
    """Indices de los bits prendidos de x."""
    while x:
        b = x & -x
        yield b.bit_length() - 1
        x ^= b


def es_orden_total(g):
    """Un orden es TOTAL si todo par de elementos distintos es comparable."""
    todos = (1 << g.n) - 1
    for i in range(g.n):
        comparables = g.fila[i] | g.columna(i) | (1 << i)
        if comparables != todos:
            return False
    return True


# ======================================================================
# 4. Clasificacion + informe
# ======================================================================

def analizar(g):
    refl, c_refl = es_reflexiva(g)
    sim, c_sim = es_simetrica(g)
    anti, c_anti = es_antisimetrica(g)
    tra, c_tra = es_transitiva(g)

    if refl and anti and tra:
        clase = "ES UN ORDEN (relacion de orden: reflexiva + antisimetrica + transitiva)"
        total = es_orden_total(g)
    elif refl and sim and tra:
        clase = "ES UNA RELACION DE EQUIVALENCIA (reflexiva + simetrica + transitiva)"
        total = None
    else:
        clase = "NO es un orden NI una relacion de equivalencia"
        total = None

    return {
        "reflexiva": (refl, c_refl),
        "simetrica": (sim, c_sim),
        "antisimetrica": (anti, c_anti),
        "transitiva": (tra, c_tra),
        "clasificacion": clase,
        "orden_total": total,
    }


def informe(g, r):
    L = []
    L.append(f"  Grafo: {g}")
    L.append("")

    def fila(nombre, clave, explicar):
        cumple, contra = r[clave]
        L.append(f"  {nombre:<15} {'SI' if cumple else 'NO'}"
                 + (f"   ({explicar(contra)})" if not cumple and contra else ""))

    fila("Reflexiva", "reflexiva",
         lambda c: "falta el bucle en " + ", ".join(c) + ", ...")
    fila("Simetrica", "simetrica",
         lambda c: f"esta ({c[0]},{c[1]}) pero no ({c[1]},{c[0]})")
    fila("Antisimetrica", "antisimetrica",
         lambda c: f"estan ({c[0]},{c[1]}) y ({c[1]},{c[0]}) con {c[0]} != {c[1]}")
    fila("Transitiva", "transitiva",
         lambda c: f"estan ({c[0]},{c[1]}) y ({c[1]},{c[2]}) pero falta ({c[0]},{c[2]})")

    L.append("")
    L.append(f"  >> {r['clasificacion']}")
    if r["orden_total"] is not None:
        L.append(f"  >> Orden total: {'SI' if r['orden_total'] else 'NO, es solo parcial'}")
    return "\n".join(L)


# ======================================================================
# 5. Programa principal
# ======================================================================

def procesar(ruta):
    print("=" * 68)
    print(f"ARCHIVO: {os.path.basename(ruta)}")
    print("=" * 68)
    t = time.time()
    g = leer_json(ruta)
    r = analizar(g)
    print(informe(g, r))
    print(f"\n  [{time.time() - t:.1f} s]\n")


def main():
    rutas = sys.argv[1:]
    if not rutas:
        rutas = [f for f in ("01.json", "02.json", "03.json") if os.path.exists(f)]
    if not rutas:
        rutas = [input("Ruta del json: ").strip()]
    for ruta in rutas:
        procesar(ruta)


if __name__ == "__main__":
    main()
