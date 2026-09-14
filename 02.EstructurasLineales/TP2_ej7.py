def TSort(P,E):
    ST=[]
    Q=[]
    for v in minimal(P, E):        
        queue(Q, v)
    while Q != []:
        x=dequeue(Q)
        queue(ST,x)
        P=P-{x}
        E_nueva = []                    
        for (o, d) in E:                   
            if o != x and d != x:          
                E_nueva.add((o, d))        
        E = E_nueva 
        for v in minimal(P, E):        
            queue(Q, v)
    return ST

def dequeue(Q):
    return Q.pop(0)

def queue(Q, elemento):
    if elemento not in Q:
        Q.append(elemento)

def minimal(P, E):
    tienen_entrada = []
    for (o, d) in E:
        if o in P:
            tienen_entrada.add(d)
    minimales = []
    for v in P:
        if v not in tienen_entrada:
            minimales.add(v)
    return minimales

def main():
    P = ["A", "B", "C", "D"]
    E = [("A", "C"), ("B", "D"), ("C", "D")]
    print(TSort(P, E))

main()