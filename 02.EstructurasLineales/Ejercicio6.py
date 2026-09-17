import random

def crearArregloLineal(dimensiones):
    producto=1
    for i in range(len(dimensiones)):
        producto=producto*dimensiones[i]
    arregloLineal=[0]*producto
    return arregloLineal  #devuelve un arreglo lineal inicializado en 0 con las posiciones necesarias segun las dimensiones del arreglo k-dimensional  

def cargarCapacidad(CAPACIDAD):
    for i in range(len(CAPACIDAD)):
        CAPACIDAD[i]=random.randint(1,100)       #le asigna a la capacidad de cada aula un numero entre 1 y 100    
    
def cargarInscriptos(INSCRIPTOS,CAPACIDAD,dimensiones):
    for i in range(len(INSCRIPTOS)):
        max=obtenerCapacidad(CAPACIDAD,dimensiones,i)
        INSCRIPTOS[i]=random.randint(1,max)
        
def obtenerCapacidad(CAPACIDAD,dimensiones,posInscriptos):
    
    indices=obtenerCoordenadas(dimensiones,posInscriptos)
    indiceLineal=obtenerPosicionLineal(indices[:-1],dimensiones[:-1])
    
    return CAPACIDAD[indiceLineal]

def obtenerCoordenadas(dimensiones,posLineal):
    indices=[0]*len(dimensiones)

    for i in range(len(dimensiones)-1,-1,-1):
        indices[i]=posLineal%dimensiones[i]
        posLineal=posLineal//dimensiones[i]
        
    return indices

def obtenerPosicionLineal(coordenadas,dimensiones):
    i=0
    res=0
    while i<len(coordenadas):
        producto=1
        j=i+1
        while j<len(coordenadas):
            producto=producto*dimensiones[j]
            j+=1
        res+=coordenadas[i]*producto
        i+=1
        
    return res

def aulaYHorarioMasOcupado(INSCRIPTOS,CAPACIDAD,dimensiones):
    maxOcupacion=0
    for i in range(len(INSCRIPTOS)):
        porcentaje=INSCRIPTOS[i]/obtenerCapacidad(CAPACIDAD,dimensiones,i)
        if(porcentaje>maxOcupacion):
            maxOcupacion=porcentaje
            indices=obtenerCoordenadas(dimensiones,i)
            
    print(f"El horario y aula con mayor porcentaje de ocupación ({maxOcupacion}) "
      f"son el aula: {indices[3]} en el horario: {indices[4]}\n")
            
def promedioAlumnosPorPiso(INSCRIPTOS, dimensiones, bloque):
    promedios=[0]*dimensiones[1]
    for piso in range(dimensiones[1]):
        suma=0
        cantidad=0
        for edificio in range(dimensiones[0]):
            for ala in range(dimensiones[2]):
                for aula in range(dimensiones[3]):
                    coordenadas=[edificio, piso, ala, aula, bloque]
                    pos=obtenerPosicionLineal(coordenadas, dimensiones)
                    suma+=INSCRIPTOS[pos]
                    cantidad+=1

        promedios[piso]=suma/cantidad

    return promedios

def alumnosPorAla(INSCRIPTOS,dimensiones,edificio,piso,bloque):
    alumnos=[0]*dimensiones[2]
    for ala in range(dimensiones[2]):
        suma=0
        for aula in range(dimensiones[3]):
            coordenadas=[edificio,piso,ala,aula,bloque]
            pos=obtenerPosicionLineal(coordenadas,dimensiones)
            suma+=INSCRIPTOS[pos]
        alumnos[ala]=suma
        
    return alumnos

def main():
    dimensiones=[4,5,2,25,85]
    INSCRIPTOS=crearArregloLineal(dimensiones)
    CAPACIDAD=crearArregloLineal(dimensiones[:-1])      #la capacidad del aula no depende del horario
    cargarCapacidad(CAPACIDAD)
    cargarInscriptos(INSCRIPTOS,CAPACIDAD,dimensiones)
    
    #a: cual es el aula/bloque horario con mayor porcentaje de ocupacion
    aulaYHorarioMasOcupado(INSCRIPTOS,CAPACIDAD,dimensiones)
    
    #b: promedio de alumnos por piso en un bloque horario pasado como parámetro (entre todos los edificios – sólo 5 promedios)
    promedios=promedioAlumnosPorPiso(INSCRIPTOS,dimensiones,10)
    for piso in range(len(promedios)):
        print(f"Piso {piso}: {promedios[piso]}")
        
    #c: dado como parámetro el edificio, el piso y el bloque horario, devolver la cantidad total de alumnos que están presentes en cada ala.
    resultado = alumnosPorAla(INSCRIPTOS, dimensiones, 2, 3, 10)
    print("\nAla 0:", resultado[0])
    print("Ala 1:", resultado[1])

main()
