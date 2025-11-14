import time
import numpy as np
from numba import njit
#Giros basicos del cubo, en sentido horario


# [1,2,3,4,5,6,7,8, 1,2,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10,11,12] cubo
# [0,1,2,3,4,5,6,7, 8,9,10,11,12,13,14,15,16,17,18,19] pos en array
perm_U = np.array([0,1,3,7,4,5,2,6, 8,9,14,11,12,10,18,15,16,17,13,19]) #como cambian los indices despues de permutar

def R(cubo):
    #rotar esquinas
    cubo[3], cubo[7], cubo[4], cubo[0] = cubo[0], cubo[3], cubo[7], cubo[4]

    #rotar aristas
    cubo[4], cubo[7], cubo[12], cubo[8] = cubo[8], cubo[4], cubo[7], cubo[12]
def U_np(cubo):
    # [1,2, 3,4, 5,6, 7,8,  1,2, 3,4, 5, 6,7, 8,9,10, 11, 12] -> 
    # [1,2, 4,8, 5,6, 3,7,  1,2, 7,4, 5, 3,11, 8,9,10, 6, 12]

    cubo[:] = cubo[perm_U]

@njit
def U_numba(cubo,perm):
    tmp = cubo.copy()
    for i in range(len(cubo)):
        cubo[i] = tmp[perm[i]]
@njit
def bucle_numba(cubo,cant,perm):
    for i in range(cant):
        U_numba(cubo,perm)

def prueba_tiempos():
    cubo=np.array([1,2,3,4,5,6,7,8, 1,2,3,4,5,6,7,8,9,10,11,12])
    print("iniciando testeo con permutaciones (numpy)...")
    inicio = time.time()
    for i in range (10000000):
        U_np(cubo)
    fin = time.time()
    print("tiempo usando permutaciones (numpy): ",fin-inicio)
    
    cubo=[1,2,3,4,5,6,7,8, 1,2,3,4,5,6,7,8,9,10,11,12] #sin numpy
    print("iniciando testeo sin permutaciones...")
    inicio = time.time()
    for i in range (10000000):
        R(cubo)
    fin = time.time()
    print("tiempo sin usar permutaciones: ",fin-inicio)

    cubo=np.array([1,2,3,4,5,6,7,8, 1,2,3,4,5,6,7,8,9,10,11,12])
    print("iniciando testeo con con permutaciones (numba)...")
    U_numba(cubo,perm_U)
    perm = perm_U
    inicio = time.time()
    bucle_numba(cubo,10000000,perm)
    fin = time.time()
    print("tiempo sin usar permutaciones (numba): ",fin-inicio)
    """    
    iniciando testeo con permutaciones (numpy)...
    tiempo usando permutaciones (numpy):  3.0189802646636963
    iniciando testeo sin permutaciones...
    tiempo sin usar permutaciones:  1.2245185375213623
    iniciando testeo con con permutaciones (numba)...
    tiempo sin usar permutaciones (numba):  0.7864949703216553 
    """

prueba_tiempos()
""" 
def L(cubo):
    cubo[], cubo[], cubo[], cubo[] = cubo[], cubo[], cubo[], cubo[]
    cubo[], cubo[], cubo[], cubo[] = cubo[], cubo[], cubo[], cubo[]
def F(cubo):
def D(cubo):
def B(cubo):

#Giros 'prima', en sentido antihorario
def Up(cubo):
def Rp(cubo):
def Lp(cubo):
def Fp(cubo):
def Dp(cubo):
def Bp(cubo):

#Giros dobles, de 180 grados
def UU(cubo):
def RR(cubo):
def LL(cubo):
def FF(cubo):
def DD(cubo):
def BB(cubo): 
"""