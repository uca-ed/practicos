import time
import numpy as np
""" 
orientaciones esquinas:
0 => orientacion correcta
1 => girada en sentido horario
2 => girada en sentido antihorario

orientaciones aristas:
0 => orientacion correcta
1 => orientacion incorrecta
cubo = {
    esquinas_pos: [1,2,3,4,5,6,7,8],
    esquinas_ori: [0,0,0,0,0,0,0,0],
    aristas_pos: [1,2,3,4,5,6,7,8,9,10,11,12],
    aristas_ori: [0,0,0,0,0,0,0,0,0,0,0,0]
}
 """

def U(ep,eo,ap,ao):#blanco
    ep[2], ep[6], ep[7], ep[3] = ep[3], ep[2], ep[6], ep[7] 
    eo[2], eo[6], eo[7], eo[3] = eo[3], eo[2], eo[6], eo[7]

    ap[2], ap[5], ap[10], ap[6] = ap[6], ap[2], ap[5], ap[10]
    ao[2], ao[5], ao[10], ao[6] = ao[6], ao[2], ao[5], ao[10]

def Up(ep,eo,ap,ao):
    ep[2], ep[6], ep[7], ep[3] = ep[6], ep[7], ep[3], ep[2] 
    eo[2], eo[6], eo[7], eo[3] = eo[6], eo[7], eo[3], eo[2]

    ap[2], ap[5], ap[10], ap[6] = ap[5], ap[10], ap[6], ap[2]
    ao[2], ao[5], ao[10], ao[6] = ao[5], ao[10], ao[6], ao[2]

def U2(ep,eo,ap,ao):
    ep[2], ep[6], ep[7], ep[3] = ep[7], ep[3], ep[2], ep[6] 
    eo[2], eo[6], eo[7], eo[3] = eo[7], eo[3], eo[2], eo[6]

    ap[2], ap[5], ap[10], ap[6] = ap[10], ap[6], ap[2], ap[5]
    ao[2], ao[5], ao[10], ao[6] = ao[10], ao[6], ao[2], ao[5]


def D(ep,eo,ap,ao):#amarillo
    ep[1], ep[5], ep[4], ep[0] = ep[5], ep[4], ep[0], ep[1] 
    eo[1], eo[5], eo[4], eo[0] = eo[5], eo[4], eo[0], eo[1]

    ap[0], ap[4], ap[8], ap[7] = ap[4], ap[8], ap[7], ap[0]
    ao[0], ao[4], ao[8], ao[7] = ao[4], ao[8], ao[7], ao[0]

def Dp(ep,eo,ap,ao):
    ep[1], ep[5], ep[4], ep[0] = ep[0], ep[1], ep[5], ep[4] 
    eo[1], eo[5], eo[4], eo[0] = eo[0], eo[1], eo[5], eo[4]

    ap[0], ap[4], ap[8], ap[7] = ap[7], ap[0], ap[4], ap[8]
    ao[0], ao[4], ao[8], ao[7] = ao[7], ao[0], ao[4], ao[8]

def D2(ep,eo,ap,ao):
    ep[1], ep[5], ep[4], ep[0] = ep[4], ep[0], ep[1], ep[5] 
    eo[1], eo[5], eo[4], eo[0] = eo[4], eo[0], eo[1], eo[5]

    ap[0], ap[4], ap[8], ap[7] = ap[8], ap[7], ap[0], ap[4]
    ao[0], ao[4], ao[8], ao[7] = ao[8], ao[7], ao[0], ao[4]

#giro R y L: solo cambian de orientacion las aristas

def R(ep,eo,ap,ao):#azul
    ep[3], ep[7], ep[4], ep[0] = ep[0], ep[3], ep[7], ep[4] 
    eo[3], eo[7], eo[4], eo[0] = eo[0], eo[3], eo[7], eo[4]

    ap[3], ap[6], ap[11], ap[7] = ap[7], ap[3], ap[6], ap[11]
    ao[3], ao[6], ao[11], ao[7] = ao[7]^1, ao[3]^1, ao[6]^1, ao[11]^1

def Rp(ep,eo,ap,ao):
    ep[3], ep[7], ep[4], ep[0] = ep[7], ep[4], ep[0], ep[3]
    eo[3], eo[7], eo[4], eo[0] = eo[7], eo[4], eo[0], eo[3]

    ap[3], ap[6], ap[11], ap[7] = ap[6], ap[11], ap[7], ap[3]
    ao[3], ao[6], ao[11], ao[7] = ao[6]^1, ao[11]^1, ao[7]^1, ao[3]^1

