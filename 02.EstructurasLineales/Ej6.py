EDIFICIOS = 4
PISOS = 5
ALAS = 2
AULAS_POR_ALA = 25
BLOQUES = 85

TOTAL_CLASES = EDIFICIOS * PISOS * ALAS * AULAS_POR_ALA * BLOQUES


def indice(edificio, piso, ala, aula, bloque):
   
    posicion = edificio
    posicion = posicion * PISOS + piso
    posicion = posicion * ALAS + ala
    posicion = posicion * AULAS_POR_ALA + aula
    posicion = posicion * BLOQUES + bloque
    return posicion


def crear_estructuras():
    """Crea los arreglos lineales, inicialmente llenos de ceros."""
    inscriptos = [0] * TOTAL_CLASES
    capacidad = [0] * TOTAL_CLASES
    return inscriptos, capacidad


def cargar_datos(inscriptos, capacidad, datos_inscriptos, datos_capacidad):
    #Carga los datos en los arreglos.
    inscriptos[:] = datos_inscriptos
    capacidad[:] = datos_capacidad 


def aula_bloque_mayor_ocupacion(inscriptos, capacidad):
   
    mayor_porcentaje = -1
    resultado = 0

    for edificio in range(EDIFICIOS):
        for piso in range(PISOS):
            for ala in range(ALAS):
                for aula in range(AULAS_POR_ALA):
                    for bloque in range(BLOQUES):
                        posicion = indice(edificio, piso, ala, aula, bloque)
                        cupo = capacidad[posicion] #en realidad no haria falta aclarar el cupo, ya que todos los bloques tienen la misma 
                        #capacidad, pero lo dejo para que se vea el ejemplo de como se haria si no fuera asi

                        if cupo > 0:
                            porcentaje = inscriptos[posicion] / cupo * 100
                        else:
                            porcentaje = 0

                        if porcentaje > mayor_porcentaje:
                            mayor_porcentaje = porcentaje
                            resultado = {
                                "aula": aula,
                                "bloque": bloque,
                               }

    return resultado


def promedio_alumnos_por_piso(inscriptos, bloque):
    promedios = []
    for piso in range(PISOS):
        total_piso = 0
        for edificio in range(EDIFICIOS):
            for ala in range(ALAS):
                for aula in range(AULAS_POR_ALA):
                    total_piso += inscriptos[indice(edificio, piso, ala, aula, bloque)]
        promedios.append(total_piso / 4)

    return promedios


def alumnos_por_ala(inscriptos, edificio, piso, bloque):
    ala_norte = 0
    ala_sur = 0

    for aula in range(AULAS_POR_ALA):
        ala_norte += inscriptos[indice(edificio, piso, 0, aula, bloque)]
        ala_sur += inscriptos[indice(edificio, piso, 1, aula, bloque)]

    return {
        "ala norte": ala_norte,
        "ala sur": ala_sur,
    }


def main():
    inscriptos, capacidad = crear_estructuras()
    datos_inscriptos = [0] * TOTAL_CLASES
    datos_capacidad = [30] * TOTAL_CLASES  #Suponemos que cada aula tiene capacidad para maximo 30 alumnos
    datos_inscriptos[indice(1, 2, 0, 4, 10)] = 30   #En esta aula en ese bloque hay 30 alumnos inscriptos
    datos_inscriptos[indice(1, 2, 1, 4, 10)] = 12
    cargar_datos(inscriptos, capacidad, datos_inscriptos, datos_capacidad)

    print("Mayor ocupación:", aula_bloque_mayor_ocupacion(inscriptos, capacidad))
    print("Promedios del bloque 10:", promedio_alumnos_por_piso(inscriptos, 10))
    print("Alumnos por ala:", alumnos_por_ala(inscriptos, 1, 2, 10))


main()
