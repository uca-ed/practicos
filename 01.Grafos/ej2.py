import json
import os

def verificar_propiedades(matriz, nodos):
    n = len(nodos)
    
    # 1. Reflexividad: Solo se evalúa la diagonal principal (i == j)
    es_reflexiva = all(matriz[i][i] == 1 for i in range(n))
    
    # 2. Simetría: Solo el triángulo superior (j > i). Compara M[i][j] con M[j][i]
    es_simetrica = True
    for i in range(n):
        for j in range(i + 1, n):  # j arranca desde i + 1
            if matriz[i][j] != matriz[j][i]:
                es_simetrica = False
                break
        if not es_simetrica: break
    
    # 3. Antisimetría: Solo el triángulo superior (j > i). Verifica que no haya doble vía
    es_antisimetrica = True
    for i in range(n):
        for j in range(i + 1, n):  # j arranca desde i + 1
            if matriz[i][j] == 1 and matriz[j][i] == 1:
                es_antisimetrica = False
                break
        if not es_antisimetrica: break
    
    # 4. Transitividad: Requiere obligatoriamente evaluar toda la matriz
    es_transitiva = True
    for i in range(n):
        for j in range(n):
            if matriz[i][j] == 1:
                for k in range(n):
                    if matriz[j][k] == 1 and matriz[i][k] == 0:
                        es_transitiva = False
                        break
            if not es_transitiva: break
        if not es_transitiva: break
                
    return es_reflexiva, es_simetrica, es_antisimetrica, es_transitiva

def clasificar_grafo(ref, sim, ant, tra):
    if ref and sim and tra:
        return "RELACIÓN DE EQUIVALENCIA"
    elif ref and ant and tra:
        return "RELACIÓN DE ORDEN PARCIAL"
    else:
        return "SIN CLASIFICACIÓN ESTÁNDAR"

def cargar_grafo_json(ruta):
    with open(ruta, 'r') as f:
        data = json.load(f)
    
    nodos = data['P']
    n = len(nodos)
    mapa_indices = {nodo: i for i, nodo in enumerate(nodos)}
    
    # Inicializar matriz de adyacencia con ceros
    matriz = [[0 for _ in range(n)] for _ in range(n)]
    
    # Llenar la matriz con las conexiones de 'E'
    for origen, destinos in data['E'].items():
        if origen in mapa_indices:
            idx_origen = mapa_indices[origen]
            for d in destinos:
                if d in mapa_indices:
                    idx_destino = mapa_indices[d]
                    matriz[idx_origen][idx_destino] = 1
                    
    return matriz, nodos

archivos_nuevos = ["01.json", "02.json","03.json"]

for archivo in archivos_nuevos:
    if os.path.exists(archivo):
        try:
            print(f"\n>>> Procesando: {archivo}...")
            M, N = cargar_grafo_json(archivo)
            
            # Realizar el test de propiedades
            r, s, a, t = verificar_propiedades(M, N)
            
            print(f"Reflexiva: {r}")
            print(f"Simétrica: {s}")
            print(f"Antisimétrica: {a}")
            print(f"Transitiva: {t}")
            print(f"RESULTADO: {clasificar_grafo(r, s, a, t)}")
            
        except Exception as e:
            print(f"Error al procesar {archivo}: {e}")
    else:
        print(f"\n[!] No se encontró el archivo: {archivo}")
