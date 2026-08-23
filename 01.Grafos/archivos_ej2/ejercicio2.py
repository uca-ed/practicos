import json
import os
 
CARPETA_SCRIPT = os.path.dirname(os.path.abspath(__file__))
 
 
def cargar_relacion(nombre_archivo):
    ruta = os.path.join(CARPETA_SCRIPT, nombre_archivo)
    with open(ruta, "r", encoding="utf-8") as f:
        datos = json.load(f)
 
    P = datos["P"]
 
    E = {}
    for elemento in datos["E"]:
        E[elemento] = set(datos["E"][elemento])
 
    return P, E
 
 
def reflexiva(P, E):
    for p in P:
        if p not in E[p]:
            return False
    return True
 
 
def simetrica(P, E):
    for p in P:
        for q in E[p]:
            if p not in E[q]:
                return False
    return True
 
 
def antisimetrica(P, E):
    for p in P:
        for q in E[p]:
            if q != p and p in E[q]:
                return False
    return True
 
 
def transitiva(P, E):
    for p in P:
        for q in E[p]:
            for r in E[q]:
                if r not in E[p]:
                    return False
    return True
 
 
def analizar_archivo(nombre_archivo):
    print(f"--- {nombre_archivo} ---")
 
    P, E = cargar_relacion(nombre_archivo)
 
    print(f"Cantidad de elementos: {len(P)}")
 
    es_reflexiva = reflexiva(P, E)
    es_simetrica = simetrica(P, E)
    es_antisimetrica = antisimetrica(P, E)
    es_transitiva = transitiva(P, E)
 
    if es_reflexiva:
        print("La relación es reflexiva")
    else:
        print("La relación no es reflexiva")
 
    if es_simetrica:
        print("La relación es simétrica")
    else:
        print("La relación no es simétrica")
 
    if es_antisimetrica:
        print("La relación es antisimétrica")
    else:
        print("La relación no es antisimétrica")
 
    if es_transitiva:
        print("La relación es transitiva")
    else:
        print("La relación no es transitiva")
 
    if es_reflexiva and es_simetrica and es_transitiva:
        print("La relación es de equivalencia")
 
    if es_reflexiva and es_antisimetrica and es_transitiva:
        print("La relación es de orden")
 
    print()
 
 
def main():
    archivos = ["01.json", "02.json", "03.json"]
 
    for archivo in archivos:
        analizar_archivo(archivo)
 
 
main()