def R2(ep,eo,ap,ao):
    ep[3], ep[7], ep[4], ep[0] = ep[4], ep[0], ep[3], ep[7]
    eo[3], eo[7], eo[4], eo[0] = eo[4], eo[0], eo[3], eo[7]

    ap[3], ap[6], ap[11], ap[7] = ap[11], ap[7], ap[3], ap[6]
    ao[3], ao[6], ao[11], ao[7] = ao[11], ao[7], ao[3], ao[6]


def L(ep,eo,ap,ao):#verde
    ep[2], ep[1], ep[5], ep[6] = ep[6], ep[2], ep[1], ep[5] 
    eo[2], eo[1], eo[5], eo[6] = eo[6], eo[2], eo[1], eo[5]

    ap[1], ap[4], ap[9], ap[5] = ap[5], ap[1], ap[4], ap[9]
    ao[1], ao[4], ao[9], ao[5] = ao[5]^1, ao[1]^1, ao[4]^1, ao[9]^1

def Lp(ep,eo,ap,ao):
    eo[2], eo[1], eo[5], eo[6] = eo[1], eo[5], eo[6], eo[2]
    ep[2], ep[1], ep[5], ep[6] = ep[1], ep[5], ep[6], ep[2] 

    ap[1], ap[4], ap[9], ap[5] = ap[4], ap[9], ap[5], ap[1]
    ao[1], ao[4], ao[9], ao[5] = ao[4]^1, ao[9]^1, ao[5]^1, ao[1]^1

def L2(ep,eo,ap,ao):
    eo[2], eo[1], eo[5], eo[6] = eo[5], eo[6], eo[2], eo[1]
    ep[2], ep[1], ep[5], ep[6] = ep[5], ep[6], ep[2], ep[1] 

    ap[1], ap[4], ap[9], ap[5] = ap[9], ap[5], ap[1], ap[4]
    ao[1], ao[4], ao[9], ao[5] = ao[9], ao[5], ao[1], ao[4]

#giros F y B presentan cambios en la orientacion de aristas y esquinas
#F si una esquina estaba en U, orientacion + 1, si estaba en D, orientacion + 2
def F(ep, eo, ap, ao):#rojo
    #FDR,FDL,FUL,FUR -> FUR,FDR,FDL,FUL
    ep[0], ep[1], ep[2], ep[3] = ep[3], ep[0], ep[1], ep[2]
    eo[0], eo[1], eo[2], eo[3] = (eo[3]+1)%3, (eo[0]+2)%3, (eo[1]+1)%3, (eo[2]+2)%3

    ap[0], ap[1], ap[2], ap[3] = ap[3], ap[0], ap[1], ap[2]
    ao[0], ao[1], ao[2], ao[3] = ao[3]^1, ao[0]^1, ao[1]^1, ao[2]^1

def Fp(ep, eo, ap, ao):
    ep[0], ep[1], ep[2], ep[3] = ep[1], ep[2], ep[3], ep[0]
    eo[0], eo[1], eo[2], eo[3] = (eo[1]+1)%3, (eo[2]+2)%3, (eo[3]+1)%3, (eo[0]+2)%3

    ap[0], ap[1], ap[2], ap[3] = ap[1], ap[2], ap[3], ap[0]
    ao[0], ao[1], ao[2], ao[3] = ao[1]^1, ao[2]^1, ao[3]^1, ao[0]^1

def F2(ep, eo, ap, ao):
    ep[0], ep[1], ep[2], ep[3] = ep[2], ep[3], ep[0], ep[1]
    eo[0], eo[1], eo[2], eo[3] = eo[2], eo[3], eo[0], eo[1]

    ap[0], ap[1], ap[2], ap[3] = ap[2], ap[3], ap[0], ap[1]
    ao[0], ao[1], ao[2], ao[3] = ao[2], ao[3], ao[0], ao[1]

