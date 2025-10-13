import random

def deIndiceAPos(dim,ind):
    producto=1
    suma=0
    for i in reversed(range(len(dim))):
        suma+=ind[i]*producto
        producto*=dim[i]
    return suma

def dePosAIndice(dim,pos):
    ind=[0]*len(dim)

    for i in reversed(range(len(dim))):
        ind[i]=pos%dim[i]
        pos=pos//dim[i]

    return ind
        
def mayorOcupacion(C,I,dim):
    N=len(C)

    maxPorcentaje=-1
    maxIndex=-1
    for i in range(N):
        if C[i]!=0:
            porcentaje=I[i]/C[i]
            if porcentaje>maxPorcentaje:
                maxPorcentaje=porcentaje
                maxIndex=i
    return (dePosAIndice(dim,maxIndex),maxPorcentaje*100)


def promedioPorPiso(bloque,dim,INSCRIPTOS):
    promedios = []
    for piso in range(dim[1]):
        total = 0
        aulas = 0
        for edificio in range(dim[0]):
            for ala in range(dim[2]):
                for aula in range(dim[3]):
                    pos = deIndiceAPos(dim,[edificio, piso, ala, aula, bloque])
                    total += INSCRIPTOS[pos]
                    aulas += 1
        promedios.append(total / aulas)
    return promedios

def totalPorAla(edificio, piso, bloque,dim,INSCRIPTOS):
    totales = [0, 0] 
    for ala in range(dim[2]):
        total = 0
        for aula in range(dim[3]):
            pos = deIndiceAPos(dim,[edificio, piso, ala, aula, bloque])
            total += INSCRIPTOS[pos]
        totales[ala] = total
    return totales


def main():

    dim = [4, 5, 2, 25, 85]  # [edificio, piso, ala, aula, bloque]
    N = dim[0] * dim[1] * dim[2] * dim[3] * dim[4]

    CAPACIDAD = []
    INSCRIPTOS = []

    for _ in range(N):
        cap = random.randint(20, 100)
        insc = random.randint(0, cap) 
        CAPACIDAD.append(cap)
        INSCRIPTOS.append(insc)

    a=mayorOcupacion(CAPACIDAD,INSCRIPTOS,dim)
    print('\n\na)')
    print(f'Edificio: {a[0][0]}')
    print(f'Piso: {a[0][1]}')
    print(f'Ala: {a[0][2]}')
    print(f'Aula: {a[0][3]}')
    print(f'Bloque: {a[0][4]}')
    print(f'PORCENTAJE DE OCUPACION: {a[1]}')

    print("\n\nb) Promedio por piso en bloque 10:")
    b= promedioPorPiso(10,dim,INSCRIPTOS)
    for i, p in enumerate(b):
        print(f"   Piso {i}: {p:.2f} alumnos")


    print("\n\nc) Totales por ala (Edificio 1, Piso 3, Bloque 20):")
    c=totalPorAla(1,3,20,dim,INSCRIPTOS)
    print(f'NORTE:{c[0]}')
    print(f'SUR:{c[1]}')


    

    

if __name__=='__main__':
    main()