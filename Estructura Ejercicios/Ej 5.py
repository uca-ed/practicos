from collections import deque, defaultdict

def archivo(nombre_archivo):
    with open("Archivo para ej/grafo.txt", "r") as f:
        lineas = f.readlines()
        num_nodos = int(lineas[0].strip())
        aristas = [tuple(map(int, linea.strip().split())) for linea in lineas[1:]]
    return num_nodos, aristas

def orden(num_nodos, aristas):
    grafo = defaultdict(list)
    grado_entrada = [0] * num_nodos

    # Construimos el grafo
    for origen, destino in aristas:
        grafo[origen].append(destino)
        grado_entrada[destino] += 1

    # Inicializamos la cola con nodos sin predecesores
    cola = deque([nodo for nodo in range(num_nodos) if grado_entrada[nodo] == 0])

    orden_final = []

    while cola:
        nodo = cola.popleft()
        orden_final.append(nodo)

        for vecino in grafo[nodo]:
            grado_entrada[vecino] -= 1
            if grado_entrada[vecino] == 0:
                cola.append(vecino)

    # Si no se procesan todos los nodos, significa que hay ciclo
    if len(orden_final) != num_nodos:
        return None  # El grafo tiene ciclos

    return orden_final

# ---- Main ----
nombre_archivo = "poner nombre del archivo"  # cambiar el nombre del archivo aquí

num_nodos, aristas = archivo(nombre_archivo)
resultado = orden(num_nodos, aristas)

if resultado is None:
    print("⚠ El grafo tiene ciclos. No es posible calcular T-Sort.")
else:
    print("✅ Secuencia de orden topológico (T-Sort):", resultado)