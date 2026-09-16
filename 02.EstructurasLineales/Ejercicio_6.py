import random
N_EDIF   = 4
N_PISO   = 5
N_ALA    = 2
N_AULA   = 25
N_BLOQUE = 85

TOTAL = N_EDIF * N_PISO * N_ALA * N_AULA * N_BLOQUE  # 170000


def indice(i0, i1, i2, i3, i4):
    # idx = i4 + N_BLOQUE*( i3 + N_AULA*( i2 + N_ALA*( i1 + N_PISO*i0 ) ) )
    return i4 + N_BLOQUE * (i3 + N_AULA * (i2 + N_ALA * (i1 + N_PISO * i0)))


INSCRIPTOS = [0] * TOTAL
CAPACIDAD = [0] * TOTAL

random.seed(0) 

for i0 in range(N_EDIF):
    for i1 in range(N_PISO):
        for i2 in range(N_ALA):
            for i3 in range(N_AULA):
                capacidad_aula = random.randint(20, 40)
                for i4 in range(N_BLOQUE):
                    idx = indice(i0, i1, i2, i3, i4)
                    CAPACIDAD[idx] = capacidad_aula
                    INSCRIPTOS[idx] = random.randint(0, capacidad_aula)

print("Estructuras creadas y cargadas. Tamaño de cada arreglo:", TOTAL)

mejor_idx = -1
mejor_porcentaje = -1.0

for idx in range(TOTAL):
    if CAPACIDAD[idx] > 0:
        porcentaje = INSCRIPTOS[idx] / CAPACIDAD[idx]
        if porcentaje > mejor_porcentaje:
            mejor_porcentaje = porcentaje
            mejor_idx = idx

# usando la formula inversa (divisiones sucesivas)
resto = mejor_idx
i4 = resto % N_BLOQUE; resto //= N_BLOQUE
i3 = resto % N_AULA;   resto //= N_AULA
i2 = resto % N_ALA;    resto //= N_ALA
i1 = resto % N_PISO;   resto //= N_PISO
i0 = resto

print("\n--- a) Mayor porcentaje de ocupacion ---")
print("Edificio:", i0, "Piso:", i1, "Ala:", "norte" if i2 == 0 else "sur",
      "Aula:", i3, "Bloque horario:", i4)
print("Ocupacion: %.1f%%" % (mejor_porcentaje * 100))
print("Inscriptos:", INSCRIPTOS[mejor_idx], "/ Capacidad:", CAPACIDAD[mejor_idx])


def promedio_por_piso(bloque):
    resultado = []  # lista de (piso, promedio)
    for i1 in range(N_PISO):
        suma = 0
        cantidad = 0
        for i0 in range(N_EDIF):
            for i2 in range(N_ALA):
                for i3 in range(N_AULA):
                    idx = indice(i0, i1, i2, i3, bloque)
                    suma += INSCRIPTOS[idx]
                    cantidad += 1
        resultado.append((i1, suma / cantidad))
    return resultado


bloque_parametro = 10 
print("\n--- b) Promedio de alumnos por piso (bloque =", bloque_parametro, ") ---")
for piso, promedio in promedio_por_piso(bloque_parametro):
    print("Piso", piso, "-> promedio:", round(promedio, 2))

def total_por_ala(edificio, piso, bloque):
    resultado = []  # lista de (ala, total)
    for i2 in range(N_ALA):
        suma = 0
        for i3 in range(N_AULA):
            idx = indice(edificio, piso, i2, i3, bloque)
            suma += INSCRIPTOS[idx]
        resultado.append((i2, suma))
    return resultado


edificio_parametro = 1
piso_parametro = 2
bloque_parametro_c = 10
print("\n--- c) Total de alumnos por ala (edificio =", edificio_parametro,
      ", piso =", piso_parametro, ", bloque =", bloque_parametro_c, ") ---")
for ala, total in total_por_ala(edificio_parametro, piso_parametro, bloque_parametro_c):
    print("Ala", "norte" if ala == 0 else "sur", "-> total alumnos:", total)