#B hecho con chatgpt, no funcionan las orientaciones si no se usa este metodo
def B(ep, eo, ap, ao):
    # --- Esquinas (BUL=6, BUR=7, BDR=4, BDL=5) ---
    e6, e7, e4, e5 = ep[6], ep[7], ep[4], ep[5]
    ep[6], ep[7], ep[4], ep[5] = e5, e6, e7, e4

    eo6, eo7, eo4, eo5 = eo[6], eo[7], eo[4], eo[5]
    eo[6] = (eo7 + 2) % 3
    eo[7] = (eo4 + 2) % 3
    eo[4] = (eo5 + 1) % 3
    eo[5] = (eo6 + 1) % 3

    # --- Aristas (BU=10, BR=11, BD=8, BL=9) ---
    a10, a11, a8, a9 = ap[10], ap[11], ap[8], ap[9]
    ap[10], ap[11], ap[8], ap[9] = a9, a10, a11, a8

    ao10, ao11, ao8, ao9 = ao[10], ao[11], ao[8], ao[9]
    ao[10], ao[11], ao[8], ao[9] = ao9 ^ 1, ao10 ^ 1, ao11 ^ 1, ao8 ^ 1


def Bp(ep, eo, ap, ao):
    # --- Esquinas ---
    e6, e7, e4, e5 = ep[6], ep[7], ep[4], ep[5]
    ep[6], ep[7], ep[4], ep[5] = e7, e4, e5, e6

    eo6, eo7, eo4, eo5 = eo[6], eo[7], eo[4], eo[5]
    eo[6] = (eo5 + 2) % 3
    eo[5] = (eo4 + 2) % 3
    eo[4] = (eo7 + 1) % 3
    eo[7] = (eo6 + 1) % 3

    # --- Aristas ---
    a10, a11, a8, a9 = ap[10], ap[11], ap[8], ap[9]
    ap[10], ap[11], ap[8], ap[9] = a11, a8, a9, a10

    ao10, ao11, ao8, ao9 = ao[10], ao[11], ao[8], ao[9]
    ao[10], ao[11], ao[8], ao[9] = ao11 ^ 1, ao8 ^ 1, ao9 ^ 1, ao10 ^ 1


def B2(ep, eo, ap, ao):
    # --- Esquinas ---
    e6, e7, e4, e5 = ep[6], ep[7], ep[4], ep[5]
    ep[6], ep[7], ep[4], ep[5] = e4, e5, e6, e7
    eo6, eo7, eo4, eo5 = eo[6], eo[7], eo[4], eo[5]
    eo[6], eo[7], eo[4], eo[5] = eo4, eo5, eo6, eo7  # sin cambio de orientación

    # --- Aristas ---
    a10, a11, a8, a9 = ap[10], ap[11], ap[8], ap[9]
    ap[10], ap[11], ap[8], ap[9] = a8, a9, a10, a11
    ao10, ao11, ao8, ao9 = ao[10], ao[11], ao[8], ao[9]
    ao[10], ao[11], ao[8], ao[9] = ao8, ao9, ao10, ao11



def prueba_tiempos():
    cubo = {
        "esquinas_pos": [1,2,3,4,5,6,7,8],
        "esquinas_ori": [0,0,0,0,0,0,0,0],
        "aristas_pos": [1,2,3,4,5,6,7,8,9,10,11,12],
        "aristas_ori": [0,0,0,0,0,0,0,0,0,0,0,0]
    }
    print("iniciando testeo con orientaciones...")
    inicio = time.time()
    for i in range (1000000):
        U(cubo["esquinas_pos"],cubo["esquinas_ori"],cubo["aristas_pos"],cubo["aristas_ori"])
    fin = time.time()
    print("tiempo usando orientaciones: ",fin-inicio)

def prueba_inversos_F():
    cubo0 = {
        "esquinas_pos": list(range(8)),
        "esquinas_ori": [0]*8,
        "aristas_pos": list(range(12)),
        "aristas_ori": [0]*12
    }
    cubo = {k: v.copy() for k, v in cubo0.items()}
    F(cubo["esquinas_pos"], cubo["esquinas_ori"], cubo["aristas_pos"], cubo["aristas_ori"])
    F2(cubo["esquinas_pos"], cubo["esquinas_ori"], cubo["aristas_pos"], cubo["aristas_ori"])
    F(cubo["esquinas_pos"], cubo["esquinas_ori"], cubo["aristas_pos"], cubo["aristas_ori"])
    Fp(cubo["esquinas_pos"], cubo["esquinas_ori"], cubo["aristas_pos"], cubo["aristas_ori"])
    F2(cubo["esquinas_pos"], cubo["esquinas_ori"], cubo["aristas_pos"], cubo["aristas_ori"])
    Fp(cubo["esquinas_pos"], cubo["esquinas_ori"], cubo["aristas_pos"], cubo["aristas_ori"])
    print(cubo == cubo0)
