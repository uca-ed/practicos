"""
Ejercicio 4 - Implementar RADIX SORT y ordenar las palabras de los archivos.
"""

from collections import deque


def leer_alfabetos(ruta):
    
    alfabetos = []
    with open(ruta, encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if not linea or linea.startswith("#"):
                continue
            alfabetos.append([s.strip() for s in linea.split(",")])
    return alfabetos


def leer_palabras(ruta):
    
    palabras = []
    with open(ruta, encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if not linea or linea.startswith("#"):
                continue
            palabras.append([s.strip() for s in linea.split(",")])
    return palabras


def mostrar(palabra):
    return "".join(f"{s:>3}" for s in palabra)


def radix_sort(palabras, alfabetos, verbose=True):
    p = len(alfabetos)          # cantidad de posiciones de cada palabra
    Q = deque(palabras)         # cola principal

    if verbose:
        print(f"Palabras de {p} posiciones. Alfabetos por posicion:")
        for i, a in enumerate(alfabetos):
            print(f"   posicion {p - i} (indice {i}):  {len(a):>2} simbolos -> {','.join(a)}")
        print()

    
    for j in range(1, p + 1):

        idx = p - j                 
        alfabeto = alfabetos[idx]
        r = len(alfabeto)

        
        cajitas = {simbolo: deque() for simbolo in alfabeto}

        
        while Q:
            X = Q.popleft()                 # dequeue de la cola principal
            s = X[idx]                      # simbolo de X en la posicion j
            if s not in cajitas:
                raise ValueError(
                    f"El simbolo '{s}' no pertenece al alfabeto de la posicion {j}")
            cajitas[s].append(X)            # enqueue en la cajita

        if verbose:
            print(f"--- Vuelta j={j}  (posicion {j}, {r} cajitas) ---")
            for simbolo in alfabeto:
                if cajitas[simbolo]:
                    contenido = "  |  ".join(",".join(w) for w in cajitas[simbolo])
                    print(f"   Q[{simbolo:>2}] : {contenido}")

        
        for simbolo in alfabeto:
            while cajitas[simbolo]:
                Q.append(cajitas[simbolo].popleft())

        if verbose:
            print(f"   => Q = " + "  |  ".join(",".join(w) for w in Q))
            print()

    return list(Q)


def esta_ordenada(palabras, alfabetos):
    
    rango = [{s: i for i, s in enumerate(a)} for a in alfabetos]

    def clave(w):
        return tuple(rango[i][s] for i, s in enumerate(w))

    return all(clave(palabras[k]) <= clave(palabras[k + 1])
               for k in range(len(palabras) - 1))


def ejecutar(ruta_alfabetos, ruta_palabras, verbose=True):
    alfabetos = leer_alfabetos(ruta_alfabetos)
    palabras = leer_palabras(ruta_palabras)

    if verbose:
        print("ENTRADA (desordenada):")
        for w in palabras:
            print("   " + ",".join(w))
        print()

    ordenadas = radix_sort(palabras, alfabetos, verbose=verbose)

    print("RESULTADO FINAL (ordenado):")
    for w in ordenadas:
        print("   " + ",".join(w))

    ok = esta_ordenada(ordenadas, alfabetos)
    print(f"\n  Verificacion de orden lexicografico: {'OK' if ok else 'FALLO'}")

    return ordenadas


if __name__ == "__main__":
    import os
    base = os.path.dirname(os.path.abspath(__file__))
    ejecutar(os.path.join(base, "datos", "alfabetos.txt"),
             os.path.join(base, "datos", "palabras.txt"))
