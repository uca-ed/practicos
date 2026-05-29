import json
import os
import numpy as np
import pandas as pd

def cargar_datos_ej2(ruta):
    if ruta.endswith('.json'):
        with open(ruta, 'r', encoding='utf-8') as f:
            datos = json.load(f)
        nodos = [str(n).strip() for n in datos.get('P', [])]
        n = len(nodos)
        mapa = {nodo: i for i, nodo in enumerate(nodos)}
        # Usamos uint8 para ahorrar memoria (1 byte por celda)
        matriz = np.zeros((n, n), dtype=np.uint8)
        for k, v in datos.items():
            if k == 'P': continue
            k_s = str(k).strip()
            if k_s in mapa:
                for dest in v:
                    d_s = str(dest).strip()
                    if d_s in mapa:
                        matriz[mapa[k_s]][mapa[d_s]] = 1
        return matriz
    else:
        df = pd.read_csv(ruta, index_col=0, sep=None, engine='python').fillna(0)
        return df.values.astype(np.uint8)

def analizar_propiedades(m):
    n = len(m)
    
    # 1. REFLEXIVA
    es_reflexiva = np.all(np.diag(m) == 1)
    
    # 2. SIMÉTRICA
    es_simetrica = np.all(m == m.T)
    
    # 3. ANTISIMÉTRICA
    m_sin_diag = m.copy()
    np.fill_diagonal(m_sin_diag, 0)
    es_antisimetrica = not np.any(m_sin_diag & m_sin_diag.T)
    
    # 4. TRANSITIVIDAD
    es_transitiva = True
    if n > 1000:
        print(f"   (Calculando transitividad para {n} nodos...)")
    
    for i in range(n):
        sucesores = np.where(m[i] == 1)[0]
        for s in sucesores:
            if s == i: continue
            # Si i apunta a s, y s apunta a j, entonces i sí o sí tiene que apuntar a j
            # Si s llega a un lugar donde i no llega, la transitividad se rompe
            if np.any((m[s] == 1) & (m[i] == 0)):
                es_transitiva = False
                break
        if not es_transitiva:
            break
            
    print(f"Propiedades: Reflexiva={es_reflexiva}, Simetrica={es_simetrica}, Antisimetrica={es_antisimetrica}, Transitiva={es_transitiva}")
    
    if es_reflexiva and es_transitiva:
        if es_simetrica: return "RELACION DE EQUIVALENCIA"
        if es_antisimetrica: return "RELACION DE ORDEN"
    return "RELACION GENERAL"

if __name__ == "__main__":
    print("\n--- EJERCICIO 2: PROPIEDADES ---")
    archivos = [
        ("01.json", "archivos_ej2/01.json"),
        ("02.json", "archivos_ej2/02.json"),
        ("03.json", "archivos_ej2/03.json")
    ]
    
    for nombre, ruta in archivos:
        if os.path.exists(ruta):
            print(f"\nAnalizando: {nombre}")
            try:
                matriz = cargar_datos_ej2(ruta)
                resultado = analizar_propiedades(matriz)
                print(f"Resultado: {resultado}")
            except Exception as e:
                print(f"Error procesando {nombre}: {e}")
            print("-" * 30)