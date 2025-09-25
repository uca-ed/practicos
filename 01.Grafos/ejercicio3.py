import json

# =========================
# Lectura / Conversión
# =========================

def leerjosn(ruta):
    with open(ruta, encoding="utf-8") as fi:
        estructura = json.load(fi)

    nodos = estructura['P']
    indice = {nodo: idx for idx, nodo in enumerate(nodos)} 
    n = len(nodos)

    adyacencia = {u: set(estructura['E'].get(u, [])) for u in nodos}

    M = [[0]*n for _ in range(n)]
    for u in nodos:
        i = indice[u]
        for v in adyacencia[u]:
            if v in indice:          
                j = indice[v]
                M[i][j] = 1

    return M

def vecinos_izquierda(M, z):

    j = z - 1
    v_izq = []
    for i in range(len(M)):
        if M[i][j] != 0:       
            v_izq.append(i + 1)
    return v_izq

def vecinos_derecha(M, z):
    
    i = z - 1
    v_der = []
    for j in range(len(M[0])):
        if M[i][j] != 0:        
            v_der.append(j + 1)
    return v_der

# =========================
# BFS de paso (camino)
# =========================

def reconstruir_camino(CLOSED, inicio, fin):
    camino = []
    actual = fin
    while actual is not None:
        camino.append(actual)
        pred = None
        for (n, p) in CLOSED:
            if n == actual:
                pred = p
                break
        actual = pred
    return list(reversed(camino))

def buscar_paso(M, a, b):
    OPEN = [(a, None)]   # cola FIFO de (nodo, padre)
    CLOSED = []          # visitados

    while OPEN:
        (z, padre) = OPEN.pop(0)   # desencolo
        CLOSED.append((z, padre))

        # sucesores de z
        sucesores = vecinos_derecha(M, z)

        if b in sucesores:
            CLOSED.append((b, z))
            return reconstruir_camino(CLOSED, a, b)

        # evitar revisitar
        visitados = {n for (n, _) in OPEN} | {n for (n, _) in CLOSED}

        # encolo sucesores no visitados
        for w in sucesores:
            if w not in visitados:
                OPEN.append((w, z))

    # sin camino
    print(f"No hay camino de {a} a {b}.")
    return None



def main():
    M1 = leerjosn('C:/Users/Fede/Documents/GitHub/practicos/01.Grafos/archivos_ej3/esDivisorDe-200.json')
    M2 = leerjosn('C:/Users/Fede/Documents/GitHub/practicos/01.Grafos/archivos_ej3/esDivisorDe-200.json')
    M3 = leerjosn('C:/Users/Fede/Documents/GitHub/practicos/01.Grafos/archivos_ej3/esDivisorDe-200.json')
    M4 = leerjosn('C:/Users/Fede/Documents/GitHub/practicos/01.Grafos/archivos_ej3/multiplos200Ref.json')
    M5 = leerjosn('C:/Users/Fede/Documents/GitHub/practicos/01.Grafos/archivos_ej3/multiplos2000Ref.json')
    M6 = leerjosn('C:/Users/Fede/Documents/GitHub/practicos/01.Grafos/archivos_ej3/multiplos20000Ref.json')

    print(buscar_paso(M1, 3, 20))
    print(buscar_paso(M2, 5, 120))
    print(buscar_paso(M3, 5, 120))
    print(buscar_paso(M4, 5, 120))
    print(buscar_paso(M5, 5, 120))
    print(buscar_paso(M6, 5, 120))
    print("INTEGRANTES GRUPO: JUAN FEDERICO ROSENFELD, IGNACIO GONZALEZ IÑIGO Y NICOLAS LUCINI")

main()
