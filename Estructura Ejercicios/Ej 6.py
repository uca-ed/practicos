import random
import time
from collections import defaultdict

# Dimensiones
D0, D1, D2, D3, D4 = 4, 5, 2, 25, 85
TAM = D0 * D1 * D2 * D3 * D4

# Arreglos 1D que simulan las 5 dimensiones
INSCRIPTOS = [0] * TAM
CAPACIDAD = [0] * TAM

# Devuelve índice lineal desde coordenadas 5D
def index(edificio, piso, ala, aula, bloque):
    return (((edificio * D1 + piso) * D2 + ala) * D3 + aula) * D4 + bloque

# Carga de datos aleatorios
def cargar_datos():
    for e in range(D0):
        for p in range(D1):
            for a in range(D2):
                for au in range(D3):
                    for b in range(D4):
                        idx = index(e, p, a, au, b)
                        cap = random.randint(20, 60)
                        CAPACIDAD[idx] = cap
                        INSCRIPTOS[idx] = random.randint(int(cap * 0.5), cap)

# a) Aula/bloque con mayor % de ocupación
def max_ocupacion():
    max_porcentaje = -1
    aula_max = None
    for e in range(D0):
        for p in range(D1):
            for a in range(D2):
                for au in range(D3):
                    for b in range(D4):
                        idx = index(e, p, a, au, b)
                        cap = CAPACIDAD[idx]
                        if cap == 0:
                            continue
                        porcentaje = INSCRIPTOS[idx] / cap
                        if porcentaje > max_porcentaje:
                            max_porcentaje = porcentaje
                            aula_max = (e, p, a, au, b)
    return aula_max, max_porcentaje

# b) Promedio de alumnos por piso en un bloque horario
def promedio_por_piso(bloque):
    if not (0 <= bloque < D4):
        raise ValueError("Bloque fuera de rango")
    promedios = []
    for p in range(D1):
        total = sum(
            INSCRIPTOS[index(e, p, a, au, bloque)]
            for e in range(D0)
            for a in range(D2)
            for au in range(D3)
        )
        cantidad = D0 * D2 * D3
        promedios.append(total / cantidad)
    return promedios

# c) Total de alumnos por ala en un edificio, piso y bloque
def alumnos_por_ala(edificio, piso, bloque):
    if not (0 <= bloque < D4):
        raise ValueError("Bloque fuera de rango")
    resultado = {"Norte": 0, "Sur": 0}
    for a in range(D2):
        clave = "Norte" if a == 0 else "Sur"
        resultado[clave] = sum(
            INSCRIPTOS[index(edificio, piso, a, au, bloque)] for au in range(D3)
        )
    return resultado

# Ejecución principal
def main():
    cargar_datos()

    print("\nResultados de consultas sobre datos universitarios\n")

    # Total en bloque 10
    total_b10 = sum(
        INSCRIPTOS[index(e, p, a, au, 10)]
        for e in range(D0)
        for p in range(D1)
        for a in range(D2)
        for au in range(D3)
    )
    print(f"Total inscriptos en bloque 10: {total_b10}")

    # a)
    t1 = time.time()
    aula, porcentaje = max_ocupacion()
    t1 = time.time() - t1
    print(f"\nAula más ocupada: {aula} con {porcentaje*100:.2f}%")

    # b)
    bloque = 10
    t2 = time.time()
    promedios = promedio_por_piso(bloque)
    t2 = time.time() - t2
    print(f"\nPromedios por piso en bloque {bloque}:")
    for i, val in enumerate(promedios):
        print(f"   Piso {i}: {val:.2f} alumnos")

    # c)
    edificio, piso, bloque = 2, 3, 20
    t3 = time.time()
    totales = alumnos_por_ala(edificio, piso, bloque)
    t3 = time.time() - t3
    print(f"\nAlumnos por ala en Edificio {edificio}, Piso {piso}, Bloque {bloque}:")
    print(totales)


main()