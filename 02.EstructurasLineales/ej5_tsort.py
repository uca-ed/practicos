"""
Ejercicio 5 - T-SORT (ordenamiento topologico) sobre un grafo leido de disco.

"""

from collections import deque


class Grafo:
    

    def __init__(self):
        self.P = []          
        self.E = []          
        self.L = {}          
        self.R = {}          

    def agregar_nodo(self, x):
        if x not in self.L:
            self.P.append(x)
            self.L[x] = []
            self.R[x] = []

    def agregar_arco(self, x, y):
        self.agregar_nodo(x)
        self.agregar_nodo(y)
        if (x, y) not in self.E:
            self.E.append((x, y))
            self.R[x].append(y)
            self.L[y].append(x)

    def Min(self):
        
        return [x for x in self.P if not self.L[x]]

    def Max(self):
        
        return [x for x in self.P if not self.R[x]]


def leer_grafo(ruta):
    g = Grafo()
    with open(ruta, encoding="utf-8") as f:
        for nro, linea in enumerate(f, 1):
            linea = linea.strip()
            if not linea or linea.startswith("#"):
                continue
            partes = [p.strip() for p in linea.split(",")]
            tipo = partes[0].upper()

            if tipo == "NODO" and len(partes) >= 2:
                g.agregar_nodo(partes[1])
            elif tipo == "ARCO" and len(partes) >= 3:
                g.agregar_arco(partes[1], partes[2])
            else:
                raise ValueError(f"Linea {nro} mal formada: {linea!r}")
    return g


def t_sort(g, verbose=True):
    gradoEnt = {y: len(g.L[y]) for y in g.P}

    
    Q = deque([y for y in g.P if gradoEnt[y] == 0])
    ST = []

    if verbose:
        print(f"{'Vuelta':<8}{'Sale':<7}{'Bajo contadores de R(x)':<34}{'Q despues'}")
        print("-" * 78)

    vuelta = 0
    while Q:
        vuelta += 1
        x = Q.popleft()
        ST.append(x)

        cambios = []
        for y in g.R[x]:
            gradoEnt[y] = gradoEnt[y] - 1
            cambios.append(f"{y}: {gradoEnt[y] + 1}->{gradoEnt[y]}")
            if gradoEnt[y] == 0:
                Q.append(y)

        if verbose:
            desc = "   ".join(cambios) if cambios else "-"
            print(f"{vuelta:<8}{x:<7}{desc:<34}{list(Q)}")

    es_ciclico = len(ST) < len(g.P)
    return ST, es_ciclico, gradoEnt


def ejecutar(ruta, verbose=True):
    g = leer_grafo(ruta)

    print(f"Archivo: {ruta}")
    print(f"  P ({len(g.P)} nodos) = {{{', '.join(g.P)}}}")
    print(f"  E ({len(g.E)} arcos) = {{{', '.join(f'({x},{y})' for x, y in g.E)}}}")
    print(f"  Min(G) = {{{', '.join(g.Min())}}}      Max(G) = {{{', '.join(g.Max())}}}")
    print()

    if verbose:
        print(f"{'x':<5}{'L(x)':<20}{'R(x)':<20}{'|L(x)|'}")
        print("-" * 55)
        for x in g.P:
            print(f"{x:<5}{('{' + ', '.join(g.L[x]) + '}' if g.L[x] else 'vacia'):<20}"
                  f"{('{' + ', '.join(g.R[x]) + '}' if g.R[x] else 'vacia'):<20}{len(g.L[x])}")
        print()

    ST, es_ciclico, gradoEnt = t_sort(g, verbose=verbose)
    print("-" * 78)

    print("\nRESULTADO")
    if es_ciclico:
        trabados = [y for y in g.P if gradoEnt[y] > 0]
        print("  LA ESTRUCTURA ES CICLICA: no existe orden topologico.")
        print(f"  Se ordenaron {len(ST)} de {len(g.P)} nodos: ST parcial = "
              f"< {', '.join(ST) if ST else ''} >")
        print(f"  Nodos trabados dentro del ciclo: {{{', '.join(trabados)}}}")
    else:
        print(f"  Secuencia t-sort:  ST = < {', '.join(ST)} >")
        print(f"  |ST| = {len(ST)} = |P|  -> el grafo es aciclico, el orden es valido.")

        # verificacion: todo arco (x,y) debe tener x antes que y en ST
        pos = {n: i for i, n in enumerate(ST)}
        ok = all(pos[x] < pos[y] for x, y in g.E)
        print(f"  Verificacion (todo arco x->y con x antes que y): {'OK' if ok else 'FALLO'}")

    print(f"\n  El grafo quedo intacto: {len(g.P)} nodos y {len(g.E)} arcos "
          f"(algoritmo no destructivo).")

    return ST, es_ciclico


if __name__ == "__main__":
    import os
    base = os.path.dirname(os.path.abspath(__file__))

    print("=" * 78)
    print(" CASO 1 - grafo aciclico")
    print("=" * 78)
    ejecutar(os.path.join(base, "datos", "grafo.txt"))

    print("\n" + "=" * 78)
    print(" CASO 2 - grafo con ciclo")
    print("=" * 78)
    ejecutar(os.path.join(base, "datos", "grafo_ciclico.txt"))
