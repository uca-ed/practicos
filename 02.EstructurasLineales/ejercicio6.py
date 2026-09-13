# Ejercicio 6 - Arreglos k-dimensionales sobre un arreglo de una dimension.
#
# INSCRIPTOS y CAPACIDAD son arreglos de 5 dimensiones:
#   d0: edificio       (4)
#   d1: piso           (5)
#   d2: ala            (2: 0 = norte, 1 = sur)
#   d3: aula           (25)
#   d4: bloque horario (85 = 17 bloques por 5 dias)
#
# Se guardan linealizados en un unico arreglo, con la formula
#   h(i0..i4) = i0*p0 + i1*p1 + i2*p2 + i3*p3 + i4*p4
# donde pj es el producto de las dimensiones que vienen despues de j.
#
# Las consultas trabajan sobre el arreglo lineal: en vez de anidar 5 ciclos
# se recorren las posiciones salteando de a pasos[j].

import random

DIMENSIONES = [4, 5, 2, 25, 85]
NOMBRES_ALA = ["norte", "sur"]


def calcular_pasos(dimensiones):
    """pasos[j] = dimensiones[j+1] * ... * dimensiones[k-1]."""
    k = len(dimensiones)
    pasos = [1] * k
    for j in range(k - 2, -1, -1):
        pasos[j] = pasos[j + 1] * dimensiones[j + 1]
    return pasos


PASOS = calcular_pasos(DIMENSIONES)
TAMANIO = DIMENSIONES[0] * PASOS[0]


def h(indices):
    """Pasa de indices multidimensionales a la posicion en el arreglo lineal."""
    pos = 0
    for j in range(len(indices)):
        pos += indices[j] * PASOS[j]
    return pos


def h_inversa(pos):
    """Pasa de una posicion del arreglo lineal a los indices originales."""
    indices = []
    for j in range(len(DIMENSIONES)):
        indices.append(pos // PASOS[j])
        pos = pos % PASOS[j]
    return indices


def crear_estructuras():
    """Genera los datos, porque el TP no provee archivo."""
    random.seed(42)   # asi los resultados se pueden repetir

    inscriptos = [0] * TAMANIO
    capacidad = [0] * TAMANIO

    for edificio in range(DIMENSIONES[0]):
        for piso in range(DIMENSIONES[1]):
            for ala in range(DIMENSIONES[2]):
                for aula in range(DIMENSIONES[3]):
                    # la capacidad es del aula, es la misma en todos los bloques
                    cap = random.randint(20, 120)
                    base = h([edificio, piso, ala, aula, 0])
                    for bloque in range(DIMENSIONES[4]):
                        pos = base + bloque * PASOS[4]
                        capacidad[pos] = cap
                        # hay bloques vacios (aula sin clase) y bloques con gente
                        if random.random() < 0.35:
                            inscriptos[pos] = 0
                        else:
                            inscriptos[pos] = random.randint(1, cap)

    return inscriptos, capacidad


def mayor_porcentaje_de_ocupacion(inscriptos, capacidad):
    """a) aula / bloque horario con mayor porcentaje de ocupacion."""
    mejor_pos = -1
    mejor_porcentaje = -1.0

    for pos in range(TAMANIO):
        if capacidad[pos] == 0:
            continue
        porcentaje = inscriptos[pos] * 100.0 / capacidad[pos]
        if porcentaje > mejor_porcentaje:
            mejor_porcentaje = porcentaje
            mejor_pos = pos

    return h_inversa(mejor_pos), mejor_porcentaje


def promedio_por_piso(inscriptos, bloque):
    """b) promedio de alumnos por piso en un bloque, entre todos los edificios."""
    promedios = []

    for piso in range(DIMENSIONES[1]):
        total = 0
        cantidad = 0
        for edificio in range(DIMENSIONES[0]):
            for ala in range(DIMENSIONES[2]):
                base = h([edificio, piso, ala, 0, bloque])
                for aula in range(DIMENSIONES[3]):
                    total += inscriptos[base + aula * PASOS[3]]
                    cantidad += 1
        promedios.append(total / cantidad)

    return promedios


def alumnos_por_ala(inscriptos, edificio, piso, bloque):
    """c) total de alumnos en cada ala, para un edificio/piso/bloque dado."""
    totales = []

    for ala in range(DIMENSIONES[2]):
        total = 0
        base = h([edificio, piso, ala, 0, bloque])
        for aula in range(DIMENSIONES[3]):
            total += inscriptos[base + aula * PASOS[3]]
        totales.append(total)

    return totales


if __name__ == "__main__":
    print("Dimensiones:", DIMENSIONES)
    print("Pasos:", PASOS)
    print("Tamaño del arreglo lineal:", TAMANIO)

    inscriptos, capacidad = crear_estructuras()
    print("Estructuras cargadas.")

    print()
    print("a) Aula/bloque con mayor porcentaje de ocupacion")
    indices, porcentaje = mayor_porcentaje_de_ocupacion(inscriptos, capacidad)
    pos = h(indices)
    print("   edificio %d, piso %d, ala %s, aula %d, bloque %d"
          % (indices[0], indices[1], NOMBRES_ALA[indices[2]],
             indices[3], indices[4]))
    print("   %d inscriptos sobre %d de capacidad (%.1f%%)"
          % (inscriptos[pos], capacidad[pos], porcentaje))

    bloque = 20
    print()
    print("b) Promedio de alumnos por piso en el bloque horario", bloque)
    promedios = promedio_por_piso(inscriptos, bloque)
    for piso in range(len(promedios)):
        print("   piso %d: %.2f alumnos por aula" % (piso, promedios[piso]))

    edificio, piso = 2, 3
    print()
    print("c) Alumnos por ala en edificio %d, piso %d, bloque %d"
          % (edificio, piso, bloque))
    totales = alumnos_por_ala(inscriptos, edificio, piso, bloque)
    for ala in range(len(totales)):
        print("   ala %s: %d alumnos" % (NOMBRES_ALA[ala], totales[ala]))
