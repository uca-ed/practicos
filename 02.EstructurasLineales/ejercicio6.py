import random
import numpy as np

EDIFICIOS = 4
PISOS = 5
ALAS = 2
AULAS = 25
BLOQUES = 85 
TOTAL = EDIFICIOS * PISOS * ALAS * AULAS * BLOQUES

def indexar(e, p, a, au, b):
    """Convierte los 5 índices en un índice lineal para un arreglo 1D"""
    return ((((e * PISOS + p) * ALAS + a) * AULAS + au) * BLOQUES) + b

inscriptos = np.zeros(TOTAL, dtype=int)
capacidad = np.zeros(TOTAL, dtype=int)

for e in range(EDIFICIOS):
    for p in range(PISOS):
        for a in range(ALAS):
            for au in range(AULAS):
                for b in range(BLOQUES):
                    idx = indexar(e, p, a, au, b)
                    capacidad[idx] = random.randint(20, 100)
                    inscriptos[idx] = random.randint(0, capacidad[idx])

def mayor_ocupacion():
    ocupacion = inscriptos / capacidad
    max_idx = np.argmax(ocupacion)
    porcentaje = ocupacion[max_idx] * 100

    # Convertir índice lineal a coordenadas 5D
    b = max_idx % BLOQUES
    au = (max_idx // BLOQUES) % AULAS
    a = (max_idx // (AULAS * BLOQUES)) % ALAS
    p = (max_idx // (ALAS * AULAS * BLOQUES)) % PISOS
    e = (max_idx // (PISOS * ALAS * AULAS * BLOQUES)) % EDIFICIOS

    return (e, p, a, au, b, porcentaje)


def promedio_por_piso(bloque):
    promedios = []
    for p in range(PISOS):
        total_alumnos = 0
        total_aulas = 0
        for e in range(EDIFICIOS):
            for a in range(ALAS):
                for au in range(AULAS):
                    idx = indexar(e, p, a, au, bloque)
                    total_alumnos += inscriptos[idx]
                    total_aulas += 1
        promedio = total_alumnos / total_aulas
        promedios.append(promedio)
    return promedios

def total_por_ala(edificio, piso, bloque):
    totales = []
    for a in range(ALAS):
        total = 0
        for au in range(AULAS):
            idx = indexar(edificio, piso, a, au, bloque)
            total += inscriptos[idx]
        totales.append(total)
    return totales

print("a) Aula/bloque con mayor porcentaje de ocupación:")
e, p, a, au, b, porc = mayor_ocupacion()
print(f"   Edificio {e}, Piso {p}, Ala {'Norte' if a==0 else 'Sur'}, Aula {au}, Bloque {b} → {porc:.2f}% ocupado")

print("\nb) Promedio de alumnos por piso en bloque 10:")
for i, prom in enumerate(promedio_por_piso(10)):
    print(f"   Piso {i}: {prom:.2f} alumnos en promedio")

print("\nc) Total de alumnos por ala (edif 2, piso 3, bloque 10):")
totales = total_por_ala(2, 3, 10)
print(f"   Ala Norte: {totales[0]} alumnos")
print(f"   Ala Sur: {totales[1]} alumnos")
