import json


# busqueda de MINIMAL, nodos que no tienen arcos entrantes [FUENTES]

def minimales(P):
    minimales=[]
    cond=True
    for i in range(0,len(P[0])):
        for j in range(0,len(P[0])):
            if P[j][i]!=0: # si tiene un arco entrante
                cond=False
        if cond:
            minimales.append(i+1)
        cond=True
        
    return minimales

def l(P,z):
    z-=1
    vIzq=[]
    for j in range(0,len(P[0])):
        if P[j][z]!=0: # si tiene un arco entrante
            vIzq.append(j+1)
        
    return vIzq

def r(P,z):
    z-=1
    vDer=[]
    for j in range(0,len(P[0])):
        if P[z][j]!=0: # si tiene un arco saliente
            vDer.append(j+1)
        
    return vDer


# busqueda de MAXIMAL, nodos que no tienen arcos salientes [SUMIDEROS]
def maximales(P):
    maximales=[]
    cond=True
    for i in range(0,len(P[0])):
        for j in range(0,len(P[0])):
            if P[i][j]!=0: # si tiene un arco saliente... 
                cond=False
        if cond:
            maximales.append(i+1)
        cond=True
    return maximales

def leerCSV(ruta):
    f=open(ruta,'r')
    M=[]
    while True:
        line=f.readline()
        if not line:
            break
        strline=line.strip().split(',')
        for i in range(0,len(strline)):
            strline[i]=int(strline[i])
        M.append(strline)

    return M

# def esReflexiva(P):
#     res=True
#     for i in range(0,len(P[0])):
#         if P[i][i]!=1:
#             res=False
#     return res

# def esSimetrica(P):
#     res=True
#     for i in range(0,len(P[0])):
#         for j in range(0,len(P[0])):
#             if P[i][j]!=P[j][i]:
#                 res=False
#     return res

# def esAntiSimetrica(P):
#     res=True
#     for i in range(0,len(P[0])):
#         for j in range(0,len(P[0])):
#             if  P[i][j]==1 and P[i][j]==P[j][i]:
#                 res=False
#     return res

# def esAntiSimetricaDebil(P):
#     res=True
#     for i in range(0,len(P[0])):
#         for j in range(0,len(P[0])):
#             if j!=i and P[i][j]==1 and P[i][j]==P[j][i]:
#                 res=False
#     return res



# def productoLogicoMatricial(P):  
    
#     C = [[0]*len(P[0]) for _ in range(len(P[0]))]
    
#     for i in range(len(P[0])):
#         for j in range(len(P[0])):
#             for k in range(len(P[0])):
#                 if P[i][k] and P[k][j]:
#                     C[i][j] = 1
#                     break  
#     return C

# def esTransitiva(P):
#     n = len(P)
#     for k in range(n): # k nodo intermedio
#         for i in range(n): 
#             if P[i][k]: # si existe la relacion (i,k)
#                 for j in range(n):
#                     if P[k][j] and not P[i][j]: #si existe (k,j) y no (i,j) entonces NO ES TRANSITIVA
#                         return False
#     return True

        

# # def esTransitiva(P):
# #     P2=productoLogicoMatricial(P)
# #     for i in range(0,len(P[0])):
# #         for j in range(0,len(P[0])):
# #             if P2[i][j]==1 and P[i][j]!=1:
# #                 return False
# #     return True

# def esRDeOrden(P):
#     return esTransitiva(P) and esReflexiva(P) and esAntiSimetricaDebil(P)

# def esRDeEquivalencia(P):
#     return esTransitiva(P) and esReflexiva(P) and esSimetrica(P)


def analisisCompletoDeMatrizDeAdyacencia(P):
    print(f"MAXIMALES: {maximales(P)}")
    print(f"MINIMALES: {minimales(P)}")
    print(f"L(4): {l(P,4)}")
    print(f"R(4): {r(P,4)}")

               
    
# dan las dos listas vacias porque todos tienen relacion consigo mismos

def main():
    
    f = open('/home/ignacio-berkelaar/Documents/GitHub/practicos/01.Grafos/archivos_ej1/01.json')
    estructura = json.load(f)

    f.close()

    M1=[]
    f=0
    for i in estructura['P']:
        M1.append([])
        for j in estructura['P']:
            if j in estructura['E'][i]:
                M1[f].append(1)
            else:
                M1[f].append(0)
        f+=1



    M2=leerCSV('/home/ignacio-berkelaar/Documents/GitHub/practicos/01.Grafos/archivos_ej1/01.csv')
    M3=leerCSV('/home/ignacio-berkelaar/Documents/GitHub/practicos/01.Grafos/archivos_ej1/02.csv')
    M4=leerCSV('/home/ignacio-berkelaar/Documents/GitHub/practicos/01.Grafos/archivos_ej1/03.csv')
    M5=leerCSV('/home/ignacio-berkelaar/Documents/GitHub/practicos/01.Grafos/archivos_ej1/04.csv')

    print("\nAnalisis M1:")
    analisisCompletoDeMatrizDeAdyacencia(M1)
    print("\nAnalisis M2:")
    analisisCompletoDeMatrizDeAdyacencia(M2)
    print("\nAnalisis M3:")
    analisisCompletoDeMatrizDeAdyacencia(M3)
    print("\nAnalisis M4:")
    analisisCompletoDeMatrizDeAdyacencia(M4)
    print("\nAnalisis M5:")
    analisisCompletoDeMatrizDeAdyacencia(M5)



main()