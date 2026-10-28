import random

EDIFICIOS = 4
PISOS = 5
ALAS = 2
AULAS = 25
BLOQUES = 85

TAMANIO = EDIFICIOS * PISOS * ALAS * AULAS * BLOQUES

INSCRIPTOS = [0] * TAMANIO
CAPACIDAD = [0] * TAMANIO


def posicion(edificio, piso, ala, aula, bloque):
    """Convierte cinco índices en un índice del arreglo lineal."""
    return (
        (((edificio * PISOS + piso) * ALAS + ala) * AULAS + aula)
        * BLOQUES + bloque
    )


def coordenadas(pos):
    """Operación inversa: índice lineal -> cinco coordenadas."""
    bloque = pos % BLOQUES
    pos //= BLOQUES

    aula = pos % AULAS
    pos //= AULAS

    ala = pos % ALAS
    pos //= ALAS

    piso = pos % PISOS
    pos //= PISOS

    edificio = pos

    return edificio, piso, ala, aula, bloque


def cargar_datos():
    # Semilla fija para que las pruebas sean reproducibles.
    random.seed(10)

    for edificio in range(EDIFICIOS):
        for piso in range(PISOS):
            for ala in range(ALAS):
                for aula in range(AULAS):
                    capacidad_aula = random.randint(20, 50)

                    for bloque in range(BLOQUES):
                        pos = posicion(edificio, piso, ala, aula, bloque)
                        CAPACIDAD[pos] = capacidad_aula
                        INSCRIPTOS[pos] = random.randint(0, capacidad_aula)


def mayor_ocupacion():
    mayor = -1.0
    mejor_pos = -1

    # Se recorre directamente la representación lineal.
    for i in range(TAMANIO):
        if CAPACIDAD[i] > 0:
            porcentaje = INSCRIPTOS[i] * 100 / CAPACIDAD[i]

            if porcentaje > mayor:
                mayor = porcentaje
                mejor_pos = i

    return mejor_pos, mayor


def promedio_por_piso(bloque_buscado):
    if bloque_buscado < 0 or bloque_buscado >= BLOQUES:
        raise ValueError("Bloque horario inválido.")

    suma = [0] * PISOS
    cantidad_aulas = [0] * PISOS

    # Para un bloque fijo, cada aula ocupa una posición cada BLOQUES
    # elementos. Así evitamos recorrer índices que pertenecen a otros bloques.
    for i in range(bloque_buscado, TAMANIO, BLOQUES):
        _, piso, _, _, _ = coordenadas(i)
        suma[piso] += INSCRIPTOS[i]
        cantidad_aulas[piso] += 1

    promedios = [0.0] * PISOS

    for piso in range(PISOS):
        if cantidad_aulas[piso] > 0:
            promedios[piso] = suma[piso] / cantidad_aulas[piso]

    return promedios


def alumnos_por_ala(edificio_buscado, piso_buscado, bloque_buscado):
    if not 0 <= edificio_buscado < EDIFICIOS:
        raise ValueError("Edificio inválido.")
    if not 0 <= piso_buscado < PISOS:
        raise ValueError("Piso inválido.")
    if not 0 <= bloque_buscado < BLOQUES:
        raise ValueError("Bloque horario inválido.")

    totales = [0] * ALAS

    # Se calcula el inicio lineal de cada ala y se recorren sólo sus aulas.
    for ala in range(ALAS):
        inicio = posicion(edificio_buscado, piso_buscado, ala, 0, bloque_buscado)

        for aula in range(AULAS):
            pos = inicio + aula * BLOQUES
            totales[ala] += INSCRIPTOS[pos]

    return totales


cargar_datos()

print("PUNTO A - MAYOR PORCENTAJE DE OCUPACIÓN")
pos, porcentaje = mayor_ocupacion()
e, p, ala, aula, bloque = coordenadas(pos)

print("Edificio:", e)
print("Piso:", p)
print("Ala:", "Norte" if ala == 0 else "Sur")
print("Aula:", aula)
print("Bloque:", bloque)
print("Inscriptos:", INSCRIPTOS[pos])
print("Capacidad:", CAPACIDAD[pos])
print("Ocupación: {:.2f}%".format(porcentaje))


print("\nPUNTO B - PROMEDIO DE ALUMNOS POR PISO")
bloque_consulta = 20
promedios = promedio_por_piso(bloque_consulta)

print("Bloque horario:", bloque_consulta)
for piso in range(PISOS):
    print("Piso {}: {:.2f}".format(piso, promedios[piso]))


print("\nPUNTO C - TOTAL DE ALUMNOS POR ALA")
edificio_consulta = 1
piso_consulta = 2
bloque_consulta = 20

totales = alumnos_por_ala(
    edificio_consulta,
    piso_consulta,
    bloque_consulta
)

print("Edificio:", edificio_consulta)
print("Piso:", piso_consulta)
print("Bloque:", bloque_consulta)
print("Ala norte:", totales[0])
print("Ala sur:", totales[1])
