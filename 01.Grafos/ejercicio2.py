
import json

# =========================
# Lectura / Conversión
# =========================

# ESTO LO HIZO CHATGPT PARA ARMAR BIEN LA MATRIZ A PARTIR DEL JSON
def leer_json(ruta_json):
    with open(ruta_json, encoding="utf-8") as f:
        est = json.load(f)
    P = list(est.get("P", []))
    E = dict(est.get("E", {}))
    for v in P:
        if v not in E:
            E[v] = []
    return P, E

def matriz_desde_vecindad(P, E):
    # Orden numérico si los nodos son "1","2",...; si no son dígitos, usa orden lexicográfico
    try:
        P_orden = sorted(P, key=lambda x: int(x))
    except:
        P_orden = sorted(P)
    pos = {v: i for i, v in enumerate(P_orden)}
    n = len(P_orden)
    A = [[0]*n for _ in range(n)]
    for u, outs in E.items():
        if u in pos:
            i = pos[u]
            for w in outs:
                if w in pos:
                    j = pos[w]
                    A[i][j] = 1
    return P_orden, A

#hasta aca hizo chatgpt junto al main para armar la matriz


# la matriz es reflexiva si cada elemento se relaciona consigo mismo, es decir veo la diagonal
def es_reflexiva(A):
    n = len(A)
    for i in range(n):
        if A[i][i] != 1: # veo la diagonal
            return False
    return True

# si un elemento se relaciona con otro, el otro se relaciona con el original.
def es_simetrica(A):
    n = len(A)
    for i in range(n):
        for j in range(n):
            if A[i][j] != A[j][i]:
                return False
    return True

# lo mismo q simetrica pero veo si son el mismo elemento / numero
def es_antisimetrica(A):
    n = len(A)
    for i in range(n):
        for j in range(n):
            if i != j and A[i][j] == 1 and A[j][i] == 1:
                return False
    return True


def es_transitiva(A):
    n = len(A)
    # Si existe i->k y k->j debe existir i->j
    for i in range(n):
        for k in range(n):
            if A[i][k] == 1:
                for j in range(n):
                    if A[k][j] == 1 and A[i][j] == 0:
                        return False
    return True



def clasificar_relacion(A):
    r = es_reflexiva(A)
    s = es_simetrica(A)
    a = es_antisimetrica(A)
    t = es_transitiva(A)

    es_orden_parcial = r and a and t
    es_equivalencia = r and s and t

    return {
        "reflexiva": r,
        "simetrica": s,
        "antisimetrica": a,
        "transitiva": t,
        "orden_parcial": es_orden_parcial,
        "equivalencia": es_equivalencia
    }

# =========================
# Ejemplos de uso
# =========================
if __name__ == "__main__":
    # ---- Caso JSON (nota) ----
    print("GRAFO 01.JSON")
    ruta_json = r"C:\Users\Fede\Documents\GitHub\practicos\01.Grafos\archivos_ej2\01.json"
    try:
        Pj, Ej = leer_json(ruta_json)
        Pj_ord, Aj = matriz_desde_vecindad(Pj, Ej)
        print("== JSON ==")
        resJ = clasificar_relacion(Aj)
        for k, v in resJ.items():
            print(f"{k}: {v}")
        print()
    except FileNotFoundError:
        print("No se encontró el JSON (ajustá la ruta).")
    print("GRAFO 02.JSON")
    ruta_json = r"C:\Users\Fede\Documents\GitHub\practicos\01.Grafos\archivos_ej2\02.json"
    try:
        Pj, Ej = leer_json(ruta_json)
        Pj_ord, Aj = matriz_desde_vecindad(Pj, Ej)
        print("== JSON ==")
        resJ = clasificar_relacion(Aj)
        for k, v in resJ.items():
            print(f"{k}: {v}")
        print()
    except FileNotFoundError:
        print("No se encontró el JSON (ajustá la ruta).")
    print("GRAFO 03.JSON")
    ruta_json = r"C:\Users\Fede\Documents\GitHub\practicos\01.Grafos\archivos_ej2\03.json"
    try:
        Pj, Ej = leer_json(ruta_json)
        Pj_ord, Aj = matriz_desde_vecindad(Pj, Ej)
        print("== JSON ==")
        resJ = clasificar_relacion(Aj)
        for k, v in resJ.items():
            print(f"{k}: {v}")
        print()
    except FileNotFoundError:
        print("No se encontró el JSON (ajustá la ruta).")
