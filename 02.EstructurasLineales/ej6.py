dimensiones = [4, 5, 2, 25, 85]



def indice_lineal(edificio, piso, ala, aula, bloque):
    return ((((edificio * dimensiones[1] + piso) * dimensiones[2]
              + ala) * dimensiones[3] + aula) * dimensiones[4] + bloque)



total = 1
for dimension in dimensiones:
    total = total * dimension

inscriptos = [0] * total
capacidad = [0] * total

for posicion in range(total):
    numero_aula = posicion // dimensiones[4]
    capacidad[posicion] = 30 + numero_aula % 21
    inscriptos[posicion] = posicion % (capacidad[posicion] + 1)


# a
def mayor_ocupacion():
    mejor_posicion = 0
    mayor_porcentaje = -1

    for posicion in range(total):
        porcentaje = inscriptos[posicion] * 100 / capacidad[posicion]
        if porcentaje > mayor_porcentaje:
            mayor_porcentaje = porcentaje
            mejor_posicion = posicion

    return mejor_posicion, mayor_porcentaje


# b
def promedios_por_piso(bloque):
    promedios = []
    aulas_por_piso = dimensiones[0] * dimensiones[2] * dimensiones[3]

    for piso in range(dimensiones[1]):
        suma = 0
        for edificio in range(dimensiones[0]):
            inicio = indice_lineal(edificio, piso, 0, 0, bloque)
            fin = inicio + dimensiones[2] * dimensiones[3] * dimensiones[4]
            for posicion in range(inicio, fin, dimensiones[4]):
                suma = suma + inscriptos[posicion]
        promedios.append(suma / aulas_por_piso)

    return promedios


# c
def alumnos_por_ala(edificio, piso, bloque):
    totales = []

    for ala in range(dimensiones[2]):
        suma = 0
        inicio = indice_lineal(edificio, piso, ala, 0, bloque)
        fin = inicio + dimensiones[3] * dimensiones[4]
        for posicion in range(inicio, fin, dimensiones[4]):
            suma = suma + inscriptos[posicion]
        totales.append(suma)

    return totales


posicion, porcentaje = mayor_ocupacion()


bloque = posicion % dimensiones[4]
resto = posicion // dimensiones[4]
aula = resto % dimensiones[3]
resto = resto // dimensiones[3]
ala = resto % dimensiones[2]
resto = resto // dimensiones[2]
piso = resto % dimensiones[1]
edificio = resto // dimensiones[1]

print("a) Mayor ocupacion:")
print("Edificio:", edificio, "Piso:", piso, "Ala:", ala,
      "Aula:", aula, "Bloque:", bloque)
print("Porcentaje:", porcentaje, "%")
print("b) Promedios por piso para el bloque 0:", promedios_por_piso(0))
print("c) Alumnos por ala, edificio 0, piso 0, bloque 0:",
      alumnos_por_ala(0, 0, 0))
