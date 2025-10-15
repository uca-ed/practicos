import random
import time

# Dimensiones
EDIFICIOS = 4
PISOS = 5
ALAS = 2  # norte (0) y sur (1)
AULAS = 25
BLOQUES = 17  # por simplicidad (en lugar de 85)

# Tamaño total
TOTAL = EDIFICIOS * PISOS * ALAS * AULAS * BLOQUES


def indice_lineal(e, p, a, au, b):
    """Convierte coordenadas 5D a índice 1D"""
    return ((((e * PISOS + p) * ALAS + a) * AULAS + au) * BLOQUES) + b


def crear_estructuras():
    """Genera datos simulados para INSCRIPTOS y CAPACIDAD"""
    inscriptos = [random.randint(0, 30) for _ in range(TOTAL)]
    capacidad = [random.randint(30, 40) for _ in range(TOTAL)]
    return inscriptos, capacidad


def mayor_ocupacion(inscriptos, capacidad):
    """a) Aula/bloque horario con mayor porcentaje de ocupación"""
    max_porcentaje = -1
    mejor_pos = None

    for e in range(EDIFICIOS):
        for p in range(PISOS):
            for a in range(ALAS):
                for au in range(AULAS):
                    for b in range(BLOQUES):
                        i = indice_lineal(e, p, a, au, b)
                        if capacidad[i] > 0:
                            porc = (inscriptos[i] / capacidad[i]) * 100
                            if porc > max_porcentaje:
                                max_porcentaje = porc
                                mejor_pos = (e, p, a, au, b)
    print("\n a) Aula/bloque con mayor ocupacion:")
    print(f"Edificio {mejor_pos[0]}, Piso {mejor_pos[1]}, Ala {['Norte','Sur'][mejor_pos[2]]}, Aula {mejor_pos[3]}, Bloque {mejor_pos[4]}")
    print(f"Ocupacion: {max_porcentaje:.2f}%\n")


def promedio_por_piso(inscriptos, bloque):
    """b) Promedio de alumnos por piso (entre todos los edificios)"""
    print(f"b) Promedio de alumnos por piso en bloque {bloque}:")
    for piso in range(PISOS):
        total = 0
        aulas_contadas = 0
        for e in range(EDIFICIOS):
            for a in range(ALAS):
                for au in range(AULAS):
                    i = indice_lineal(e, piso, a, au, bloque)
                    total += inscriptos[i]
                    aulas_contadas += 1
        prom = total / aulas_contadas
        print(f"Piso {piso}: {prom:.2f} alumnos en promedio")
    print()


def alumnos_por_ala(inscriptos, edificio, piso, bloque):
    """c) Cantidad total de alumnos por ala"""
    totales = [0, 0]
    for a in range(ALAS):
        for au in range(AULAS):
            i = indice_lineal(edificio, piso, a, au, bloque)
            totales[a] += inscriptos[i]
    print(f"c) Edificio {edificio}, Piso {piso}, Bloque {bloque}")
    print(f"Ala Norte: {totales[0]} alumnos")
    print(f"Ala Sur: {totales[1]} alumnos\n")


def comparar_tiempos():
    """Simula comparación entre estructuras 1D y 5D"""
    print("Comparando tiempos de acceso...\n")

    # Datos aleatorios
    inscriptos, capacidad = crear_estructuras()

    # Estructura 1D
    t1 = time.time()
    _ = inscriptos[indice_lineal(1, 2, 0, 10, 5)]
    t2 = time.time()

    # Estructura 5D (listas anidadas)
    estructura5D = [[[[[random.randint(0, 30) for _ in range(BLOQUES)]
                        for _ in range(AULAS)] for _ in range(ALAS)]
                        for _ in range(PISOS)] for _ in range(EDIFICIOS)]

    t3 = time.time()
    _ = estructura5D[1][2][0][10][5]
    t4 = time.time()

    print(f"Acceso 1D: {(t2 - t1)*1e6:.3f} microsegundos")
    print(f"Acceso 5D: {(t4 - t3)*1e6:.3f} microsegundos\n")


def main():
    inscriptos, capacidad = crear_estructuras()

    mayor_ocupacion(inscriptos, capacidad)
    promedio_por_piso(inscriptos, bloque=5)
    alumnos_por_ala(inscriptos, edificio=2, piso=3, bloque=4)
    comparar_tiempos()


main()
