import json
f=open('02.json')
estructura = json.load(f)
prox=estructura['E']

i=str(input("ingrese nodo inicial: "))
fin=str(input("ingrese nodo final: "))
open=[(i,None)]
closed=[]
camino_encontrado=False
while open!=[]:
    nodoAct=open[0][0]#string del nodo en el que estoy
    vecinos=prox.get(nodoAct,[])#lista de los nodos a los que puedo llegar desde donde estoy
    for j in vecinos:
        conto=0
        contc=0
        for k in open:
            if j==k[0]:
                conto=1
        for k in closed:
            if j==k[0]:
                contc=1
        if conto==0 and contc==0:
            open.append((j,nodoAct))
    closed.append(open[0])
    if nodoAct==fin:
            camino_encontrado=True
            break
    
    open.pop(0)
if camino_encontrado:
    camino=[]
    while fin!=i:
        for x in closed:
            if x[0]==fin:
                camino.insert(0,x[0])
                fin=x[1]
                break
    print(i,end='')
    for n in camino:
        print(' ->',n,end='')

else:
    print("no existe camino entre los dos nodos")
print()
f.close()