def prueba_inversos_B():
    cubo0 = {
        "esquinas_pos": list(range(8)),
        "esquinas_ori": [0]*8,
        "aristas_pos": list(range(12)),
        "aristas_ori": [0]*12
    }
    cubo = {k: v.copy() for k, v in cubo0.items()}
    B(cubo["esquinas_pos"], cubo["esquinas_ori"], cubo["aristas_pos"], cubo["aristas_ori"])
    B2(cubo["esquinas_pos"], cubo["esquinas_ori"], cubo["aristas_pos"], cubo["aristas_ori"])
    B(cubo["esquinas_pos"], cubo["esquinas_ori"], cubo["aristas_pos"], cubo["aristas_ori"])
    Bp(cubo["esquinas_pos"], cubo["esquinas_ori"], cubo["aristas_pos"], cubo["aristas_ori"])
    B2(cubo["esquinas_pos"], cubo["esquinas_ori"], cubo["aristas_pos"], cubo["aristas_ori"])
    Bp(cubo["esquinas_pos"], cubo["esquinas_ori"], cubo["aristas_pos"], cubo["aristas_ori"])
    print(cubo == cubo0)

def prueba_inversos_U():
    cubo0 = {
        "esquinas_pos": list(range(8)),
        "esquinas_ori": [0]*8,
        "aristas_pos": list(range(12)),
        "aristas_ori": [0]*12
    }
    cubo = {k: v.copy() for k, v in cubo0.items()}
    U(cubo["esquinas_pos"], cubo["esquinas_ori"], cubo["aristas_pos"], cubo["aristas_ori"])
    U2(cubo["esquinas_pos"], cubo["esquinas_ori"], cubo["aristas_pos"], cubo["aristas_ori"])
    U(cubo["esquinas_pos"], cubo["esquinas_ori"], cubo["aristas_pos"], cubo["aristas_ori"])
    Up(cubo["esquinas_pos"], cubo["esquinas_ori"], cubo["aristas_pos"], cubo["aristas_ori"])
    U2(cubo["esquinas_pos"], cubo["esquinas_ori"], cubo["aristas_pos"], cubo["aristas_ori"])
    Up(cubo["esquinas_pos"], cubo["esquinas_ori"], cubo["aristas_pos"], cubo["aristas_ori"])
    print(cubo == cubo0)
def prueba_inversos_D():
    cubo0 = {
        "esquinas_pos": list(range(8)),
        "esquinas_ori": [0]*8,
        "aristas_pos": list(range(12)),
        "aristas_ori": [0]*12
    }
    cubo = {k: v.copy() for k, v in cubo0.items()}
    D(cubo["esquinas_pos"], cubo["esquinas_ori"], cubo["aristas_pos"], cubo["aristas_ori"])
    D2(cubo["esquinas_pos"], cubo["esquinas_ori"], cubo["aristas_pos"], cubo["aristas_ori"])
    D(cubo["esquinas_pos"], cubo["esquinas_ori"], cubo["aristas_pos"], cubo["aristas_ori"])
    Dp(cubo["esquinas_pos"], cubo["esquinas_ori"], cubo["aristas_pos"], cubo["aristas_ori"])
    D2(cubo["esquinas_pos"], cubo["esquinas_ori"], cubo["aristas_pos"], cubo["aristas_ori"])
    Dp(cubo["esquinas_pos"], cubo["esquinas_ori"], cubo["aristas_pos"], cubo["aristas_ori"])
    print(cubo == cubo0)
def prueba_inversos_R():
    cubo0 = {
        "esquinas_pos": list(range(8)),
        "esquinas_ori": [0]*8,
        "aristas_pos": list(range(12)),
        "aristas_ori": [0]*12
    }
    cubo = {k: v.copy() for k, v in cubo0.items()}
    R(cubo["esquinas_pos"], cubo["esquinas_ori"], cubo["aristas_pos"], cubo["aristas_ori"])
    R2(cubo["esquinas_pos"], cubo["esquinas_ori"], cubo["aristas_pos"], cubo["aristas_ori"])
    R(cubo["esquinas_pos"], cubo["esquinas_ori"], cubo["aristas_pos"], cubo["aristas_ori"])
    Rp(cubo["esquinas_pos"], cubo["esquinas_ori"], cubo["aristas_pos"], cubo["aristas_ori"])
    R2(cubo["esquinas_pos"], cubo["esquinas_ori"], cubo["aristas_pos"], cubo["aristas_ori"])
    Rp(cubo["esquinas_pos"], cubo["esquinas_ori"], cubo["aristas_pos"], cubo["aristas_ori"])
    print(cubo == cubo0)
