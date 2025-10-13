import json

def abrirJson(archivo):
    f = open(archivo)
    estructura = json.load(f)
    f.close()
    return estructura


def MinUnico(P, E):
    """Devuelve el conjunto minimal del grafo (nodos sin predecesores)."""
    candidatos = set(P)
    for origen, destinos in E.items():
        for d in destinos:
            if d in candidatos:
                candidatos.remove(d)
    #return sorted(list(candidatos))  lista ordenada
    return list(candidatos)


def TSort(P, E):

    # No destructivo
    P = list(P)

    E_copia = {}
    for k, v in E.items():
        E_copia[k] = v.copy() 
    E = E_copia

    OT = []
    Q = MinUnico(P, E)

    while Q != []:
        x = Q.pop(0)
        print(f"x ← {x}")

        OT.append(x)

        if x in P:
            P.remove(x)

        # E = E|P  (eliminamos las aristas salientes de x y las que apuntan a él)
        E.pop(x, None)
        for v in E.values():
            if x in v:
                v.remove(x)

        Q = MinUnico(P, E)

    # Si al terminar P está vacío, éxito
    if P:
        print(" Error: Grafo con ciclos.")
        return None

    print("Orden topológico final:", OT)
    return OT


# Ejemplo de uso
if __name__ == "__main__":
    estructura = abrirJson("02.EstructurasLineales\ej0507-grafosPrueba\lineal.json")
    P = estructura["P"]
    E = estructura["E"]
    TSort(P, E)


