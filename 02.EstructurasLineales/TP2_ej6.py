from Datos_ej6 import CAPACIDAD, INSCRIPTOS
#PUNTO A
def AulaMayorPorcentajeDeOcupacion(Inscriptos, Capacidad):
    n = len(Capacidad)
    mejor_porcentaje = -1
    mejor_indice = 0
    for i in range(n):
        porcentaje = Inscriptos[i] / Capacidad[i]
        if porcentaje > mejor_porcentaje:
            mejor_porcentaje = porcentaje
            mejor_indice = i
    indices = obtenerIndices(mejor_indice)
    return {"aula": indices[3], "bloque": indices[4]}

def obtenerIndices(l):
    indice0 = l // 21250
    l = l % 21250
    indice1 = l // 4250
    l = l % 4250
    indice2 = l // 2125
    l = l % 2125
    indice3 = l // 85
    l = l % 85
    indice4 = l
    return [indice0, indice1, indice2, indice3, indice4]

#PUNTO B
# bloqueHorario: entero entre 0 y 84 que identifica el bloque horario dentro
# de la dimensión d4 del arreglo (85 bloques = 17 bloques horarios por día x 5 días).
# Si se cuenta con el día y el bloque del día por separado, se debe convertir
# antes de llamar a la función: bloqueHorario = dia * 17 + bloqueDelDia
def promedioPorPisoEnBloque(bloqueHorario, Inscriptos):
    promedios=[]
    for piso in range(5):
        suma=0
        cantidad=0
        for edificio in range(4):
            for ala in range(2):
                for aula in range(25):
                    indice= edificio*5*2*25*85 +piso*2*25*85+ala*25*85 +aula*85 + bloqueHorario
                    suma+=Inscriptos[indice]
                    cantidad+=1
        promedios.append(suma/cantidad)
    return promedios

#PUNTO C
def AlumnosXAla(edificio, piso, bloque, Inscriptos):
    alumnosPorAla=[]
    for ala in range(2):
        cantidad=0
        for aula in range(25):
            indice= edificio*5*2*25*85 +piso*2*25*85+ala*25*85 +aula*85 + bloque
            cantidad+=Inscriptos[indice]
        alumnosPorAla.append(cantidad)
    res={"ala norte": alumnosPorAla[0], "ala sur": alumnosPorAla[1]}
    return res

def main():
    print("PUNTO A:", AulaMayorPorcentajeDeOcupacion(INSCRIPTOS, CAPACIDAD))
    print("PUNTO B (bloque 10):", promedioPorPisoEnBloque(10, INSCRIPTOS))
    print("PUNTO C (edificio 1, piso 2, bloque 30):", AlumnosXAla(1, 2, 30, INSCRIPTOS))

main()