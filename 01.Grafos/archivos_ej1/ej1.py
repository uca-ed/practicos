import json
import csv

with open("01.json", "r", encoding="utf-8") as archivo:
    grafo = json.load(archivo)


P = grafo["P"]   
E = grafo["E"]



reflexiva=True
i=0
while i<len(P):
    
    nodo =P[i]  
    if nodo not in E.get(str(nodo), []):
        reflexiva=False
        print(nodo)
        print (reflexiva)
        break 
    i+=1   
print(f"reflexividad={reflexiva}")
   

simetria=True
i=0
while i<len(P):
    nodo=P[i]
    for b in E.get(nodo,[]):
        if nodo not in E.get(b,[]):
           
            simetria=False
            
            break
    if not simetria:
        break
    i+=1
print (f"simetria={simetria}")

i=0
antisimetria=True
while i<len(P):
    nodo=P[i]
    for c in E.get(nodo,[]):
        
        if  nodo !=c and nodo in E.get(str(c),[]): 
            
            antisimetria=False  
            break
    if not antisimetria:
        break
    i+=1
print (f"antisimetria={antisimetria}")




transitiva = True
i=0

while i < len(P):
    a = str(P[i])
    vecinos_de_a = E.get(a, [])
    
    for b in vecinos_de_a:
        b = str(b)
        vecinos_de_b = E.get(b, [])
        
        for c in vecinos_de_b:
            c = str(c)

            if c not in vecinos_de_a:
                transitiva = False
                print(f"Falta la conexión directa entre '{a}' y '{c}' (pasando por '{b}')")
                break
                
        if not transitiva:
            break
            
    if not transitiva:
        break
        
    i += 1

print(f"transitiva = {transitiva}")


es_equivalencia = reflexiva and simetria and transitiva
es_orden = reflexiva and antisimetria and transitiva

if es_equivalencia:
    print("El grafo corresponde a una RELACIÓN DE EQUIVALENCIA.")
elif es_orden:
    print("El grafo corresponde a una RELACIÓN DE ORDEN.")
else:
    print("El grafo NO es ni de orden ni de equivalencia.")