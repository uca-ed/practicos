import time
import random

def dimensiones():
    return 4, 5, 2, 25, 85

def tam_total():
    e, p, a, u, b = dimensiones()
    return e * p * a * u * b

def indice_lineal(ed, piso, ala, aula, bloque):
    e, p, a, u, b = dimensiones()
    return ((((ed * p) + piso) * a + ala) * u + aula) * b + bloque

def crear_lineal():
    n = tam_total()
    inscriptos = [0] * n
    capacidad = [0] * n
    return inscriptos, capacidad

def crear_anidado():
    edificios, pisos, alas, aulas, bloques = dimensiones()

    inscriptos = []
    capacidad = []

    for e in range(edificios):
        lista_pisos_i = []
        lista_pisos_c = []

        for p in range(pisos):
            lista_alas_i = []
            lista_alas_c = []

            for a in range(alas):
                lista_aulas_i = []
                lista_aulas_c =[]

                for u in range(aulas):
                    lista_bloques_i = []
                    lista_bloques_c = []

                    for b in range(bloques):
                        lista_bloques_i.append(0)
                        lista_bloques_c.append(0)

                    lista_aulas_i.append(lista_bloques_i)
                    lista_aulas_c.append(lista_bloques_c)

                lista_alas_i.append(lista_aulas_i)
                lista_alas_c.append(lista_aulas_c)

            lista_pisos_i.append(lista_alas_i)
            lista_pisos_c.append(lista_alas_c)

        inscriptos.append(lista_pisos_i)
        capacidad.append(lista_pisos_c)

    return inscriptos, capacidad


def cargar_aleatorio_lineal(inscriptos, capacidad, semilla=1):
    random.seed(semilla)
    e, p, a, u, b = dimensiones()
    for ed in range(e):
        for piso in range(p):
            for ala in range(a):
                for aula in range(u):
                    for bloque in range(b):
                        idx = indice_lineal(ed, piso, ala, aula, bloque)
                        cap = random.randint(20, 120)
                        val = random.randint(0, cap)
                        capacidad[idx] = cap
                        inscriptos[idx] = val

def cargar_aleatorio_anidado(inscriptos, capacidad, semilla=1):
    random.seed(semilla)
    e, p, a, u, b = dimensiones()
    for ed in range(e):
        for piso in range(p):
            for ala in range(a):
                for aula in range(u):
                    for bloque in range(b):
                        cap = random.randint(20, 120)
                        val = random.randint(0, cap)
                        capacidad[ed][piso][ala][aula][bloque] = cap
                        inscriptos[ed][piso][ala][aula][bloque] = val

def mejor_ocupacion_lineal(inscriptos, capacidad):
    e, p, a, u, b = dimensiones()
    mejor = -1.0
    mejor_pos = (0, 0, 0, 0, 0)
    for ed in range(e):
        for piso in range(p):
            for ala in range(a):
                for aula in range(u):
                    for bloque in range(b):
                        idx = indice_lineal(ed, piso, ala, aula, bloque)
                        cap = capacidad[idx]
                        if cap > 0:
                            porc = inscriptos[idx] / cap
                            if porc > mejor:
                                mejor = porc
                                mejor_pos = (ed, piso, ala, aula, bloque)
    return mejor_pos, mejor

def mejor_ocupacion_anidado(inscriptos, capacidad):
    e, p, a, u, b = dimensiones()
    mejor = -1.0
    mejor_pos = (0, 0, 0, 0, 0)
    for ed in range(e):
        for piso in range(p):
            for ala in range(a):
                for aula in range(u):
                    for bloque in range(b):
                        cap = capacidad[ed][piso][ala][aula][bloque]
                        if cap > 0:
                            porc = inscriptos[ed][piso][ala][aula][bloque] / cap
                            if porc > mejor:
                                mejor = porc
                                mejor_pos = (ed, piso, ala, aula, bloque)
    return mejor_pos, mejor

def promedio_por_piso_lineal(inscriptos, bloque):
    e, p, a, u, b = dimensiones()
    promedios = []
    divisor = e * a * u
    for piso in range(p):
        suma = 0
        for ed in range(e):
            for ala in range(a):
                for aula in range(u):
                    idx = indice_lineal(ed, piso, ala, aula, bloque)
                    suma += inscriptos[idx]
        promedios.append(suma / divisor)
    return promedios

def promedio_por_piso_anidado(inscriptos, bloque):
    e, p, a, u, b = dimensiones()
    promedios = []
    divisor = e * a * u
    for piso in range(p):
        suma = 0
        for ed in range(e):
            for ala in range(a):
                for aula in range(u):
                    suma += inscriptos[ed][piso][ala][aula][bloque]
        promedios.append(suma / divisor)
    return promedios

def total_por_ala_lineal(inscriptos, edificio, piso, bloque):
    e, p, a, u, b = dimensiones()
    norte = 0
    sur = 0
    for aula in range(u):
        norte += inscriptos[indice_lineal(edificio, piso, 0, aula, bloque)]
        sur += inscriptos[indice_lineal(edificio, piso, 1, aula, bloque)]
    return norte, sur

def total_por_ala_anidado(inscriptos, edificio, piso, bloque):
    e, p, a, u, b = dimensiones()
    norte = 0
    sur = 0
    for aula in range(u):
        norte += inscriptos[edificio][piso][0][aula][bloque]
        sur += inscriptos[edificio][piso][1][aula][bloque]
    return norte, sur

def medir_tiempo(funcion, *args):
    t0 = time.perf_counter()
    r = funcion(*args)
    t1 = time.perf_counter()
    return r, t1 - t0

def main():
    ins_l, cap_l = crear_lineal()
    ins_a, cap_a = crear_anidado()

    cargar_aleatorio_lineal(ins_l, cap_l, 7)
    cargar_aleatorio_anidado(ins_a, cap_a, 7)

    (pos_l, porc_l), t1 = medir_tiempo(mejor_ocupacion_lineal, ins_l, cap_l)
    (pos_a, porc_a), t2 = medir_tiempo(mejor_ocupacion_anidado, ins_a, cap_a)

    bloque = 10
    prom_l, t3 = medir_tiempo(promedio_por_piso_lineal, ins_l, bloque)
    prom_a, t4 = medir_tiempo(promedio_por_piso_anidado, ins_a, bloque)

    edificio = 2
    piso = 3
    (n_l, s_l), t5 = medir_tiempo(total_por_ala_lineal, ins_l, edificio, piso, bloque)
    (n_a, s_a), t6 = medir_tiempo(total_por_ala_anidado, ins_a, edificio, piso, bloque)

    print("a_lineal_posicion:", pos_l, "a_lineal_porcentaje:", round(porc_l * 100, 2))
    print("a_anidado_posicion:", pos_a, "a_anidado_porcentaje:", round(porc_a * 100, 2))

    print("b_lineal_promedios_por_piso:", [round(x, 2) for x in prom_l])
    print("b_anidado_promedios_por_piso:", [round(x, 2) for x in prom_a])

    print("c_lineal_totales_por_ala:", (n_l, s_l))
    print("c_anidado_totales_por_ala:", (n_a, s_a))

    print("tiempo_mejor_ocupacion_lineal_segundos:", round(t1, 6))
    print("tiempo_mejor_ocupacion_anidado_segundos:", round(t2, 6))
    print("tiempo_promedio_por_piso_lineal_segundos:", round(t3, 6))
    print("tiempo_promedio_por_piso_anidado_segundos:", round(t4, 6))
    print("tiempo_total_por_ala_lineal_segundos:", round(t5, 6))
    print("tiempo_total_por_ala_anidado_segundos:", round(t6, 6))

main()
