
import random

def calcularStride(dimensiones):
    strides=[1]*len(dimensiones)
    for j in range(len(dimensiones)-2, -1,-1):
        strides[j] = strides[j+1]*dimensiones[j+1]
    return strides

def h(indices, strides):
    idx=0
    for j in range(len(indices)):
        idx += indices[j]*strides[j]
    return idx

def hInversa(idx, dimensiones):
    indices = [0]*len(dimensiones)
    for j in range(len(dimensiones)-1, -1,-1):
        indices[j] = idx%dimensiones[j]
        idx= idx//dimensiones[j]

    return indices




def crearArreglo(dimensiones):
    total=1
    for n in dimensiones:
        total*=n
    return [0]*total

def cargarDatos(dimensiones, strides):
    inscriptos = crearArreglo(dimensiones)
    capacidad = crearArreglo(dimensiones)

    for edificio in range(dimensiones[0]):
        for piso in range(dimensiones[1]):
            for ala in range(dimensiones[2]):
                for aula in range(dimensiones[3]):
                    capAula = random.randint(5,50)
                    for bloque in range(dimensiones[4]):
                        idx = h([edificio, piso, ala, aula, bloque], strides)
                        capacidad[idx] = capAula
                        inscriptos[idx] = random.randint(0,capAula)

    return inscriptos, capacidad
 
def mayorOcupacion(inscriptos, capacidad):
    mejorIdx = None
    mejorPorcentaje = -1

    for idx in range(len(inscriptos)):
        if capacidad[idx]>0:
            porcentaje = inscriptos[idx]/capacidad[idx]
            if porcentaje > mejorPorcentaje:
                mejorPorcentaje = porcentaje
                mejorIdx = idx

    return mejorPorcentaje, mejorIdx


def promedioAlumnosPorPiso(inscriptos, dimensiones, strides, bloque):

    promedios = []
    for piso in range(dimensiones[1]):
        suma = 0 
        cantidad = 0 
        for edificio in range (dimensiones[0]):
            for ala in range(dimensiones[2]):
                for aula in range(dimensiones[3]):
                    idx = h([edificio, piso, ala, aula, bloque], strides)
                    suma += inscriptos[idx]
                    cantidad += 1
        promedios.append(suma/cantidad)

    return promedios

def cantTotalPresentes(inscriptos, dimensiones, strides, edificio, piso, bloque):
    totales = []
    for ala in range(dimensiones[2]):
        suma = 0
        for aula in range(dimensiones[3]):
            idx = h([edificio, piso, ala, aula, bloque], strides )
            suma += inscriptos[idx]
        totales.append(suma)
    return totales




def main():

    dimensiones = [4,5,2,25,85]
    strides = calcularStride(dimensiones)

    inscriptos,capacidad = cargarDatos(dimensiones, strides)

    porcentaje, idx = mayorOcupacion(inscriptos, capacidad)
    print('a) ', hInversa(idx, dimensiones), f"-> {porcentaje*100:.1f}%")
    print("b) ", promedioAlumnosPorPiso(inscriptos, dimensiones, strides, bloque=10))
    print('c) ', cantTotalPresentes(inscriptos, dimensiones, strides, 1,2,5))

main()


