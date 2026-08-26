import json

#Ejercicio 3

def leerArchivo_json(nomarch):
    f = open(nomarch)
    estructura = json.load(f)
    f.close()
    return estructura

def BusquedaDePaso(struct,a,b):
    open=[[a,None]]
    closed=[]
    terminado=False

    while len(open)>0 and terminado==False:
        actual=open.pop(0)
        closed.append(actual)

        pi1_closed=[]
        for par in closed:
            pi1_closed.append(par[0])

        pi0_open=[]
        for par in open:
            pi0_open.append(par[0])

        for i in struct['E'][actual[0]]:
            if i!=actual[0]:
                if not(i in pi0_open):
                    if not(i in pi1_closed):
                        open.append([i,actual[0]])

        if actual[0]==b:
            terminado=True

    if terminado==False:
        return None

    pares={}
    for par in closed:
        pares[par[0]]=par[1]

    camino=[]
    actual=b
    while actual!=None:
        camino.insert(0,actual)
        actual=pares[actual]

    return camino

def main():
    struct=leerArchivo_json("multiplos200Ref.json")
    print("el camino para ir de '2' a '3':",BusquedaDePaso(struct,'2','3'))
main()
