import json
import os
import numpy as np
import pandas as pd

class Grafo:
    def __init__(self, matriz, nombres_nodos):
        self.matriz = np.array(matriz).astype(np.int8)
        self.nodos = [str(n).strip() for n in nombres_nodos]
        self.mapa = {nombre: i for i, nombre in enumerate(self.nodos)}

    def vecindad_derecha(self, nodo):
        n_str = str(nodo).strip()
        if n_str not in self.mapa: return []
        idx = self.mapa[n_str]
        return [self.nodos[j] for j, val in enumerate(self.matriz[idx]) if val == 1 and j != idx]

    def obtener_minimales(self):
        n = len(self.nodos)
        m_sin_diag = self.matriz.copy()
        np.fill_diagonal(m_sin_diag, 0)
        # Un nodo es minimal si ningún OTRO nodo apunta hacia él (la suma de la columna externa es 0)
        sumas_columnas = np.sum(m_sin_diag, axis=0)
        return [self.nodos[j] for j in range(n) if sumas_columnas[j] == 0]

    def obtener_maximales(self):
        n = len(self.nodos)
        m_sin_diag = self.matriz.copy()
        np.fill_diagonal(m_sin_diag, 0)
        sumas_filas = np.sum(m_sin_diag, axis=1)
        return [self.nodos[i] for i in range(n) if sumas_filas[i] == 0]

def cargar_datos_ej1(ruta):
    if ruta.endswith('.json'):
        with open(ruta, 'r', encoding='utf-8') as f:
            datos = json.load(f)
        nodos = [str(n).strip() for n in datos.get('P', [])]
        mapa = {n: i for i, n in enumerate(nodos)}
        matriz = np.zeros((len(nodos), len(nodos)), dtype=np.int8)
        for k, v in datos.items():
            if k == 'P': continue
            k_s = str(k).strip()
            if k_s in mapa:
                for dest in v:
                    d_s = str(dest).strip()
                    if d_s in mapa:
                        matriz[mapa[k_s]][mapa[d_s]] = 1
        return Grafo(matriz, nodos)
    else:
        df = pd.read_csv(ruta, index_col=0)
        return Grafo(df.values, df.index.astype(str).tolist())

if __name__ == "__main__":
    print("\n--- EJERCICIO 1: OPERADORES ---")
    archivos = ["archivos_ej1/01.csv", "archivos_ej1/01.json", "archivos_ej1/02.csv", "archivos_ej1/03.csv", "archivos_ej1/04.csv"]
    for r in archivos:
        if os.path.exists(r):
            print(f"\nProcesando: {os.path.basename(r)}")
            g = cargar_datos_ej1(r)
            print(f"Minimales: {g.obtener_minimales()[:5]}...")
            print(f"Maximales: {g.obtener_maximales()[:5]}...")
            if g.nodos:
                print(f"Vecindad Derecha de '{g.nodos[0]}': {g.vecindad_derecha(g.nodos[0])[:5]}...")