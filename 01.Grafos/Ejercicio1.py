import json


def cargar_matriz_desde_csv(ruta_archivo):
    matriz = []
    with open(ruta_archivo, "r") as archivo:
        for linea in archivo:
            fila = [int(valor) for valor in linea.strip().split(",")]
            matriz.append(fila)
    return matriz


def cargar_matriz_desde_json(ruta_archivo_json):
    """Convierte un archivo JSON en una matriz de adyacencia"""
    with open(ruta_archivo_json, 'r') as archivo_json:
        estructura = json.load(archivo_json)

    # Mostrar la información de la vecindad derecha
    for i in estructura['E']:
        print(i)

    # Imprimir la vecindad derecha de un nodo específico (por ejemplo, 'a')
    print("Vecindad derecha de 'a':", estructura['E'].get('a', []))

    # Imprimir la cardinalidad de la vecindad derecha de 'a'
    print("Cardinalidad de la vecindad derecha de 'a':", len(estructura['E'].get('a', [])))

    # Convertir la estructura de JSON en una matriz de adyacencia
    cantidad_nodos = len(estructura['E'])
    matriz = [[0] * cantidad_nodos for _ in range(cantidad_nodos)]

    # Asumiendo que los nodos en el JSON son etiquetas (como 'a', 'b', etc.), los convertimos en índices numéricos
    nodos = list(estructura['E'].keys())
    nodo_a_indice = {nodo: i for i, nodo in enumerate(nodos)}

    # Construir la matriz de adyacencia
    for nodo, vecinos in estructura['E'].items():
        for vecino in vecinos:
            matriz[nodo_a_indice[nodo]][nodo_a_indice[vecino]] = 1

    return matriz

def minimales(matriz):
    """Nodos sin entradas (columnas con solo ceros)"""
    nodos = []
    cantidad_nodos = len(matriz)
    for j in range(cantidad_nodos):
        suma_columna = 0
        for i in range(cantidad_nodos):
            suma_columna += matriz[i][j]
        if suma_columna == 0:
            nodos.append(j)
    return nodos

def maximales(matriz):
    """Nodos sin salidas (filas con solo ceros)"""
    nodos = []
    for i in range(len(matriz)):
        if sum(matriz[i]) == 0:
            nodos.append(i)
    return nodos

def vecindad_derecha(matriz, nodo):
    """Nodos alcanzables desde el nodo (adyacentes salientes)"""
    vecinos = []
    for j in range(len(matriz[nodo])):
        if matriz[nodo][j] != 0:
            vecinos.append(j)
    return vecinos

def vecindad_izquierda(matriz, nodo):
    """Nodos que llegan al nodo (adyacentes entrantes)"""
    vecinos = []
    for i in range(len(matriz)):
        if matriz[i][nodo] != 0:
            vecinos.append(i)
    return vecinos


# --- Ejemplo de uso ---
if __name__ == "__main__":
    ruta_json = "01.json"
    ruta_csv = "02.csv"
    matriz = cargar_matriz_desde_json("01.json")

    print("Minimales:", minimales(matriz))
    
    print("Maximales:", maximales(matriz))

    nodo = 0  # Puedes elegir el nodo que prefieras
    print(f"Vecindad derecha del nodo {nodo}:", vecindad_derecha(matriz, nodo))
    print(f"Vecindad izquierda del nodo {nodo}:", vecindad_izquierda(matriz, nodo))
