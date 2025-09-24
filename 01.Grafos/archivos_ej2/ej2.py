import json

def cargar_grafo_json(ruta_json):
    with open(ruta_json, 'r', encoding='utf-8') as file:
        return json.load(file)

def verificar_reflexividad(E, P):
    for nodo in P:
        if nodo not in E or nodo not in E[nodo]:
            return False
    return True

def verificar_simetria(E, P):
    for i in P:
        for j in P:
            if i != j and i in E and j in E[i]:
                if j not in E or i not in E[j]:
                    return False
    return True

def verificar_antisimetri(E, P):
    for i in P:
        for j in P:
            if i != j and i in E and j in E[i]:
                if j in E and i in E[j]:
                    return False
    return True

def verificar_transitividad(E, P):
    for i in P:
        for j in P:
            if j in E.get(i, []):
                for k in P:
                    if k in E.get(j, []):
                        if k not in E.get(i, []):
                            return False
    return True

def es_orden_o_equivalencia(E, P):
    reflexividad = verificar_reflexividad(E, P)
    simetria = verificar_simetria(E, P)
    antisimetri = verificar_antisimetri(E, P)
    transitividad = verificar_transitividad(E, P)
    
    if reflexividad and simetria and transitividad:
        return "Relación de equivalencia"
    elif reflexividad and antisimetri and transitividad:
        return "Orden parcial"
    else:
        return "No es ni orden ni relación de equivalencia"


if __name__ == "__main__":
    grafo = cargar_grafo_json('01.json')
    P = grafo["P"]
    E = grafo["E"]
    
    print("Reflexividad:", verificar_reflexividad(E, P))
    print("Simetría:", verificar_simetria(E, P))
    print("Antisimetría:", verificar_antisimetri(E, P))
    print("Transitividad:", verificar_transitividad(E, P))
    
    resultado = es_orden_o_equivalencia(E, P)
    print("El grafo es:", resultado)
