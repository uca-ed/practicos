import random

EDIFICIOS = 4
PISOS = 5
ALAS = 2
AULAS = 25
BLOQUES = 17

CANTIDAD = EDIFICIOS * PISOS * ALAS * AULAS * BLOQUES

def posicion(edificio, piso, ala, aula, bloque):
    # calculamos el indice lineal aplicando los pesos de cada dimension
    return (edificio * 4250 +
            piso * 850 +
            ala * 425 +
            aula * 17 +
            bloque)

def inicializar_datos():
    # creamos los arreglos vacios
    inscriptos = [0] * CANTIDAD
    capacidad = [0] * CANTIDAD
    
    # cargamos los datos respetando que los inscriptos no superen la capacidad
    for edificio in range(EDIFICIOS):
        for piso in range(PISOS):
            for ala in range(ALAS):
                for aula in range(AULAS):
                    cap = random.randint(20, 60)
                    for bloque in range(BLOQUES):
                        pos = posicion(edificio, piso, ala, aula, bloque)
                        capacidad[pos] = cap
                        inscriptos[pos] = random.randint(0, cap)
                        
    return inscriptos, capacidad

def mostrar_mayor_ocupacion(inscriptos, capacidad):
    # buscamos el pico de ocupacion recorriendo todo el arreglo lineal
    mayor_porcentaje = -1
    mejor_posicion = 0
    
    for pos in range(CANTIDAD):
        porcentaje = inscriptos[pos] / capacidad[pos]
        if porcentaje > mayor_porcentaje:
            mayor_porcentaje = porcentaje
            mejor_posicion = pos
            
    # desarmamos el indice para mostrar las coordenadas exactas
    pos_temp = mejor_posicion
    mejor_bloque = pos_temp % BLOQUES
    pos_temp //= BLOQUES
    
    mejor_aula = pos_temp % AULAS
    pos_temp //= AULAS
    
    mejor_ala = pos_temp % ALAS
    pos_temp //= ALAS
    
    mejor_piso = pos_temp % PISOS
    pos_temp //= PISOS
    
    mejor_edificio = pos_temp
    
    print("a) mayor porcentaje de ocupacion:")
    print(f"edificio: {mejor_edificio}, piso: {mejor_piso}, ala: {mejor_ala}, aula: {mejor_aula}, bloque: {mejor_bloque}")
    print(f"porcentaje: {mayor_porcentaje * 100:.2f} %\n")

def mostrar_promedio_por_piso(inscriptos, bloque):
    # calculamos y mostramos el promedio iterando sobre un bloque estatico
    print(f"b) promedio de alumnos por piso (bloque {bloque}):")
    
    for piso in range(PISOS):
        total = 0
        for edificio in range(EDIFICIOS):
            for ala in range(ALAS):
                for aula in range(AULAS):
                    pos = posicion(edificio, piso, ala, aula, bloque)
                    total += inscriptos[pos]
                    
        promedio = total / EDIFICIOS
        print(f"piso {piso} : {promedio} alumnos")
    print()

def mostrar_alumnos_por_ala(inscriptos, edificio, piso, bloque):
    # filtramos directamente por las coordenadas que llegan por parametro
    print(f"c) alumnos por ala (edificio {edificio}, piso {piso}, bloque {bloque}):")
    
    for ala in range(ALAS):
        total = 0
        for aula in range(AULAS):
            pos = posicion(edificio, piso, ala, aula, bloque)
            total += inscriptos[pos]
            
        print(f"ala {ala} : {total} alumnos")
    print()

if __name__ == "__main__":
    # preparamos los datos base
    arreglo_inscriptos, arreglo_capacidad = inicializar_datos()
    
    # inciso a
    mostrar_mayor_ocupacion(arreglo_inscriptos, arreglo_capacidad)
    
    # test inciso b 
    mostrar_promedio_por_piso(arreglo_inscriptos, bloque=0)
    mostrar_promedio_por_piso(arreglo_inscriptos, bloque=8)
    mostrar_promedio_por_piso(arreglo_inscriptos, bloque=16)
    
    # test inciso c 
    mostrar_alumnos_por_ala(arreglo_inscriptos, edificio=0, piso=0, bloque=0)
    mostrar_alumnos_por_ala(arreglo_inscriptos, edificio=2, piso=3, bloque=10)
    mostrar_alumnos_por_ala(arreglo_inscriptos, edificio=3, piso=4, bloque=16)