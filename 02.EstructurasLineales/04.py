import json

def leerJson(arch):
    f = open(arch)
    data = json.load(f)

    Q = data["Q"]
    alfabetos = data["alfabetos"]

    f.close()
    return [Q,alfabetos]


def radixSort(palabras, alfabetos):
    p = len(palabras[0])
    Q = palabras[:]
    
    for j in range(p-1, -1, -1):

        alfabetoActual = alfabetos[j] # alfabeto para la pos j
        r = len(alfabetoActual)
        pos = {c: i for i, c in enumerate(alfabetoActual)} # crea un diccionario q mapea cada simbolo a su indice
        
        buckets = [[] for _ in range(r)] # crea r buckets
        
        while Q:    
            X = Q.pop(0)                    # X <- Q
            c = X[j]                        # toma el caracter en la posicion
            idx = pos[c]                    # se fija en que nro de bucket
            buckets[idx].append(X)          
        
        Q = []
        for b in buckets:
            Q.extend(b)                     # rearma Q para la proxima
    
    return Q

Q, alfabetos = leerJson("02.EstructurasLineales\ejemplo2RS.json")
print("Entrada:", Q)
print("Alfabetos:", alfabetos)
resultado = radixSort(Q, alfabetos)
print("Salida ordenada:", resultado)