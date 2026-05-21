import json
import csv

def obtener_minimales(matriz, nodos):
    # Columnas que son todas 0
    minimales = []
    n = len(nodos)
    for j in range(n):
        columna_vacia = True
        for i in range(n):
            if matriz[i][j] != 0:
                columna_vacia = False
                break
        if columna_vacia:
            minimales.append(nodos[j])
    return minimales

def obtener_maximales(matriz, nodos):
    # Filas que son todas 0
    maximales = []
    for i, fila in enumerate(matriz):
        if all(valor == 0 for valor in fila):
            maximales.append(nodos[i])
    return maximales

def vecindad_derecha(nodo, matriz, nodos):
    if nodo not in nodos: return []
    idx = nodos.index(nodo)
    # Retorna los nodos donde la fila tiene un 1
    return [nodos[j] for j, val in enumerate(matriz[idx]) if val == 1]

def vecindad_izquierda(nodo, matriz, nodos):
    if nodo not in nodos: return []
    idx = nodos.index(nodo)
    # Retorna los nodos donde la columna tiene un 1
    return [nodos[i] for i, fila in enumerate(matriz) if fila[idx] == 1]

# FUNCIONES DE CARGA Y CONVERSIÓN

def matriz_adyacencia_nativa(G):
    P = G["P"]  # Lista de todos los nodos
    E = G["E"]  # Diccionario de conexiones
    
    n = len(P)
    matriz = [[0 for _ in range(n)] for _ in range(n)]
    mapa = {nodo: i for i, nodo in enumerate(P)}
    
    for origen, destinos in E.items():
        if origen in mapa:
            for d in destinos:
                if d in mapa:
                    matriz[mapa[origen]][mapa[d]] = 1
    return matriz

def cargar_csv_nativo(ruta):
    with open(ruta, 'r') as f:
        lector = csv.reader(f)
        matriz = [list(map(int, fila)) for fila in lector]
    nodos = [str(i) for i in range(len(matriz))]
    return matriz, nodos

# Procesar JSON
try:
    with open("01.json", 'r') as f:
        data = json.load(f)
    
    G_json = {"P": data['P'], "E": data['E']}
    nodos_json = G_json["P"]
    M_json = matriz_adyacencia_nativa(G_json)
    
    print(f"\nGrafo JSON (01.json):")
    print(f"Minimales: {obtener_minimales(M_json, nodos_json)}")
    print(f"Maximales: {obtener_maximales(M_json, nodos_json)}")
    
    # MOSTRAR VECINDADES PARA EL NODO '1' 
    test_nodo = "1"
    print(f"Vecindad Derecha de '{test_nodo}': {vecindad_derecha(test_nodo, M_json, nodos_json)}")
    print(f"Vecindad Izquierda de '{test_nodo}': {vecindad_izquierda(test_nodo, M_json, nodos_json)}")

except FileNotFoundError:
    print("\n[!] No se encontró 01.json")
except Exception as e:
    print(f"\n[!] Error procesando JSON: {e}")

# Procesar CSVs
archivos_csv = ["01.csv", "02.csv", "03.csv", "04.csv"]

for nombre_arc in archivos_csv:
    try:
        M_csv, nodos_csv = cargar_csv_nativo(nombre_arc)
        print(f"\nGrafo {nombre_arc}:")
        print(f"Minimales: {obtener_minimales(M_csv, nodos_csv)}")
        print(f"Maximales: {obtener_maximales(M_csv, nodos_csv)}")
        
        # MOSTRAR VECINDADES PARA EL NODO '0' 
        if len(nodos_csv) > 0:
            test_nodo_csv = nodos_csv[0] # Usamos el primer nodo disponible
            print(f"Vecindad Derecha de '{test_nodo_csv}': {vecindad_derecha(test_nodo_csv, M_csv, nodos_csv)}")
            print(f"Vecindad Izquierda de '{test_nodo_csv}': {vecindad_izquierda(test_nodo_csv, M_csv, nodos_csv)}")
            
    except FileNotFoundError:
        print(f"\n[!] No se encontró {nombre_arc}")
    except Exception as e:
        print(f"\n[!] Error procesando {nombre_arc}: {e}")
