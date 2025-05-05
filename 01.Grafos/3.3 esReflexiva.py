#------------------------------Como matriz: La diagonal principal de la matriz contendrá solo 1's
def esReflexiva(matriz):
    devolver = True
    i=0
    for linea in matriz:
        if (linea[i] != 1):
            devolver = False
        i=i+1
    return devolver
        
A= [ [1,0,2],[3,1,4],[0,6,1]]
print( esReflexiva(A))
A= [ [4,0,2],[3,1,4],[0,6,1]]
print( esReflexiva(A))