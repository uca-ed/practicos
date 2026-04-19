import json
import numpy as np
import os

#------------------------------------------- Ejercicio 1 -------------------------------------------

class Grafo:
    def __init__(self, matriz, nombres_nodos):
        self.matriz = np.array(matriz)
        self.nodos = [str(n) for n in nombres_nodos]  # Convertimos a string por seguridad
        self.mapa = {nombre: i for i, nombre in enumerate(self.nodos)}

    def vecindad_derecha(self, nodo):
        nodo_str = str(nodo)
        if nodo_str not in self.mapa: return []
        idx = self.mapa[nodo_str]
        return [self.nodos[j] for j, val in enumerate(self.matriz[idx]) if val == 1]

    def vecindad_izquierda(self, nodo):
        nodo_str = str(nodo)
        if nodo_str not in self.mapa: return []
        idx = self.mapa[nodo_str]
        return [self.nodos[i] for i, fila in enumerate(self.matriz) if fila[idx] == 1]

    def obtener_minimales(self):
        # Suma de columnas = 0 (nadie entra)
        return [self.nodos[i] for i in range(len(self.nodos)) if np.sum(self.matriz[:, i]) == 0]

    def obtener_maximales(self):
        # Suma de filas = 0 (nadie sale)
        return [self.nodos[i] for i in range(len(self.nodos)) if np.sum(self.matriz[i, :]) == 0]

# --- FUNCIONES DE CARGA ---

def cargar_json(ruta):
    with open(ruta, 'r') as f:
        datos = json.load(f)
    nodos = list(datos['E'].keys())
    n = len(nodos)
    mapa = {nodo: i for i, nodo in enumerate(nodos)}
    matriz = np.zeros((n, n), dtype=int)
    for nodo, vecinos in datos['E'].items():
        for v in vecinos:
            matriz[mapa[nodo]][mapa[v]] = 1
    return Grafo(matriz, nodos)

def cargar_csv(ruta):
    matriz = np.genfromtxt(ruta, delimiter=',', dtype=int)
    # Si la matriz es de un solo elemento, hay que ajustarla
    if matriz.ndim == 0: matriz = matriz.reshape((1, 1))
    nodos = [str(i) for i in range(len(matriz))]
    return Grafo(matriz, nodos)

# --- EJECUCIÓN ---

# Usamos rutas relativas a la carpeta actual (01.Grafos)
archivos = [
    ("JSON 01", "archivos_ej1/01.json", "json"),
    ("CSV 01", "archivos_ej1/01.csv", "csv"),
    ("CSV 02", "archivos_ej1/02.csv", "csv"),
    ("CSV 03", "archivos_ej1/03.csv", "csv"),
    ("CSV 04", "archivos_ej1/04.csv", "csv")
]

print("--- INICIANDO PROCESAMIENTO DE GRAFOS ---")

for nombre, ruta, tipo in archivos:
    if os.path.exists(ruta):
        print(f"\n>>> {nombre} ({ruta})")
        try:
            g = cargar_json(ruta) if tipo == "json" else cargar_csv(ruta)
            print(f"Minimales: {g.obtener_minimales()}")
            print(f"Maximales: {g.obtener_maximales()}")
            if len(g.nodos) > 0:
                print(f"Vecindad Derecha de '{g.nodos[0]}': {g.vecindad_derecha(g.nodos[0])}")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print(f"\n[!] Archivo no encontrado: {ruta}")

print("\n--- FIN DEL PROCESAMIENTO ---")

#------------------------------------------- Ejercicio 2 -------------------------------------------

def analizar_relacion(matriz):
    n = len(matriz)
    # 1. REFLEXIVIDAD: 
    es_reflexiva = np.all(np.diag(matriz) == 1)
    
    # 2. SIMETRÍA
    es_simetrica = np.all(matriz == matriz.T)
    
    # 3. ANTISIMETRÍA: Si M[i,j]==1 y M[j,i]==1, entonces i==j
    
    solo_diagonal = matriz * matriz.T
    es_antisimetrica = np.all(np.diag(np.diag(solo_diagonal)) == solo_diagonal)
    
    # 4. TRANSITIVIDAD: M^2 debe estar contenida en M
    
    m_cuadrado = (np.dot(matriz, matriz) > 0).astype(int)
    es_transitiva = np.all(matriz >= m_cuadrado)
    
    print(f"Propiedades: Reflexiva={es_reflexiva}, Simétrica={es_simetrica}, Antisimétrica={es_antisimetrica}, Transitiva={es_transitiva}")
    
 
    if es_reflexiva and es_transitiva:
        if es_simetrica:
            return "RELACIÓN DE EQUIVALENCIA"
        if es_antisimetrica:
            return "RELACIÓN DE ORDEN"
    return "NINGUNA (Relación General)"          # EJERCICIO 2 
archivos_ej2 = [
    ("EJ2 - CSV 01", "archivos_ej2/01.csv"),
    ("EJ2 - CSV 02", "archivos_ej2/02.csv"),
    ("EJ2 - CSV 03", "archivos_ej2/03.csv")
]

print("\n--- ANALIZANDO PROPIEDADES (EJERCICIO 2) ---")
for nombre, ruta in archivos_ej2:
    if os.path.exists(ruta):
        print(f"\n>>> {nombre}")
        try:
            g = cargar_csv(ruta)
            resultado = analizar_relacion(g.matriz)
            print(f"Resultado Final: {resultado}")
        except Exception as e:
            print(f"Error: {e}")