import json

def abrirJson(archivo):
    f = open(archivo)
    estructura = json.load(f)
    f.close()
    return  estructura

def paso(s,t,estructura):
    open = []
    closed = []

    open.append([s,None])
    
    while len(open)!=0:
        x = open.pop(0)
        closed.append(x)

        vecindadDer = estructura['E'][x[0]]

        if (t in vecindadDer):
            closed.append([t,x[0]])
            break

        for w in vecindadDer:
            seAgrega = True
            for i in open:
                if i[0] == w:
                    seAgrega = False
            for i in closed:
                if i[0] == w:
                    seAgrega = False
            if w not in estructura['E']:
                seAgrega = False
            
            if seAgrega ==True:
                open.append([w, x[0]])

    if hayPaso(closed,s,t):
        rta = rearmarPaso(s,t,closed)
    else:
        rta = "No hay paso"

    return rta
     

def rearmarPaso(s,t,closed):
    path = []

    path.append(t)
    actual = t

    while actual != s:
        for nodo, padre in closed:
            if nodo == actual:
                actual = padre
                path.append(actual)
                break

    path.reverse()            
    return path 

def hayPaso(closed, s, t):
    return any(nodo == t for nodo, padre in closed)

estructura1 = abrirJson('archivos_ej3/esDivisorDe-200.json')
print(paso("2","26",estructura1))
print(paso("2","23",estructura1))

