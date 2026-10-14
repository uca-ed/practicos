def leer_grafo(nombre_arch):
    P = []
    E = []

    with open(nombre_arch,"r") as arch:
        for linea in arch:
            linea = linea.strip()
            if not linea:
                continue

            partes = linea.replace(","," ").split()
            origen = partes[0]
            destino = partes[1]

            if origen not in P:
                P.append(origen)
            if destino not in P:
                P.append(destino)

            E.append([origen,destino])

    return P,E

def Min(P,E):
    minimales = []
    for nodo in P:
        tiene_entrante = False
        for arista in E:
            if arista[1] == nodo:
                tiene_entrante = True
                break
        if not tiene_entrante:
            minimales.append(nodo)
    return minimales

def T_Sort(nombre_arch):
    P, E = leer_grafo(nombre_arch)
    total = len(P)

    Q = []
    Sort_T = []

    for m in Min(P,E):
        Q.append(m)

    while len(Q) > 0:
        x = Q.pop(0)

        Sort_T.append(x)

        P.remove(x)

        nuevas_aristas = []

        for arista in E:
            if arista[0] != x:
                nuevas_aristas.append(arista)
        E = nuevas_aristas

        for m in Min(P,E):
            if m not in Q:
                Q.append(m)

    if len(Sort_T) != total:
        print("Es una estructura ciclica, no se termino de vaciar el grafo")
        return None

    return Sort_T

def main():
    resultado = T_Sort("grafoEJ5.txt")
    if resultado is not None:
        print("Resultado 1 luego del algoritmo T-sort: ",resultado)

    resultadoCiclico = T_Sort("grafoCiclicoEJ5.txt")
    if resultadoCiclico is not None:
        print("Resultado 2 luego del algoritmo T-sort: ",resultadoCiclico)
main()