import random


EDIFICIOS = 4
PISOS = 5
ALAS = 2
AULAS = 25
BLOQUES = 85


TOTAL = 4 * 5 * 2 * 25 * 85


def index(e, p, a, au, b):
    return ((((e * PISOS) + p) * ALAS + a) * AULAS + au) * BLOQUES + b


INSCRIPTOS = [0] * TOTAL
CAPACIDAD = [0] * TOTAL

for e in range(EDIFICIOS):
    for p in range(PISOS):
        for a in range(ALAS):
            for au in range(AULAS):
                cap_base = random.randint(20, 60)
                for b in range(BLOQUES):
                    i = index(e, p, a, au, b)
                    CAPACIDAD[i] = cap_base
                    INSCRIPTOS[i] = random.randint(0, cap_base)

max_porcentaje = -1
max_indices = None

for e in range(EDIFICIOS):
    for p in range(PISOS):
        for a in range(ALAS):
            for au in range(AULAS):
                for b in range(BLOQUES):
                    i = index(e, p, a, au, b)
                    if CAPACIDAD[i] > 0:
                        porc = INSCRIPTOS[i] / CAPACIDAD[i]
                        if porc > max_porcentaje:
                            max_porcentaje = porc
                            max_indices = (e, p, a, au, b)

print(f"a) Aula/bloque con mayor ocupación: {max_indices} ({max_porcentaje*100:.2f}%)")


def promedio_por_piso(bloque):
    promedios = []
    for p in range(PISOS):
        total = 0
        cuenta = 0
        for e in range(EDIFICIOS):
            for a in range(ALAS):
                for au in range(AULAS):
                    i = index(e, p, a, au, bloque)
                    total += INSCRIPTOS[i]
                    cuenta += 1
        promedios.append(total / cuenta)
    return promedios

bloque_test = random.randint(0, BLOQUES - 1)
promedios = promedio_por_piso(bloque_test)
print(f"\nb) Promedios de alumnos por piso en bloque {bloque_test}:")
for i, prom in enumerate(promedios):
    print(f"   Piso {i}: {prom:.2f} alumnos en promedio")

def total_por_ala(edificio, piso, bloque):
    totales = [0] * ALAS
    for a in range(ALAS):
        for au in range(AULAS):
            i = index(edificio, piso, a, au, bloque)
            totales[a] += INSCRIPTOS[i]
    return totales

piso_test = random.randint(0, PISOS - 1)
ed_test = random.randint(0, EDIFICIOS - 1)
ed, piso, bloque = ed_test, piso_test, bloque_test
totales = total_por_ala(ed, piso, bloque)
print(f"\nc) En el edificio {ed}, piso {piso}, bloque {bloque}:")
print(f"   Ala norte: {totales[0]} alumnos")
print(f"   Ala sur:   {totales[1]} alumnos")
