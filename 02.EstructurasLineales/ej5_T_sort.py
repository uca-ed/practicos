import sys
import json
from collections import deque


def armar_grafo(nodos, aristas):
    """
    Equivalente a tu 'armar_indices'. 
    Prepara las estructuras de datos que el algoritmo necesita.
    """
    adj = {}
    in_degree = {}

    # Nodos sin dependencias
    for nodo in nodos:
        nodo_int = int(nodo)
        adj[nodo_int] = []
        in_degree[nodo_int] = 0

    # Lista de adyacencia y a eso le sumamos los grados de entrada
    for u_str, vecinos in aristas.items():
        u = int(u_str)
        for v_str in vecinos:
            v = int(v_str)
            adj[u].append(v)
            in_degree[v] += 1

    return adj, in_degree


def tsort(nodos, aristas):

    adj, in_degree = armar_grafo(nodos, aristas)
    node_count = len(nodos)
    
    Q = deque() # crea la cola 
    
    # Encolar todos los nodos que tienen grado de entrada 0
    for nodo in in_degree:
        if in_degree[nodo] == 0:
            Q.append(nodo)

    ordenadas = []

    while Q:
        u = Q.popleft() 
        ordenadas.append(u)

        # Reducimos el grado de entrada de los vecinos
        for v in adj[u]:
            in_degree[v] -= 1
            # Si ya no tiene dependencias va a entrar a la cola
            if in_degree[v] == 0:
                Q.append(v)

    if len(ordenadas) != node_count:
        return None # Aca nos dice si es cíclico

    return ordenadas


def cargar_archivo(nombre):

    nodos = []
    aristas = {}
    try:
        with open(nombre, encoding="utf-8") as f:
            data = json.load(f)
            nodos = data.get("P", [])
            aristas = data.get("E", {})
            
    except OSError:
        print(f"No se pudo abrir '{nombre}'", file=sys.stderr)
    except json.JSONDecodeError:
        print(f"El archivo '{nombre}' no tiene un formato JSON válido.", file=sys.stderr)

    return nodos, aristas


def main():
    if len(sys.argv) < 2:
        print(f"Uso: python3 {sys.argv[0]} archivo.json", file=sys.stderr)
        sys.exit(1)

    nombre_archivo = sys.argv[1]
    nodos, aristas = cargar_archivo(nombre_archivo)

    if not nodos:
        print("No se cargaron nodos. Verifica el formato del archivo JSON.")
        return

    ordenadas = tsort(nodos, aristas)

    if ordenadas is None:
        print("Error: La estructura es cíclica. No se puede calcular el T-Sort.")
    else:
        print(f"T-Sort Exitoso! Ordenados {len(ordenadas)} nodos.")
        with open("salida_tsort.txt", "w", encoding="utf-8") as out:
            out.write(" ".join(map(str, ordenadas)) + "\n")
        
        print("Muestra de los primeros 20 elementos:")
        print(ordenadas[:20])
        print("... (Secuencia completa guardada en 'salida_tsort.txt')")


if __name__ == "__main__":
    main()


# EL ARCHIVO FUE PORBADO CON EXITO CON EL GRAFO DE esDivisorDe-2000.json, de la unidad 1 y devolvio lo siguiente: T-Sort Exitoso! Ordenados 1999 nodos. Muestra de los primeros 20 elementos: [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67] ... (Secuencia completa guardada en 'salida_tsort.txt') 
# Esta el txt del T-Sort en la carpeta de la unidad 2, con el nombre salida_tsort.txt