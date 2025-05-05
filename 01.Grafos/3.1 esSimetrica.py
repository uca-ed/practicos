#-----------------------------Como par ordenado
def checkIfExists(b,a):
    value=False
    for par in list:
        if ((par[0]==b) and (par[1]==a)):
            value=True
    return value

def esSimetrica (list):
    for par in list:
        a=par[0]
        b=par[1]
        value = checkIfExists(b,a)
        if (value == False):
            print("El par ordenado es simetrico")
            break
    if (value == True):
        print("El par ordenado es simetrico")
    return value

list= ((3,4),(5,6),(1,7),(1,2))
#esSimetrica(list)
list= ((3,4),(4,3),(1,7),(7,1))
#esSimetrica(list)
#----------------------Como matriz
def sacarTransversa(matriz):
    cant=0
    nuevaMatriz = [[0,0,0],[0,0,0],[0,0,0]]
    for fila in matriz:
        nuevaMatriz[0][cant]=fila[0]
        nuevaMatriz[1][cant]=fila[1]
        nuevaMatriz[2][cant]=fila[2]
        cant=cant+1      
    print(matriz)
    print(nuevaMatriz)
    return nuevaMatriz

def checkIfMatrizSimetrica (matriz):
    value = False
    transversa = sacarTransversa(matriz)
    if (transversa == matriz):
        value=True
        print("La matriz es simétrica")
    else:
        print("La matriz NO es Simetrica simétrica")
    return value

matriz = [[1,0,4], [0,5,0], [6,0,-9]]
checkIfMatrizSimetrica (matriz)
matriz = [[3,1,2], [1,6,0], [2,0,4]]
checkIfMatrizSimetrica (matriz)