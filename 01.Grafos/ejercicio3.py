import json
import os
from collections import deque

def cargar_json_bfs(ruta):
    with open(ruta, 'r', encoding='utf-8') as f:
        datos = json.load(f)
    return datos, set(str(n) for n in datos.get('P', []))

def buscar_camino(datos, inicio, fin, nodos_validos):
    inicio, fin = str(inicio).strip(), str(fin).strip()
    if inicio not in nodos_validos or fin not in nodos_validos:
        return None
    
    cola = deque([(inicio, [inicio])])
    visitados = {inicio}
    
    while cola:
        actual, camino = cola.popleft()
        if actual == fin: return camino
        
        for vecino in datos.get(actual, []):
            v_s = str(vecino).strip()
            if v_s not in visitados:
                visitados.add(v_s)
                cola.append((v_s, camino + [v_s]))
    return None

if __name__ == "__main__":
    print("\n--- EJERCICIO 3: CAMINOS ---")
    pruebas = [
        ("esDivisorDe-200.json", "2", "128"),
        ("esDivisorDe-2000.json", "2", "1024"),
        ("esDivisorDe-20000_corregido.json", "2", "16384"),
        ("multiplos200Ref.json", "10", "10"),
        ("multiplos2000Ref.json", "50", "50"),
        ("multiplos20000Ref.json", "1000", "1000")
    ]
    for archivo, inicio, fin in pruebas:
        path = f"archivos_ej3/{archivo}" if os.path.exists(f"archivos_ej3/{archivo}") else archivo
        if os.path.exists(path):
            print(f"\nArchivo: {archivo}")
            datos, nodos = cargar_json_bfs(path)
            camino = buscar_camino(datos, inicio, fin, nodos)
            print(f"Ruta {inicio} a {fin}: {' -> '.join(camino) if camino else 'Sin conexión'}")