def prueba_inversos_L():
    cubo0 = {
        "esquinas_pos": list(range(8)),
        "esquinas_ori": [0]*8,
        "aristas_pos": list(range(12)),
        "aristas_ori": [0]*12
    }
    cubo = {k: v.copy() for k, v in cubo0.items()}
    L(cubo["esquinas_pos"], cubo["esquinas_ori"], cubo["aristas_pos"], cubo["aristas_ori"])
    L2(cubo["esquinas_pos"], cubo["esquinas_ori"], cubo["aristas_pos"], cubo["aristas_ori"])
    L(cubo["esquinas_pos"], cubo["esquinas_ori"], cubo["aristas_pos"], cubo["aristas_ori"])
    Lp(cubo["esquinas_pos"], cubo["esquinas_ori"], cubo["aristas_pos"], cubo["aristas_ori"])
    L2(cubo["esquinas_pos"], cubo["esquinas_ori"], cubo["aristas_pos"], cubo["aristas_ori"])
    Lp(cubo["esquinas_pos"], cubo["esquinas_ori"], cubo["aristas_pos"], cubo["aristas_ori"])
    print(cubo == cubo0)

def prueba_sexy(): #sexy move
    cubo0 = {
        "esquinas_pos": list(range(8)),
        "esquinas_ori": [0]*8,
        "aristas_pos": list(range(12)),
        "aristas_ori": [0]*12
    }
    cubo = {k: v.copy() for k, v in cubo0.items()}
    ep,eo,ap,ao = cubo["esquinas_pos"], cubo["esquinas_ori"], cubo["aristas_pos"], cubo["aristas_ori"]
    for i in range(6):
        R(ep,eo,ap,ao)
        U(ep,eo,ap,ao)
        Rp(ep,eo,ap,ao)
        Up(ep,eo,ap,ao)
    print(cubo == cubo0)

def prueba_sexy2(): #sexy move usando F y U
    cubo0 = {
        "esquinas_pos": list(range(8)),
        "esquinas_ori": [0]*8,
        "aristas_pos": list(range(12)),
        "aristas_ori": [0]*12
    }
    cubo = {k: v.copy() for k, v in cubo0.items()}
    ep,eo,ap,ao = cubo["esquinas_pos"], cubo["esquinas_ori"], cubo["aristas_pos"], cubo["aristas_ori"]
    for i in range(6):
        F(ep,eo,ap,ao)
        U(ep,eo,ap,ao)
        Fp(ep,eo,ap,ao)
        Up(ep,eo,ap,ao)
    print(cubo == cubo0)
def prueba_patron_3era_Capa():
    cubo0 = {
        "esquinas_pos": list(range(8)),
        "esquinas_ori": [0]*8,
        "aristas_pos": list(range(12)),
        "aristas_ori": [0]*12
    }
    cubo = {k: v.copy() for k, v in cubo0.items()}
    ep,eo,ap,ao = cubo["esquinas_pos"], cubo["esquinas_ori"], cubo["aristas_pos"], cubo["aristas_ori"]
    for i in range(3):
        R(ep,eo,ap,ao)
        Up(ep,eo,ap,ao)
        Lp(ep,eo,ap,ao)
        U(ep,eo,ap,ao)
        Rp(ep,eo,ap,ao)
        Up(ep,eo,ap,ao)
        L(ep,eo,ap,ao)
        U(ep,eo,ap,ao)
        
    print(cubo == cubo0)

def pruebas():
    print("iniciando pruebas...")
    prueba_tiempos()
    prueba_inversos_F()
    prueba_inversos_B()
    prueba_inversos_U()
    prueba_inversos_D()
    prueba_inversos_R()
    prueba_inversos_L()
    prueba_sexy()
    prueba_sexy2()
    prueba_patron_3era_Capa()

#pruebas()

#0.1304 -> 0.2545 por tener orientaciones y un diseño distinto de cubo