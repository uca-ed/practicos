"""
Ejercicio 6: modelizacion de "INSCRIPTOS" (y "CAPACIDAD") como un arreglo
de 5 dimensiones, representado internamente sobre un arreglo de una sola
dimension mediante la funcion de hash:

    h(n1,...,nk, i1,...,ik) = sum_{j=0}^{k-1} [ i_j * prod_{w=j+1}^{k-1} n_w ]

Dimensiones utilizadas (d0..d4):
    d0: edificio        (4 edificios)
    d1: piso            (5 pisos por edificio)
    d2: ala             (2: norte o sur)
    d3: aula            (25 aulas por ala)
    d4: bloque horario  (85: 17 bloques horarios x 5 dias)

No se provee un archivo de datos, asi que se generan datos aleatorios
para ambos arreglos.
"""

import os
import random

DIMENSIONES = (4, 5, 2, 25, 85)  # (edificio, piso, ala, aula, bloque_horario)


# ---------------------------------------------------------------------------
# Funcion de mapeo h y su inversa
# ---------------------------------------------------------------------------

def h(dims, indices):
    """Convierte un vector de indices k-dimensional a un indice lineal."""
    total = 0
    k = len(dims)
    for j in range(k):
        producto = 1
        for w in range(j + 1, k):
            producto *= dims[w]
        total += indices[j] * producto
    return total


def h_inv(dims, idx):
    """Convierte un indice lineal en su vector de indices k-dimensional."""
    k = len(dims)
    indices = [0] * k
    for j in range(k - 1, -1, -1):
        indices[j] = idx % dims[j]
        idx //= dims[j]
    return tuple(indices)


# ---------------------------------------------------------------------------
# Creacion y carga de las estructuras
# ---------------------------------------------------------------------------

def crear_arreglo(dims, valor_inicial=0):
    tamanio = 1
    for d in dims:
        tamanio *= d
    return [valor_inicial] * tamanio


def cargar_datos_aleatorios(dims, seed=None):
    if seed is not None:
        random.seed(seed)
    capacidad = crear_arreglo(dims)
    inscriptos = crear_arreglo(dims)
    for idx in range(len(capacidad)):
        cap = random.randint(20, 50)
        capacidad[idx] = cap
        inscriptos[idx] = random.randint(0, cap)
    return inscriptos, capacidad


# ---------------------------------------------------------------------------
# a) Aula/bloque horario con mayor porcentaje de ocupacion
# ---------------------------------------------------------------------------

def mayor_ocupacion(inscriptos, capacidad, dims):
    mejor_idx = None
    mejor_pct = -1
    for idx in range(len(inscriptos)):
        if capacidad[idx] > 0:
            pct = inscriptos[idx] / capacidad[idx]
            if pct > mejor_pct:
                mejor_pct = pct
                mejor_idx = idx
    edificio, piso, ala, aula, bloque = h_inv(dims, mejor_idx)
    return {
        "edificio": edificio,
        "piso": piso,
        "ala": ala,
        "aula": aula,
        "bloque_horario": bloque,
        "porcentaje_ocupacion": round(mejor_pct * 100, 2),
    }


# ---------------------------------------------------------------------------
# b) Promedio de alumnos por piso en un bloque horario dado (entre todos
#    los edificios) -> 5 promedios (uno por piso)
#
# En vez de recorrer con 4 indices anidados (edificio, piso, ala, aula),
# se recorre directamente el arreglo lineal: para un bloque fijo, los
# indices validos son idx = X * n_bloque + bloque, con X variando sobre
# todas las combinaciones de (edificio, piso, ala, aula). El piso se
# obtiene a partir de X por cociente/resto, sin reconstruir todos los
# indices.
# ---------------------------------------------------------------------------

def promedio_por_piso(inscriptos, dims, bloque):
    n_edificio, n_piso, n_ala, n_aula, n_bloque = dims
    sumas = [0] * n_piso
    cantidades = [0] * n_piso

    tam_reducido = n_edificio * n_piso * n_ala * n_aula
    for x in range(tam_reducido):
        idx = x * n_bloque + bloque
        piso = (x // (n_ala * n_aula)) % n_piso
        sumas[piso] += inscriptos[idx]
        cantidades[piso] += 1

    return [round(sumas[p] / cantidades[p], 2) for p in range(n_piso)]


# ---------------------------------------------------------------------------
# c) Dado edificio, piso y bloque horario, total de alumnos por ala
#
# Se recorre el arreglo lineal con un paso fijo de n_bloque (una posicion
# por cada aula dentro del ala), sin generar los 5 indices completos en
# cada iteracion.
# ---------------------------------------------------------------------------

def total_por_ala(inscriptos, dims, edificio, piso, bloque):
    n_edificio, n_piso, n_ala, n_aula, n_bloque = dims
    resultado = [0] * n_ala
    base = (edificio * n_piso + piso) * n_ala

    for ala in range(n_ala):
        idx_inicio = (base + ala) * n_aula * n_bloque + bloque
        total = 0
        for aula in range(n_aula):
            total += inscriptos[idx_inicio + aula * n_bloque]
        resultado[ala] = total

    return resultado


if __name__ == "__main__":
    inscriptos, capacidad = cargar_datos_aleatorios(DIMENSIONES, seed=42)
    print(f"Dimensiones: {DIMENSIONES}")
    print(f"Tamanio del arreglo lineal: {len(inscriptos)}\n")

    print("a) Aula/bloque horario con mayor porcentaje de ocupacion:")
    print(" ", mayor_ocupacion(inscriptos, capacidad, DIMENSIONES))

    print("\nb) Promedio de alumnos por piso en el bloque horario 10 (todos los edificios):")
    print(" ", promedio_por_piso(inscriptos, DIMENSIONES, bloque=10))

    print("\nc) Total de alumnos por ala (edificio=1, piso=2, bloque=10):")
    print(" ", total_por_ala(inscriptos, DIMENSIONES, edificio=1, piso=2, bloque=10))
