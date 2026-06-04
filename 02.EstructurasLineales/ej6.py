import random

D0_EDIFICIOS   = 4
D1_PISOS       = 5
D2_ALAS        = 2   # 0=norte, 1=sur
D3_AULAS       = 25
D4_BLOQUES     = 17  # 85 bloques / 5 días

# Tamaño total del arreglo lineal
TOTAL_INSCRIPTOS = D0_EDIFICIOS * D1_PISOS * D2_ALAS * D3_AULAS * D4_BLOQUES
TOTAL_CAPACIDAD  = D0_EDIFICIOS * D1_PISOS * D2_ALAS * D3_AULAS

def indice_inscriptos(edificio, piso, ala, aula, bloque):
    return (edificio * D1_PISOS * D2_ALAS * D3_AULAS * D4_BLOQUES +
            piso     * D2_ALAS * D3_AULAS * D4_BLOQUES +
            ala      * D3_AULAS * D4_BLOQUES +
            aula     * D4_BLOQUES +
            bloque)

def indice_capacidad(edificio, piso, ala, aula):
    return (edificio * D1_PISOS * D2_ALAS * D3_AULAS +
            piso     * D2_ALAS * D3_AULAS +
            ala      * D3_AULAS +
            aula)

def crear_estructuras():
    # Capacidad: entre 20 y 60 alumnos por aula
    CAPACIDAD = [random.randint(20, 60) for _ in range(TOTAL_CAPACIDAD)]

    # Inscriptos: entre 0 y la capacidad del aula
    INSCRIPTOS = []
    for edificio in range(D0_EDIFICIOS):
        for piso in range(D1_PISOS):
            for ala in range(D2_ALAS):
                for aula in range(D3_AULAS):
                    cap = CAPACIDAD[indice_capacidad(edificio, piso, ala, aula)]
                    for bloque in range(D4_BLOQUES):
                        INSCRIPTOS.append(random.randint(0, cap))

    return INSCRIPTOS, CAPACIDAD

# Aula/bloque con mayor porcentaje de ocupación

def mayor_porcentaje_ocupacion(INSCRIPTOS, CAPACIDAD):
    max_porcentaje = -1
    mejor = None

    for edificio in range(D0_EDIFICIOS):
        for piso in range(D1_PISOS):
            for ala in range(D2_ALAS):
                for aula in range(D3_AULAS):
                    cap = CAPACIDAD[indice_capacidad(edificio, piso, ala, aula)]
                    if cap == 0:
                        continue
                    for bloque in range(D4_BLOQUES):
                        idx = indice_inscriptos(edificio, piso, ala, aula, bloque)
                        porcentaje = (INSCRIPTOS[idx] / cap) * 100
                        if porcentaje > max_porcentaje:
                            max_porcentaje = porcentaje
                            mejor = (edificio, piso, ala, aula, bloque)

    e, p, a, au, b = mejor
    print("a. Mayor porcentaje de ocupación")
    print(f"  Edificio: {e} | Piso: {p} | Ala: {'Norte' if a==0 else 'Sur'} | Aula: {au} | Bloque: {b}")
    print(f"  Inscriptos: {INSCRIPTOS[indice_inscriptos(*mejor)]}")
    print(f"  Capacidad:  {CAPACIDAD[indice_capacidad(e, p, a, au)]}")
    print(f"  Ocupación:  {max_porcentaje:.2f}%")

# Promedio de alumnos por piso en un bloque horario dado

def promedio_por_piso(INSCRIPTOS, bloque):
    print(f"\nb. Promedio de alumnos por piso (bloque {bloque})")

    for piso in range(D1_PISOS):
        total = 0
        cantidad = 0
        # Iterar solo sobre los índices lineales que corresponden a este piso y bloque
        for edificio in range(D0_EDIFICIOS):
            for ala in range(D2_ALAS):
                for aula in range(D3_AULAS):
                    idx = indice_inscriptos(edificio, piso, ala, aula, bloque)
                    total += INSCRIPTOS[idx]
                    cantidad += 1

        promedio = total / cantidad if cantidad > 0 else 0
        print(f"  Piso {piso}: promedio = {promedio:.2f} alumnos")

# Total de alumnos por ala dado edificio, piso y bloque

def total_por_ala(INSCRIPTOS, edificio, piso, bloque):
    print(f"\nc. Total por ala (Edificio {edificio}, Piso {piso}, Bloque {bloque})")

    for ala in range(D2_ALAS):
        total = 0
        # Índices lineales que corresponden a esta ala
        for aula in range(D3_AULAS):
            idx = indice_inscriptos(edificio, piso, ala, aula, bloque)
            total += INSCRIPTOS[idx]
        nombre_ala = "Norte" if ala == 0 else "Sur"
        print(f"  Ala {nombre_ala}: {total} alumnos")

def main():
    print("Generando datos...\n")
    INSCRIPTOS, CAPACIDAD = crear_estructuras()
    print(f"Arreglo INSCRIPTOS: {TOTAL_INSCRIPTOS} elementos")
    print(f"Arreglo CAPACIDAD:  {TOTAL_CAPACIDAD} elementos\n")

    mayor_porcentaje_ocupacion(INSCRIPTOS, CAPACIDAD)
    promedio_por_piso(INSCRIPTOS, bloque=3)
    total_por_ala(INSCRIPTOS, edificio=1, piso=2, bloque=5)

if __name__ == "__main__":
    main()
