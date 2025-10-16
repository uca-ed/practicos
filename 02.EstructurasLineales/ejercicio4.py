import json

def radix2(A, P):
    tipos = A["tipo"]
    niveles = A["nivel"]

 
    cubos = [[] for _ in niveles]
    for par in P:
        k = niveles.index(par[1])
        cubos[k].append(par)
    orden_parcial = []
    for c in cubos:
        orden_parcial.extend(c)


    cubos = [[] for _ in tipos]
    for par in orden_parcial:
        k = tipos.index(par[0])
        cubos[k].append(par)
    orden_final = []
    for c in cubos:
        orden_final.extend(c)

    return orden_final

def leer_json(ruta):
    with open(ruta, "r", encoding="utf-8") as f:
        data = json.load(f)
    A = data["abc"]          # claves nuevas
    P = data["elementos"]    # clave nueva
    return A, P

def main():
    ruta = "diccionario.json"  # ajusta si hace falta
    A, P = leer_json(ruta)
    print("DESORDENADO:", P)
    P_ordenado = radix2(A, P)
    print("ORDENADO   :", P_ordenado)

if __name__ == "__main__":
    main()
