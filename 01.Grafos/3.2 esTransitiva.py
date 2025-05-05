#--------------Como par ordenado
def checkIfExists(b,a):
    value=False
    for par in list:
        if ((par[0]==b) and (par[1]==a)):
            value=True
    return value

def esTransitiva (list):
    value = True
    for par in list:
        a=par[0]
        b=par[1]
        for otroPar in list:
            b2 = otroPar[1]
            if (otroPar[0]==b):
                value = checkIfExists(a,b2)
                if (value == False):
                    print("No es transivita")
            break
    if (value == True):
        print("Es transivita")
    return value



list= ((3,4),(5,6),(1,7),(1,2))
#esTransitiva(list)
list= ((3,4),(4,3),(1,7),(7,1))
#esTransitiva(list)
list= ((1,1),(2,3),(3,3),(1,3),(2,6))
#esTransitiva(list)
#---------------------Como matriz
 
def multiplicarCuadrado(matriz):
    resultante = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            for k in range(len(matriz)):
                resultante[i][j] += matriz[i][k] * matriz[k][j]
    return resultante
 

def esTransitiva (matriz):
    devolver = True
    i=0
    j=0
    mCuadrada= multiplicarCuadrado(matriz)
    print(mCuadrada)
    filas = len(matriz)
    while (i<filas):
        while (j<filas):
            if (mCuadrada[i][j] > matriz[i][j]):
                devolver= False
            j=j+1
        j=0
        i=i+1
    print(devolver)
    return devolver
    

A = [[1, 1, 1], [1, 1, 1], [1, 0, 1]]
esTransitiva(A)
B = [[1, 1, 1], [0, 0, 0], [0, 0, 0]]
esTransitiva(B)
